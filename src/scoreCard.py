from src.scores import Rolls
class ScoreCard:



    def __init__(self, pins):
        self.pins = pins

        self.__frames = list(pins)




    def translateScore(self):
        
        i = 0
        total = []
        for rolls in self.getFrames():

            if rolls == Rolls.NONE:

                total.append(0)
                i +=1

            elif rolls == Rolls.STRIKE and self.getFrames()[i+1]  == Rolls.STRIKE:

                total.append(10)
                i +=1

            elif rolls == Rolls.STRIKE and self.getFrames()[i+1] != Rolls.STRIKE:

                total.append(10 + (self.getFrames()[i+1]) + (self.getFrames()[i+2]))
                i +=1

            elif rolls == Rolls.SPARE and self.getFrames()[i+1] == Rolls.STRIKE:

                total.append(10-int(self.getFrames()[i-1])+10)
                i +=1

            elif rolls == Rolls.SPARE and self.getFrames()[i+1] == Rolls.NONE  :

                total.append(10 -int(self.getFrames()[i-1]))
                i +=1

            elif rolls == Rolls.SPARE and (self.getFrames()[i+1] != Rolls.STRIKE and self.getFrames()[i-1] == Rolls.NONE):

                total.append((10-0)+ int(self.getFrames()[i+1]))
                i +=1

            elif rolls == Rolls.SPARE and (self.getFrames()[i+1] != Rolls.STRIKE and self.getFrames()[i-1] != Rolls.NONE):

                total.append((10-int(self.getFrames()[i-1]))+ int(self.getFrames()[i+1]))
                i +=1

            else:
                total.append(int(rolls))
                i +=1
        return total
    
    def computeScore(self):
        
        score = self.translateScore()
        return sum(score)

    def getFrames(self):
        return self.__frames

    def getPins(self):
        return self.pins


    def getScore(self):
        score = self.getFrames()
        return score