import logging
from pathlib import Path
from typing import Annotated, TypedDict

from langchain_core.messages import AnyMessage, ToolMessage
from langchain_ollama import ChatOllama
from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import END, START, StateGraph
from langgraph.graph.message import add_messages

from calculator_tool import calculator

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler(),
              logging.FileHandler("agent.log", encoding="utf-8")],
)
logger = logging.getLogger(__name__)

BASE_DIR = Path(__file__).resolve().parent
KNOWLEDGE_PATH = BASE_DIR / "knowledge.txt"


def load_knowledge() -> str:
    try:
        text = KNOWLEDGE_PATH.read_text(encoding="utf-8").strip()
        if not text:
            raise ValueError("knowledge.txt is empty.")
        return text
    except (OSError, ValueError):
        logger.exception("Could not load knowledge.txt.")
        raise


knowledge = load_knowledge()


class State(TypedDict):
    messages: Annotated[list[AnyMessage], add_messages]


llm = ChatOllama(model="qwen3:4b", temperature=0)
llm_with_tools = llm.bind_tools([calculator])


def agent_node(state: State):
    prompt = f"""
You are a helpful customer support agent.
Use the following document for company questions:
--- SAMPLE DOCUMENT ---
{knowledge}
--- END DOCUMENT ---
Rules:
1. Do not invent information not in the document.
2. If the document lacks an answer, say you do not have enough information.
3. Remember details from the current conversation.
4. Use the calculator tool for mathematical calculations.
5. Keep answers concise.
"""
    logger.info("Agent is processing a request.")
    response = llm_with_tools.invoke(
        [{"role": "system", "content": prompt}] + state["messages"]
    )
    if response.tool_calls:
        logger.info("LLM requested %d tool call(s).", len(response.tool_calls))
    return {"messages": [response]}


def route_after_agent(state: State):
    last = state["messages"][-1]
    return "calculator" if getattr(last, "tool_calls", None) else END


def calculator_node(state: State):
    last = state["messages"][-1]
    outputs = []
    for call in last.tool_calls:
        try:
            if call["name"] != calculator.name:
                result = "Error: unsupported tool."
            else:
                result = calculator.invoke(call["args"])
            logger.info("Calculator tool completed.")
        except Exception:
            logger.exception("Calculator tool failed.")
            result = "Error: calculator could not complete the request."
        outputs.append(ToolMessage(content=str(result), tool_call_id=call["id"]))
    return {"messages": outputs}


graph = StateGraph(State)
graph.add_node("agent", agent_node)
graph.add_node("calculator", calculator_node)
graph.add_edge(START, "agent")
graph.add_conditional_edges("agent", route_after_agent,
                            {"calculator": "calculator", END: END})
graph.add_edge("calculator", "agent")

app = graph.compile(checkpointer=MemorySaver())


def ask(question: str, thread_id: str = "customer-001") -> str:
    config = {"configurable": {"thread_id": thread_id}}
    logger.info("Received request (thread_id=%s).", thread_id)
    try:
        result = app.invoke(
            {"messages": [{"role": "user", "content": question}]},
            config=config,
        )
        logger.info("Request completed successfully.")
        return result["messages"][-1].content
    except Exception:
        logger.exception("Agent request failed.")
        return "Sorry, the agent encountered an error. Check agent.log for details."


def show_graph() -> str:
    return app.get_graph().draw_mermaid()
