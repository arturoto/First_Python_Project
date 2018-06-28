

class VarSymbol:

    def __init__(self, Name, currentEnv, parentEnv):

        self.variableName = Name
        self.value = None
        self.environment = currentEnv
        self.parentEnvironment = parentEnv


    def __str__(self):

        return '\nVarSymbol(Name: {variableName}, Value: {value}, Environment: {environment}, Parent Environment: {parentEnvironment})'.format(
            variableName=self.variableName,
            value=self.value,
            environment=self.environment,
            parentEnvironment=repr(self.parentEnvironment)

        )
    def __repr__(self):
        return self.__str__()


class Environment(object):
    def __init__ (self, currentEnv=None, parentEnv=None):
        self.stack = []
        self.currentEnvironment = currentEnv
        self.parentEnvironment = parentEnv


    def __str__(self):
        """String representation of the class instance.
        Examples:
            Token(INTEGER, 3)
            Token(PLUS, '+')
            Token(MUL, '*')
        """
        return '\nEnvironment(Environment: {environment}, local Stack : {stack}, Parent Environment: {parentEnvironment})'.format(
            environment=self.currentEnvironment,
            stack=self.stack,
            parentEnvironment=repr(self.parentEnvironment),

        )

    ## Come back to this, this might be very useful



    ''' Returns type given a string if
        no string makes a match, return None'''
    def getVal(self, var):

        if isNegNum(var) or isNum(var):
            return int(var)
        elif var == ":unit:":
            return ":unit:"
        elif var == ":true:":
            return True
        elif var == ":false:":
            return False
        # test this
        elif var[0:] == "\"" and var[:-1] == "\"":
            return var
        else:
            return None


    def pushToStack(self, elem):
        if str(elem) == "True":
            self.stack.append(":true:")
        elif str(elem) == "False":
            self.stack.append(":false:")
        else:
            self.stack.append(elem)

    def pushError(self): self.stack.append(":error:")

    def binaryOperator(self):
        if len(self.stack) >= 3:
            self.stack.pop()
            a = self.stack[-1]
            b = self.stack[-2]
            self.stack.pop()
            self.stack.pop()
            return (a, b)
        else:
            self.stack.pop()
            return ()


    def ADD(self):
        tupl = self.binaryOperator()
        if len(tupl) == 0:
            self.pushToStack(":error:")
        else:
            try:
                a1, b1 = tupl
                if (("VAR:" == b1[:4]) and ("VAR:" == a1[:4])):
                    a = self.getVal(VariableList[search(a1[5:], self.currentEnvironment)].value)
                    b = self.getVal(VariableList[search(b1[5:], self.currentEnvironment)].value)
                    if (isNum(a) or isNegNum(a)) and (isNum(b) or isNegNum(b)):
                            self.pushToStack(str(b + a))
                    else:
                        raise Exception

                elif ((not("VAR:" == b1[:4])) and ("VAR:" == a1[:4])):
                    a = self.getVal(VariableList[search(a1[5:], self.currentEnvironment)].value)
                    b = self.getVal(b1)
                    if (isNum(a) or isNegNum(a)) and (isNum(b1) or isNegNum(b1)):

                        self.pushToStack(str(b + a))
                    else:
                        raise Exception


                elif(("VAR:" == b1[:4]) and (not("VAR:" == a1[:4]))):
                    a = self.getVal(a1)
                    b = self.getVal(VariableList[search(b1[5:], self.currentEnvironment)].value)
                    if (isNum(b) or isNegNum(b)) and (isNum(a1) or isNegNum(a1)):
                            self.pushToStack(str(b + a))
                    else:
                        raise Exception

                elif (type(self.getVal(a1)) == int and type(self.getVal(b1)) == int):
                    self.pushToStack(str(self.getVal(b1) + self.getVal(a1)))
                else:
                    raise Exception

            except Exception:
                self.pushToStack(tupl[1])
                self.pushToStack(tupl[0])
                self.pushError()


    def SUB(self):
        tupl = self.binaryOperator()
        if len(tupl) == 0:
            self.pushToStack(":error:")
        else:
            try:
                a1, b1 = tupl
                if (("VAR:" == b1[:4]) and ("VAR:" == a1[:4])):
                    a = self.getVal(VariableList[search(a1[5:], self.currentEnvironment)].value)
                    b = self.getVal(VariableList[search(b1[5:], self.currentEnvironment)].value)
                    if (isNum(a) or isNegNum(a)) and (isNum(b) or isNegNum(b)):
                            self.pushToStack(str(b - a))
                    else:
                        raise Exception

                elif ((not("VAR:" == b1[:4])) and ("VAR:" == a1[:4])):
                    a = self.getVal(VariableList[search(a1[5:], self.currentEnvironment)].value)
                    b = self.getVal(b1)
                    if (isNum(a) or isNegNum(a)) and (isNum(b1) or isNegNum(b1)):

                        self.pushToStack(str(b - a))
                    else:
                        raise Exception


                elif(("VAR:" == b1[:4]) and (not("VAR:" == a1[:4]))):
                    a = self.getVal(a1)
                    b = self.getVal(VariableList[search(b1[5:], self.currentEnvironment)].value)
                    if (isNum(b) or isNegNum(b)) and (isNum(a1) or isNegNum(a1)):
                            self.pushToStack(str(b - a))
                    else:
                        raise Exception

                elif (type(self.getVal(a1)) == int and type(self.getVal(b1)) == int):
                    self.pushToStack(str(self.getVal(b1) - self.getVal(a1)))
                else:
                    raise Exception

            except Exception:
                self.pushToStack(tupl[1])
                self.pushToStack(tupl[0])
                self.pushError()



    def MUL(self):
        tupl = self.binaryOperator()
        if len(tupl) == 0:
            self.pushToStack(":error:")
        else:
            try:
                a1, b1 = tupl
                if (("VAR:" == b1[:4]) and ("VAR:" == a1[:4])):
                    a = self.getVal(VariableList[search(a1[5:], self.currentEnvironment)].value)
                    b = self.getVal(VariableList[search(b1[5:], self.currentEnvironment)].value)
                    if (isNum(a) or isNegNum(a)) and (isNum(b) or isNegNum(b)):
                            self.pushToStack(str(b * a))
                    else:
                        raise Exception

                elif ((not("VAR:" == b1[:4])) and ("VAR:" == a1[:4])):
                    a = self.getVal(VariableList[search(a1[5:], self.currentEnvironment)].value)
                    b = self.getVal(b1)
                    if (isNum(a) or isNegNum(a)) and (isNum(b1) or isNegNum(b1)):

                        self.pushToStack(str(b * a))
                    else:
                        raise Exception


                elif(("VAR:" == b1[:4]) and (not("VAR:" == a1[:4]))):
                    a = self.getVal(a1)
                    b = self.getVal(VariableList[search(b1[5:], self.currentEnvironment)].value)
                    if (isNum(b) or isNegNum(b)) and (isNum(a1) or isNegNum(a1)):
                            self.pushToStack(str(b * a))
                    else:
                        raise Exception

                elif (type(self.getVal(a1)) == int and type(self.getVal(b1)) == int):
                    self.pushToStack(str(self.getVal(b1) * self.getVal(a1)))
                else:
                    raise Exception

            except Exception:
                self.pushToStack(tupl[1])
                self.pushToStack(tupl[0])
                self.pushError()


    def DIV(self):
        tupl = self.binaryOperator()
        if len(tupl) == 0:
            self.pushToStack(":error:")
        else:
            try:
                a1, b1 = tupl
                if (("VAR:" == b1[:4]) and ("VAR:" == a1[:4])):
                    a = self.getVal(VariableList[search(a1[5:], self.currentEnvironment)].value)
                    b = self.getVal(VariableList[search(b1[5:], self.currentEnvironment)].value)
                    if (isNum(a) or isNegNum(a)) and (isNum(b) or isNegNum(b)):
                            self.pushToStack(str(b / a))
                    else:
                        raise Exception

                elif ((not("VAR:" == b1[:4])) and ("VAR:" == a1[:4])):
                    a = self.getVal(VariableList[search(a1[5:], self.currentEnvironment)].value)
                    b = self.getVal(b1)
                    if (isNum(a) or isNegNum(a)) and (isNum(b1) or isNegNum(b1)):

                        self.pushToStack(str(b / a))
                    else:
                        raise Exception


                elif(("VAR:" == b1[:4]) and (not("VAR:" == a1[:4]))):
                    a = self.getVal(a1)
                    b = self.getVal(VariableList[search(b1[5:], self.currentEnvironment)].value)
                    if (isNum(b) or isNegNum(b)) and (isNum(a1) or isNegNum(a1)):
                            self.pushToStack(str(b / a))
                    else:
                        raise Exception

                elif (type(self.getVal(a1)) == int and type(self.getVal(b1)) == int):
                    self.pushToStack(str(self.getVal(b1) / self.getVal(a1)))
                else:
                    raise Exception

            except ZeroDivisionError:
                self.pushToStack(tupl[1])
                self.pushToStack(tupl[0])
                self.pushError()
            except Exception:
                self.pushToStack(tupl[1])
                self.pushToStack(tupl[0])
                self.pushError()

    def REM(self):
        tupl = self.binaryOperator()
        if len(tupl) == 0:
            self.pushToStack(":error:")
        else:
            try:
                a1, b1 = tupl
                if (("VAR:" == b1[:4]) and ("VAR:" == a1[:4])):
                    a = self.getVal(VariableList[search(a1[5:], self.currentEnvironment)].value)
                    b = self.getVal(VariableList[search(b1[5:], self.currentEnvironment)].value)
                    if (isNum(a) or isNegNum(a)) and (isNum(b) or isNegNum(b)):
                            self.pushToStack(str(b % a))
                    else:
                        raise Exception

                elif ((not("VAR:" == b1[:4])) and ("VAR:" == a1[:4])):
                    a = self.getVal(VariableList[search(a1[5:], self.currentEnvironment)].value)
                    b = self.getVal(b1)
                    if (isNum(a) or isNegNum(a)) and (isNum(b1) or isNegNum(b1)):

                        self.pushToStack(str(b % a))
                    else:
                        raise Exception


                elif(("VAR:" == b1[:4]) and (not("VAR:" == a1[:4]))):
                    a = self.getVal(a1)
                    b = self.getVal(VariableList[search(b1[5:], self.currentEnvironment)].value)
                    if (isNum(b) or isNegNum(b)) and (isNum(a1) or isNegNum(a1)):
                            self.pushToStack(str(b % a))
                    else:
                        raise Exception

                elif (type(self.getVal(a1)) == int and type(self.getVal(b1)) == int):
                    self.pushToStack(str(self.getVal(b1) % self.getVal(a1)))
                else:
                    raise Exception

            except ZeroDivisionError:
                self.pushToStack(tupl[1])
                self.pushToStack(tupl[0])
                self.pushError()
            except Exception:
                self.pushToStack(tupl[1])
                self.pushToStack(tupl[0])
                self.pushError()

    def SWAP(self):
        try:
            a, b = self.binaryOperator()
            self.pushToStack(a)
            self.pushToStack(b)
        except Exception:
            self.pushError()

    def EQUAL(self):
        tupl = self.binaryOperator()

        try:
            a1, b1 = tupl

            if(("VAR:" in b1) and ("VAR:" in a1)):
                a = self.getVal(VariableList[search(a1[5:], self.currentEnvironment)].value)
                b = self.getVal(VariableList[search(b1[5:], self.currentEnvironment)].value)
                if isNum(a) or isNegNum(a):
                    if isNum(b) or isNegNum(b):
                        self.pushToStack(str(b == a))
                    else:
                        raise Exception
                else:
                    raise Exception
            elif(not("VAR:" in b1) and ("VAR:" in a1)):
                a = self.getVal(VariableList[search(a1[5:], self.currentEnvironment)].value)
                if isNum(a) or isNegNum(a):
                    if isNum(b1) or isNegNum(b1):
                        self.pushToStack(str(self.getVal(b1) == a))
                    else:
                        raise Exception
                else:
                    raise Exception


            elif(("VAR:" in b1) and not("VAR:" in a1)):
                b = self.getVal(VariableList[search(b1[5:], self.currentEnvironment)].value)
                if isNum(b) or isNegNum(b):
                    if isNum(a1) or isNegNum(a1):
                        self.pushToStack(str(b == self.getVal(a1)))
                    else:
                        raise Exception
                else:
                    raise Exception

            elif (type(self.getVal(a1)) == int and type(self.getVal(b1)) == int):
                self.pushToStack(str(self.getVal(b1) == self.getVal(a1)))

            else:
                raise Exception
        except Exception:
            self.pushToStack(tupl[1])
            self.pushToStack(tupl[0])
            self.pushError()
    def LESSTHAN(self):
        tupl = self.binaryOperator()

        try:
            a1, b1 = tupl
            if(("VAR:" in b1) and ("VAR:" in a1)):
                a = self.getVal(VariableList[search(a1[5:], self.currentEnvironment)].value)
                b = self.getVal(VariableList[search(b1[5:], self.currentEnvironment)].value)
                if isNum(a) or isNegNum(a):
                    if isNum(b) or isNegNum(b):
                        self.pushToStack(str(b < a))
                    else:
                        raise Exception
                else:
                    raise Exception
            elif(not("VAR:" in b1) and ("VAR:" in a1)):
                a = self.getVal(VariableList[search(a1[5:], self.currentEnvironment)].value)
                if isNum(a) or isNegNum(a):
                    if isNum(b1) or isNegNum(b1):
                        self.pushToStack(str(self.getVal(b1) < a))
                    else:
                        raise Exception
                else:
                    raise Exception


            elif(("VAR:" in b1) and not("VAR:" in a1)):
                b = self.getVal(VariableList[search(b1[5:], self.currentEnvironment)].value)
                if isNum(b) or isNegNum(b):
                    if isNum(a1) or isNegNum(a1):
                        self.pushToStack(str(b < self.getVal(a1)))
                    else:
                        raise Exception
                else:
                    raise Exception

            elif (type(self.getVal(a1)) == int and type(self.getVal(b1)) == int):
                self.pushToStack(str(self.getVal(b1) < self.getVal(a1)))

            else:
                raise Exception

        except Exception:
            self.pushToStack(tupl[1])
            self.pushToStack(tupl[0])
            self.pushError()
    # exception raised at this positiopn!!!!!
    def AND(self):
        tupl = self.binaryOperator()

        if len(tupl) != 0:
            try:
                a1, b1 = tupl
                if(("VAR:" in b1) and ("VAR:" in a1)):
                    a = self.getVal(VariableList[search(a1[5:], self.currentEnvironment)].value)
                    b = self.getVal(VariableList[search(b1[5:], self.currentEnvironment)].value)
                    if isBool(a):
                        if isBool(b):
                            self.pushToStack(str(b and a))
                        else:
                            raise Exception
                    else:
                        raise Exception
                elif(not("VAR:" in b1) and ("VAR:" in a1)):
                    a = self.getVal(VariableList[search(a1[5:], self.currentEnvironment)].value)
                    if isBool(a):
                        if isBool(b1):
                            self.pushToStack(str(self.getVal(b1) and a))
                        else:
                            raise Exception
                    else:
                        raise Exception


                elif(("VAR:" in b1) and not("VAR:" in a1)):
                    b = self.getVal(VariableList[search(b1[5:], self.currentEnvironment)].value)
                    if isBool(b):
                        if isBool(a1):
                            self.pushToStack(str(b and self.getVal(a1)))
                        else:
                            raise Exception
                    else:
                        raise Exception

                elif (type(self.getVal(a1)) == type(True) and type(self.getVal(b1)) == type(True)):
                    self.pushToStack(str(self.getVal(b1) and self.getVal(a1)))

                else:
                    raise Exception
            except Exception:

                self.pushToStack(tupl[1])
                self.pushToStack(tupl[0])
                self.pushError()
        else:
            self.pushError()
    def OR(self):
        tupl = self.binaryOperator()

        if len(tupl) != 0:
            try:
                a1, b1 = tupl
                if(("VAR:" in b1) and ("VAR:" in a1)):
                    a = self.getVal(VariableList[search(a1[5:], self.currentEnvironment)].value)
                    b = self.getVal(VariableList[search(b1[5:], self.currentEnvironment)].value)
                    if isBool(a):
                        if isBool(b):
                            self.pushToStack(str(b or a))
                        else:
                            raise Exception
                    else:
                        raise Exception
                elif(not("VAR:" in b1) and ("VAR:" in a1)):
                    a = self.getVal(VariableList[search(a1[5:], self.currentEnvironment)].value)
                    if isBool(a):
                        if isBool(b1):
                            self.pushToStack(str(self.getVal(b1) or a))
                        else:
                            raise Exception
                    else:
                        raise Exception


                elif(("VAR:" in b1) and not("VAR:" in a1)):
                    b = self.getVal(VariableList[search(b1[5:], self.currentEnvironment)].value)
                    if isBool(b):
                        if isBool(a1):
                            self.pushToStack(str(b or self.getVal(a1)))
                        else:
                            raise Exception
                    else:
                        raise Exception

                elif (type(self.getVal(a1)) == type(True) and type(self.getVal(b1)) == type(True)):
                    self.pushToStack(str(self.getVal(b1) or self.getVal(a1)))

                else:
                    raise Exception
            except Exception:

                self.pushToStack(tupl[1])
                self.pushToStack(tupl[0])
                self.pushError()
        else:
            self.pushError()

    def BIND(self):

        tupl = self.binaryOperator()
        if len(tupl) == 0:
            self.pushToStack(":error:")
        else:
            try:
                a, b = tupl
                if a == ":error:":
                    raise Exception

                elif a == ":unit:":
                    bind(b[5:], self.currentEnvironment, a)
                    self.pushToStack(":unit:")

                elif len(VariableList) != 0 and b[:4] == "VAR:":
                    if bind(b[5:], self.currentEnvironment, a) == False:
                        raise Exception
                    self.pushToStack(":unit:")

                elif VariableList[search(a[5:], self.currentEnvironment)].value == None:
                    raise Exception

                else:
                    raise Exception

            except Exception:
                self.pushToStack(tupl[1])
                self.pushToStack(tupl[0])
                self.pushError()




