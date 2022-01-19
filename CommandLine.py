from Container import Container


class CommandLine:

    functionDict = {}

    def __init__(self, length) -> None:
        self.functionDict["SURE"] = self.addSure
        self.functionDict["UNSURE"] = self.addUnsure
        self.functionDict["REDUCE"] = self.reduce
        self.functionDict["DISPLAY"] = self.display
        self.functionDict["RESET"] = self.reset
        self.wordLength = length
        self.c = Container(self.wordLength)

    def daemon(self):
        while(True):
            cmd = input().strip().upper()
            if cmd is None or len(cmd) == 0:
                continue
            cmds = cmd.split()
            opern = cmds[0]
            inputList = cmds[1:]
            if opern in ["EXIT", "QUIT", "LOGOUT"]:
                break
            if opern in self.functionDict.keys():
                self.functionDict[opern](inputList)
            else:
                print("Valid commands are: " +
                      ','.join(self.functionDict.keys()))

    def checkInputList(self, inputList):
        errorMsgs = []
        if len(inputList) != 2:
            errorMsgs.append("The command should be followed by 2 params.")
        if len(inputList) >= 1 and len(inputList[0]) != 1:
            errorMsgs.append("The first param should be a single letter")
        digitStrings = [str(i) for i in range(0, self.wordLength)]
        if len(inputList) == 2 and inputList[1] not in digitStrings:
            errorMsgs.append(
                "The second param should be in the following: " + digitStrings)
        return errorMsgs

    def addUnsure(self, inputList):
        errorMsgs = self.checkInputList(inputList)
        if len(errorMsgs) > 0:
            for msg in errorMsgs:
                print(msg)
            return
        self.c.unsureLetter(inputList[0], int(inputList[1]))

    def addSure(self, inputList):
        errorMsgs = self.checkInputList(inputList)
        if len(errorMsgs) > 0:
            for msg in errorMsgs:
                print(msg)
            return
        self.c.sureLetter(inputList[0], int(inputList[1]))

    def display(self, inputList):
        possibilities = self.c.getPossibilities()
        for possibility in possibilities:
            print(possibility)

    def reduce(self, inputList):
        self.c.reduce()

    def reset(self, inputList):
        self.c = Container(self.wordLength)


if __name__ == "__main__":
    cli = CommandLine(5)
    cli.daemon()
