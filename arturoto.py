
from collections import OrderedDict

import sys

import io



GlobalStack = []
#TokenQ must be revered before use
TokenQueue = []
EnviormentLevel = 0
CurrentStackIndex = 0
fileString = ''
primitives = (int, str, bool)


def importFromFile(input):
    inputFile = open(input, 'r')
    commandList = []

    for line in inputFile:
        commandList.append(line[:-1])
        #print("current: ", commandList)

    inputFile.close()



    #print(commandList)
    return commandList



def tokenizer(listOfString):
    #possibleToken = ''

    for string in listOfString:
        possibleToken = ''

        if "push" in string:
            possibleToken = string[5:]
            if possibleToken[0] == "-":
                possibleToken = possibleToken[1:]
                if possibleToken.isdigit():
                    TokenQueue.append( -int(possibleToken))
            elif "." in str(possibleToken):

                TokenQueue.append(":error:")


            elif possibleToken.isdigit():
                TokenQueue.append(int(possibleToken))

            elif possibleToken.isalnum() and not possibleToken.isdigit():
                TokenQueue.append( possibleToken)

            elif "\"" in possibleToken:
                TokenQueue.append(possibleToken[1:-1])
            else:
                TokenQueue.append(":error:")

        elif ":true:" in string:
            TokenQueue.append( True)
        elif ":false:" in string:
            TokenQueue.append( False)
        elif ":error:" in string:
            TokenQueue.append(":error:")
        elif "add" in string:
            TokenQueue.append( "add")
        elif "sub" in string:
            TokenQueue.append( "sub")
        elif "mul" in string:
            TokenQueue.append( "mul")
        elif "div" in string:
            TokenQueue.append( "div")
        elif "rem" in string:
            TokenQueue.append( "rem")
        elif "neg" in string:
            TokenQueue.append( "neg")
        elif "swap" in string:
            TokenQueue.append( "swap")
        elif "pop" in string:
            TokenQueue.append( "pop")
        elif "quit" in string:
            TokenQueue.append( "quit")

class Enviorment(object):
    def __init__ (self, commandQueue):
        self.stack = []
        self.commandQueue = commandQueue
        self.currentStackSize = 0



    # parser or grammar checker

    def interp_ish(self):


        for element in self.commandQueue:

            self.stack.append(element)

            # make sure to define these later in their own method def
            if element == "add":
                if len(self.stack) >= 3:
                    self.stack.pop()
                    a = self.stack.pop()
                    b = self.stack.pop()
                    if type(a) == int and type(b) == int:
                        self.stack.append(b+a)
                    else:
                        self.stack.append(b)
                        self.stack.append(a)
                        self.stack.append(":error:")
                elif len(self.stack) >=2:
                    self.stack.pop()
                    a = self.stack.pop()
                    self.stack.append(a)
                    self.stack.append(":error:")

                else:
                    self.stack.pop()
                    self.stack.append(":error:")


            elif element == "sub":
                if len(self.stack) >= 3:
                    self.stack.pop()
                    a = self.stack.pop()
                    b = self.stack.pop()
                    if type(a) == int and type(b) == int:
                        self.stack.append(b-a)

                    else:
                        self.stack.append(b)
                        self.stack.append(a)
                        self.stack.append(":error:")
                elif len(self.stack) >=2:
                    self.stack.pop()
                    a = self.stack.pop()
                    self.stack.append(a)
                    self.stack.append(":error:")

                else:
                    self.stack.pop()
                    self.stack.append(":error:")



            elif element == "mul":
                if len(self.stack) >= 3:
                    self.stack.pop()
                    a = self.stack.pop()
                    b = self.stack.pop()
                    if type(a) == int and type(b) == int:
                        self.stack.append(b*a)

                    else:
                        self.stack.append(b)
                        self.stack.append(a)
                        self.stack.append(":error:")
                elif len(self.stack) >=2:
                    self.stack.pop()
                    a = self.stack.pop()
                    self.stack.append(a)
                    self.stack.append(":error:")

                else:
                    self.stack.pop()
                    self.stack.append(":error:")

            elif element == "div":
                if len(self.stack) >= 3:
                    self.stack.pop()
                    a = self.stack.pop()
                    b = self.stack.pop()
                    if a == 0 :
                        self.stack.append(b)
                        self.stack.append(a)
                        self.stack.append(":error:")

                    elif type(a) == int and type(b) == int:
                        self.stack.append(b/a)

                    else:
                        self.stack.append(b)
                        self.stack.append(a)
                        self.stack.append(":error:")
                elif len(self.stack) >=2:
                    self.stack.pop()
                    a = self.stack.pop()
                    self.stack.append(a)
                    self.stack.append(":error:")

                else:
                    self.stack.pop()
                    self.stack.append(":error:")

            elif element == "rem":
                if len(self.stack) >= 3:
                    self.stack.pop()
                    a = self.stack.pop()
                    b = self.stack.pop()
                    if type(a) == int and type(b) == int:
                        self.stack.append(b%a)

                    else:
                        self.stack.append(b)
                        self.stack.append(a)
                        self.stack.append(":error:")
                elif len(self.stack) >=2:
                    self.stack.pop()
                    a = self.stack.pop()
                    self.stack.append(a)
                    self.stack.append(":error:")

                else:
                    self.stack.pop()
                    self.stack.append(":error:")

            elif element == "swap":
                if len(self.stack) >= 3:
                    self.stack.pop()
                    a = self.stack.pop()
                    b = self.stack.pop()
                    self.stack.append(a)
                    self.stack.append(b)

                elif len(self.stack) >=2:
                    self.stack.pop()
                    a = self.stack.pop()
                    self.stack.append(a)
                    self.stack.append(":error:")

                else:
                    self.stack.pop()
                    self.stack.append(":error:")

            elif element == "neg":
                if len(self.stack) >= 2:
                    self.stack.pop()
                    a = self.stack.pop()
                    if type(a) == int:
                        self.stack.append(-a)

                    else:
                        self.stack.append(a)
                        self.stack.append(":error:")
                else:
                    self.stack.pop()
                    self.stack.append(":error:")
            elif element == "pop":
                if len(self.stack) >= 2:
                    self.stack.pop()
                    a = self.stack.pop()
                else:
                    self.stack.pop()
                    self.stack.append(":error:")

            elif element == "quit":
                self.stack.pop()
                self.stack.reverse()



        #print(self.stack)
        return self.stack


def interpreter(input, output):

    inputFile = importFromFile(input)

    tokenizer(inputFile)

    e1 = Enviorment(TokenQueue)
    GlobalStack = e1.interp_ish()
    GlobalStack.reverse()


    outputFile = open(output, 'w')
    randomIndex = 0
    #GlobalStack.reverse()
    for element in GlobalStack:
        if not(str(element).isdigit()) and element == True:
            outputFile.write(":true:" + '\n')

        elif not(str(element).isdigit()) and element == False:
            outputFile.write(":false:" + '\n')

        else:
            outputFile.write(str(element) + '\n')

    #print(TokenQueue)

interpreter("sample_input3.txt", "samO1.txt")
