def expression_evaluation(expression):
    """
    Safely evaluates a mathematical expression passed as a string.

    Parameters
    ----------
    expression : str
        A string containing a mathematical expression to evaluate.
        Example: "3 + 4 * (2 - 1)"

    Returns
    -------
    str
        The result of the evaluated expression, converted to a string.
        Returns "Error" if evaluation fails (e.g., due to syntax or runtime errors).
    """

    # Attempt to evaluate the expression.
    # If it fails due to invalid syntax or any runtime error, return "Error".
    try:
        return str(eval(expression))
    except:
        return "Error"
