def calc(a, op, b):
    if op not in '+-/*':
        return None, 'Operator must be +-/*'
    try:
        if op == '+':
            result = a + b
        elif op == '-':
            result = a - b
        elif op == '/':
            result = a / b
        else:
            result = a * b
    except Exception as e:
        return None,e.__class__.__name__

    return result,str(result)
