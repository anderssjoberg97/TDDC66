

#The main interpreter function.
#expression is a list or a string referencing values in the values list
#values is a list of the values which are referenced in the expression
def interpret(expression, values):
    #If expression is a list it is evaluated further
    if isinstance(expression, list):
        #When the expression list has a length of 3 it is a binary operation
        #which takes to operands
        #The operation is executed by the doOperation() function
        print("Is list")
        if len(expression)==3:
            print("Do operation"+str(interpret(expression[0], values)))
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
        print("Not list")
        if strIsBool(expression): #Check if expression is a bool constant
            print("Is stringBool converting to boolean"+str(expression))
            return strToBool(expression)
        else: #Otherwise get the value from values list
            print("getting values")
            return values[expression]

#The interpreter for operations
def doOperation(operand1, operand2, operator):

    if operator == "AND":
        return strToBool(operand1) and strToBool(operand2)
    elif operator == "OR":
        print("Doing operation OR: "+str(operand1)+" OR "+str(operand2))
        return operand1 or operand2

#Returns a value of true or false depending on if a string is "truthy"
def strToBool(boolString):
    print("Boolcheck("+str(boolString)+"): "+ str(boolString in ["true", "TRUE", "1", "True"]))
    return str in ["true", "TRUE", "1", "True"]

#Returns a boolean from a "boolish" string
def strIsBool(boolString):
    return boolString in ["true", "TRUE", "1", "True", "false", "FALSE", "0", "False"]