#check
    def UnaryOp(self):
        if len(self.stack) >= 2:
            self.stack.pop()
            return self.stack.pop()
        else:
            self.stack.pop()
            return ()

    def NEG(self):
        a = self.UnaryOp()
        if(len(a) == 0):
            self.pushError()
        else:
            try:
                if "VAR:" == a[:4]:
                    value = VariableList[search(a[5:], self.currentEnvironment)].value
                    if isNum(value) or isNegNum(value):
                        self.stack.append(str(-int(value)))
                        return
                    else:
                        raise Exception
                elif isNum(a) or isNegNum(a):
                    self.stack.append(str(-int(a)))
                else:
                    raise Exception

            except Exception:
                self.stack.append(a)
                self.stack.append(":error:")

    def NOT(self):
        a = self.UnaryOp()
        if(len(a) == 0 ):
            self.pushError()
        else:
            try:
                if a == ":true:":
                    self.stack.append(":false:")
                elif a == ":false:":
                    self.stack.append(":true:")
                elif "VAR:" in a:
                    value = VariableList[search(a[5:], self.currentEnvironment)].value
                    if value == ":true:":
                        self.stack.append(":false:")
                    elif value == ":false:":
                        self.stack.append(":true:")
                    else:
                        raise Exception
                else:
                    raise Exception
            except Exception:
                self.stack.append(a)
                self.stack.append(":error:")




    def ternaryOp(self):
        if len(self.stack) >= 4 :
            self.stack.pop()
            a = self.stack[-1]
            b = self.stack[-2]
            c = self.stack[-3]
            self.stack.pop()
            self.stack.pop()
            self.stack.pop()
            return (a, b, c)
        else:
            self.stack.pop()
            return ()
    def IF(self):
        tupl = self.ternaryOp()
        if len(tupl) == 0:
            return self.pushToStack(":error:")
        else:
            try:
                a, b, c = tupl
                if c == ":true:":
                    self.pushToStack(tupl[0])
                elif c == ":false:":
                    self.pushToStack(tupl[1])

                elif "VAR:" in tupl[2]:
                    value = VariableList[search(c[5:], self.currentEnvironment)].value
                    if c == ":true:":
                        self.pushToStack(tupl[0])
                    elif c == ":false:":
                        self.pushToStack(tupl[1])
                    else:
                        raise Exception
                else:
                    raise Exception
            except Exception:
                self.pushToStack(tupl[0])
                self.pushToStack(tupl[1])
                self.pushToStack(tupl[2])
                self.pushError()
    def POP(self):
        if len(self.stack) >= 2:
            self.stack.pop()
            self.stack.pop()

        else:
            self.stack.pop()
            self.stack.append(":error:")




    # parser or grammar checker

    # this evaluator takes the tokens and evaluates them, uses the
    # inputs from the local stack to this environment
    def evaluator(self, element):
        #print("evaluating" + str(element))
        #print("EnvEval Recived: " + element)
        # compiles fine
        if element[:4] == "VAR:":
            self.stack.append(element)
            addSymbol(element[5:],  self.currentEnvironment, self.parentEnvironment)
            updateValue(element[5:], self.currentEnvironment)
        else:
            self.stack.append(element)


        if element == "add": self.ADD()
        elif element == "sub": self.SUB()
        elif element == "mul": self.MUL()
        elif element == "div": self.DIV()
        elif element == "rem": self.REM()
        elif element == "swap": self.SWAP()
        elif element == "neg": self.NEG()
        elif element == "and": self.AND()
        elif element == "or": self.OR()
        elif element == "not": self.NOT()
        elif element == "equal": self.EQUAL()
        elif element == "lessThan": self.LESSTHAN()
        elif element == "bind": self.BIND()
        elif element == "if": self.IF()
        elif element == "pop": self.POP()

        elif element == "quit":
            self.stack.pop()
        elif element == "qui":
            self.stack.pop()



        print("EVAL: "+ str(element))
        print("STACK: "+ str(self.stack))
        print("Current EnvState: " + str(EnvRelation))
        print("VarL: "+ str(VariableList))
        print("\n")


        #print(self.stack)
        #print(self.listOfVariables)
        #return self.stack













