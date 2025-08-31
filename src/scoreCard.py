from src.scores import Rolls
class ScoreCard:



    def __init__(self, pins):
        self.pins = pins

        self.__frames = list(pins)




    def computeScore(self):

        total = 0
        for rolls in self.getFrames():
            if int(rolls) == Rolls.STRIKE and self.getFrames()[rolls+1]  == Rolls.STRIKE:

                total +=10

            elif int(rolls) == Rolls.STRIKE and self.getFrames()[rolls+1] != Rolls.STRIKE:

                total +=10+ int(self.getFrames()[rolls+1]) + int(self.getFrames()[rolls+2])

            elif int(rolls) == Rolls.SPARE and self.getFrames()[rolls+1] == Rolls.STRIKE:

                total += (10-int(self.getFrames()[rolls-1])+10)

            elif int(rolls) == Rolls.SPARE and self.getFrames()[rolls+1] != Rolls.STRIKE:

                total += (10-int(self.getFrames()[rolls-1])+ self.getFrames()[rolls+1])
            
            elif rolls == Rolls.NONE:
                continue

            else:
                total += int(rolls)

        return total

    def getFrames(self):
        return self.__frames

    def getPins(self):
        return self.pins


    def getScore(self):
        score = self.getFrames()
        return score