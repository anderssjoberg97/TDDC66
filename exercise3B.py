

#The main interpreter function.
#expression is a list or a string referencing values in the values list
#values is a list of the values which are referenced in the expression
def interpret(expression, values):
    #If expression is a list it is evaluated further
    if isinstance(expression, list):
        #When the expression list has a length of 3 it is a binary operation
        #which takes to operands
        #The operation is executed by the doOperation() function
        if len(expression)==3:
            return doOperation(interpret(expression[0], values), interpret(expression[2], values), expression[1])

        #When the expression list has a length of 2 it is a logical negation
        elif len(expression)==2:
            if expression[0]=="NOT":
                return not interpret(expression[1], values)
            else:
                return interpret(expression[1], values)

        #If expression is a list with a length of 1 then it is evaluated further
        elif len(expression)==1:
            return value(interpret(expression[0]))
    #If expression is not a list then it is either a constant with the values
    #true or false or it is a reference to a variable in the values list
    else:
        if strIsBool(expression): #Check if expression is a bool constant
            return strToBool(expression)
        else: #Otherwise get the value from values list
            return values[expression]

#The interpreter for operations
def doOperation(operand1, operand2, operator):
    if operator == "AND":
        return strToBool(operand1) and strToBool(operand2)
    elif operator == "OR":
        return strToBool(operand1) or strToBool(operand2)

#Returns a value of true or false depending on if a string is "truthy"
def strToBool(str):
    return str in ["true", "TRUE", "1", "True"]

#Returns a boolean from a "boolish" string
def strIsBool(str):
    return str in ["true", "TRUE", "1", "True", "false", "FALSE", "0", "False"]
