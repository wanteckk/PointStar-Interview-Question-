from langchain_core.tools import tool

@tool
def calculator(a: float, b: float, operation: str) -> str:
    """Perform a basic calculation."""
    if operation == "add":
        return str(a + b)
    if operation == "subtract":
        return str(a - b)
    if operation == "multiply":
        return str(a * b)
    if operation == "divide":
        if b == 0:
            return "Error: division by zero is not allowed."
        return str(a / b)
    return "Error: unsupported operation."
