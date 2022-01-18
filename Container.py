from operator import length_hint


class Container:
    word = []
    length = 0
    unsureWrongIdxMap = {}
    blankChar = "_"

    def __init__(self) -> None:
        pass

    def __init__(self, len) -> None:
        self.length = len
        self.word = self.length * [None]

    def checkIndex(self, idx):
        if idx < 0 or idx >= self.length:
            print("Wrong index: ", idx +
                  ". Should be in range" + 0 + "-" + (self.length-1))

    def unsureLetter(self, letter, wrongIdx):
        self.checkIndex(wrongIdx)
        if letter in self.unsureWrongIdxMap.keys():
            vals = self.unsureWrongIdxMap[letter]
            vals.append(wrongIdx)
        else:
            vals = [wrongIdx]
        self.unsureWrongIdxMap[letter] = vals

    def sureLetter(self, letter, correctIdx):
        self.checkIndex(correctIdx)
        self.word[correctIdx] = letter

    def getPossibilities(self):
        possibilities = []
        positions = [i for i in range(0, self.length) if self.word[i] == None]
        runningWord = self.word.copy()
        letters = list(self.unsureWrongIdxMap.keys())
        self.recurse(positions, letters, runningWord, possibilities)
        return possibilities

    def recurse(self, positions, letters, runningWord, possibilites):
        if len(positions) == 0 or len(letters) == 0:
            possibilites.append(self.fillInTheBlanks(runningWord))
            return
        for pos in positions:
            runningWordNew = runningWord.copy()
            positionsCopy = positions.copy()
            lettersCopy = letters.copy()
            letterNow = lettersCopy.pop(0)
            if pos not in self.unsureWrongIdxMap.get(letterNow):
                runningWordNew[pos] = letterNow
                positionsCopy.remove(pos)
                self.recurse(positionsCopy, lettersCopy,
                             runningWordNew, possibilites)

    def fillInTheBlanks(self, givenWord):
        return ' '.join([self.blankChar if x == None else x for x in givenWord])


if __name__ == "__main__":
    c = Container(5)
    c.unsureLetter("O", 1)
    c.unsureLetter("T", 0)
    c.unsureLetter("S", 3)
    possibilities = c.getPossibilities()
    for possibility in possibilities:
        print(possibility)