############################ Backend


TokenQueue = []
EnvironmentLevel = 0
CurrentStackIndex = 0
GlobalStack = []
EnvironmentList = []
VariableList = []
EnvRelation = {}



#searches the current enviorment for the given name
# returns the index in the variable list where the name is found
# or returns flase if not existent
def searchEnv(name, env):
    index = 0
    for elem in VariableList:
        if (elem.environment == env) and (elem.variableName == name):
            return index
        else:
            index += 1

    return False

def searchBool(name, env):

    if searchEnv(name, env) is not False:
        return True
    else:
        return False

# searches the scope where the variable can be found
# retuns index where closes variable exists
# returns false if it doesnt exist in symbol table
def search(name, env):
    if EnvRelation[env] == 0:
        return searchEnv(name, env)
    elif searchBool(name, env):
        return searchEnv(name, env)
    else:
        PE = EnvRelation[env]
        return search(name, PE)



#searches the parent scope of the variable
def searchInScope(name, env):
    PE = EnvRelation[env]
    if EnvRelation[env] == 0:
        return searchEnv(name, env)
    elif searchBool(name, PE):
        return searchEnv(name, PE)
    else:
        return searchInScope(name, PE)


#adds to current enviormemt
def addSymbol(name, CE, PE):
    possibleElem = searchEnv(name, CE)
    if possibleElem is False:
        VariableList.append(VarSymbol(name, CE, PE))


