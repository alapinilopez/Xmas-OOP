class Frame:
    def __init__(self, pins, FirstSetUp, secondSetUp, frameScore):
        self.pins = pins
        self.FirstSetUp = FirstSetUp
        self.secondSetUp = secondSetUp
        self.frameScore = frameScore
        
    def setPins(self, newPins):
        self.pins = 10
        self.pins = newPins
    
    def getPins(self):
        return self.pins
    
    def setFirstSetUp(self, newFirstSetUp):
        self.setFirstSetUp = newFirstSetUp
        newFirstSetUp = self.pins - self.firstSetUp
        return newFirstSetUp
    
    def getFirstSetUp(self):
        return self.FirstSetUp
    
    def setSecondSetUp(self, newSecondSetUp):
        self.secondSetUp = newSecondSetUp
        newSecondSetUp = self.pins - self.secondSetUp
        return  newSecondSetUp
    
    def getFrameScore(self):
        return self.frameScore
    
    def setFrameScore(self, newFrameScore):
        self.frameScore = newFrameScore
        newFrameScore = self.FirstSetUp + self.secondSetUp
        return newFrameScore
        




