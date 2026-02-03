import itertools

def is_tautology(expression):
    """
    Checks if a given propositional logic expression is a tautology.
    Variables must be lowercase letters (p, q, r, etc.)
    Supported operators:
    and, or, not, == (iff), != (xor)

    Example:
    is_tautology("(p or not p)") -> True
    """

    # Identify variables
    variables = sorted(list(set(c for c in expression if 'a' <= c <= 'z')))

    if not variables:
        return bool(eval(expression))

    # Generate all truth assignments
    truth_assignments = list(itertools.product([True, False], repeat=len(variables)))

    # Evaluate expression for all assignments
    for assignment in truth_assignments:
        env = dict(zip(variables, assignment))
        try:
            if not eval(expression, {}, env):
                return False
        except Exception as e:
            print("Error:", e)
            return False

    return True


# Test cases
if __name__ == "__main__":
    expr1 = "(p or not p)"
    print(f"Is '{expr1}' a tautology? {is_tautology(expr1)}")

    expr2 = "(p and not p)"
    print(f"Is '{expr2}' a tautology? {is_tautology(expr2)}")

    expr3 = "(not p or q) or (not q or p)"
    print(f"Is '{expr3}' a tautology? {is_tautology(expr3)}")
    exp4 = "p or not p"
    print(f"Is '{exp4}' a tautology? {is_tautology(exp4)}")