# if variable has been previously bound, it updates the value
def updateValue(name, CE):

    possibleElem = searchInScope(name, CE)
    currentElem = searchEnv(name, CE)
    if VariableList[currentElem].value == None:
        if possibleElem is not False:
            VariableList[currentElem].value = VariableList[possibleElem].value
            return VariableList[currentElem].value

def getVal(name, CE):
    posIndex = search(name, CE)
    return VariableList[posIndex].value


def bind(name, CE, val):

    posIndex = search(name, CE)
    value = None

    if val == ":true:" or val == ":false:" or val == ":unit:" or isNum(val) or isNegNum(val) or "\"" in val or "-" in val:
        value = val

    elif "VAR:" in val:
        value = VariableList[search(val[5:], CE)].value

    if value == None:
        return False

    VariableList[posIndex].value = value















def importFromFile(input):
    inputFile = open(input, 'r')
    commandList = []

    for line in inputFile:
        commandList.append(line[:-1])

    inputFile.close()
    return commandList



# only for push ops
def isNegNum(string):
    try:
        a = str(string)
        if len(a) > 1:
            if "-" == a[0] and a[1:].isdigit():
                return True
            else:
                False
        else:
            return False
    except Exception:
        return False
    return False


def isNum(string):
    if string == ":true:" or string == ":false:":
        return False
    try:
        a = str(string)
        return a.isdigit()
    except Exception:
        return False
    else:
        return False


