def expression_evaluation(expression):
    try:
        return str(eval(expression))
    except:
        return "Error"