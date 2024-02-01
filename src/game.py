import re
class Frame:
    VALID_CHARS = '123456789x-/'

    def __init__(self, pins=''):
        self.__pins = pins

    @property
    def pins(self):
        return self.__pins
    
    @pins.setter
    def pins(self,pins):
        self.__pins = pins
    
    @staticmethod
    def validatePins(pins):
        return all(char.lower() in Frame.VALID_CHARS for char in pins)
    
    def padPins(pins):
        # utiliza una regex para colocar un guión antes de una x exceptuando la ultima
        patron = re.compile(r'(?<!x)(x)(?!$)')
        return patron.sub(r'-\1', pins)


    
class ScoreCard:
    def __init__(self, pins):
        self.score = 0
        self.rolls = self.getRollsList(pins)
        self.frames = [Frame(frame) for frame in self.getRolls()] # cambio a la hora de construir los frames pasandole ya los elementos del turno validados
        
    def getFramePins(self):
        return [frame.pins for frame in self.getFrames()]

    def getFrames(self):
        return self.frames

    def getRolls(self):
        return self.rolls
    
    def getRollsList(self, pins):
        rolls = str(Frame.padPins(pins))
        # itera sobre los pines agregandolos a rollsList de dos en dos si los pines son válidos
        rollsList = [rolls[i:i + 2] for i in range(0, len(rolls), 2)] if Frame.validatePins(pins) else None
        lastRoll = ''
        # en caso de que el ultimo roll solo tenga un elemento, se lo agregamos al roll anterior
        if len(rollsList[-1]) < 2:
            lastRoll = rollsList[-1]
            rollsList.pop()
            rollsList[-1] = rollsList[-1] + lastRoll

        return rollsList
    

if __name__ == '__main__':

    pins = '81-92/x637-52x-62/x'
    scoreCard = ScoreCard(pins)
    #total3 = 122
    print(scoreCard.getRolls())

    pins2 = '1-x1232x123-x'
    scoreCard2 = ScoreCard(pins2)
    print(scoreCard2.getRolls())
    print(scoreCard2.getFramePins())

    pins3 = '12345123451234512345'
    scoreCard3 = ScoreCard(pins3)

    print(scoreCard3.getFramePins())
    
    