def isBool(string):
    if type(string) == type(True):
        return True
    elif str(string) == ":true:":
        return True
    elif str(string) == ":false:":
        return True
    else:
        return False

def isName(string): return (string.isalnum() and not string.isdigit())

def pushERROR(): addToQueue(":error:")

def addToQueue(elem): TokenQueue.insert(0,elem)







def LexicalAnalysis(listOfString):

    for string in listOfString:
        possibleToken = ''


        if "push" in string:
            #addToQueue("push")
            possibleToken = string[5:]

            # push NegNumber
            if isNegNum(possibleToken):
                addToQueue(str(int(possibleToken)))
            # push Real
            elif "." in str(possibleToken):
                pushERROR()
            # push int
            elif possibleToken.isdigit():
                addToQueue(str(int(possibleToken)))
            # is qualified Name
            elif isName(possibleToken):
                addToQueue("VAR: " + possibleToken)
            # is string
            elif "\"" in possibleToken:
                addToQueue(possibleToken)
            elif possibleToken == ":true:":
                addToQueue(possibleToken)
            elif possibleToken == ":false:":
                addToQueue(possibleToken)
            # will take care of special chars
            else:
                pushERROR()

        elif ":true:" == string:    addToQueue(":true:")
        elif ":false:" == string:   addToQueue(":false:")
        elif ":error:" == string:     addToQueue(":error:")
        elif "add" == string:       addToQueue("add")
        elif "sub" == string:       addToQueue("sub")
        elif "mul" == string:       addToQueue("mul")
        elif "div" == string:       addToQueue("div")
        elif "rem" == string:       addToQueue("rem")
        elif "neg" == string:       addToQueue("neg")
        elif "swap" == string:      addToQueue("swap")
        elif "pop" == string:       addToQueue("pop")
        elif "quit" == string:      addToQueue("quit")
        elif "and" == string:       addToQueue("and")
        elif "or" == string:        addToQueue("or")
        elif "not" == string:       addToQueue("not")
        elif "equal" == string:     addToQueue("equal")
        elif "lessThan" == string:  addToQueue("lessThan")
        elif "bind" == string:      addToQueue("bind")
        elif "if" == string:        addToQueue("if")
        elif "let" == string:       addToQueue("let")
        elif "end" == string:       addToQueue("end")
        elif "quit" == string:      addToQueue("quit")
        elif "qui" == string:       addToQueue("qui")

    print("Lex Output: TokenQueue = " + str(TokenQueue))

