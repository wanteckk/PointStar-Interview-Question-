from agent import ask, show_graph


def run_demo():
    cases = [
        ("KNOWLEDGE", "What is the refund policy?"),
        ("POLICY GROUNDING", "Can I refund my purchase after 30 days?"),
        ("CALCULATOR", "What is 25 * 48?"),
        ("MEMORY - SET NAME", "My name is Wan Teck."),
        ("MEMORY - RECALL NAME", "What is my name?"),
        ("UNKNOWN INFORMATION", "What is PointStar's employee salary policy?"),
    ]
    for title, question in cases:
        print(f"\\n{'=' * 10} {title} {'=' * 10}")
        print("User:", question)
        print("Agent:", ask(question))
    print("\\n========== MERMAID GRAPH ==========")
    print(show_graph())


if __name__ == "__main__":
    run_demo()
