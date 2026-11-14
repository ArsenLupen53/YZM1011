def safe_calc(expression):

    try:
        left,right = expression.split("/")
        return float(left) / float(right)
    except ZeroDivisionError:
        return "cannot divide by zero"
    except ValueError:
        return "invalid input"
    
for e in ["10/4","7/0","x/3","8","1/2/3"]:
    print(e, "->", safe_calc(e))