def inputAndParse(input):

    inputFile = importFromFile(input)
    inputFile.reverse()
    print("Input File: " + str(inputFile))


    # This converts inputfile to tokens that that will be proccessed
    # by the environment handler
    LexicalAnalysis(inputFile)



def environmentInit(tokenQ):
    tokenQueue = tokenQ
    envCounter = 1
    currentEnv = 1
    prevEnv = 0

    #print("Tokens: "+ str(tokenQ))

    global GlobalStack
    global EnvironmentList
    global EnvRelation

    EnvRelation[0] = None
    EnvRelation[envCounter] = prevEnv
    EnvironmentList.append(Environment(None, None))
    EnvironmentList.append(Environment(envCounter, prevEnv))

    for tokens in tokenQueue:

        if tokens == "let":
            envCounter +=1
            currentEnv = envCounter
            prevEnv += 1
            EnvRelation[envCounter] = prevEnv
            EnvironmentList.append(Environment(envCounter, prevEnv))
            print("Evaluating \"LET\"\n")
            continue
            #print("entering Let "+ str(envCounter) + str(currentEnv) + str(prevEnv))
        if tokens == "end":
            print("Evaluating \"END\"")
            EnvironmentList[prevEnv].stack.append(EnvironmentList[currentEnv].stack[-1])
            currentEnv = prevEnv
            prevEnv -= 1
            #print("entering END "+ str(envCounter) + str(currentEnv) + str(prevEnv))
            continue
        if tokens == "quit":
            #print("\tInput \"quit\": Ending Program")
            break
        if tokens == "qui":
            #print("\tInput \"quit\": Ending Program")
            break

        #print("\tCurrent_Enviorment = " + str(currentEnv))
        #print("\nPassing to EnvEval: " + tokens)
        EnvironmentList[currentEnv].evaluator(tokens)

    GlobalStack = EnvironmentList[1].stack
    #print("\nFINAL STACK: " + str(GlobalStack) + "\n")




    print("################## FINAL STATE ###################")
    for elem in EnvironmentList:
        if elem.currentEnvironment == None:
            pass
        else:
            print(elem)

    print("Env Rel: " + str(EnvRelation))
    print("VarL: "+ str(VariableList))

def outputFile(output):
    outputFile = open(output, 'w')
    global GlobalStack

    GlobalStack.reverse()


    for element in GlobalStack:


        if "\"" == element[:1] and "\"" == element[:-1]:
            outputFile.write(element[1:-1] + '\n')
        elif "VAR:" == element[:4]:
            outputFile.write(element[5:] + '\n')
        else:
            outputFile.write(element + '\n')

    outputFile.close()



def interpreter(input, output):
    inputAndParse(input)
    environmentInit(TokenQueue)
    outputFile(output)


interpreter("sample_input2.txt", "samO1.txt")
