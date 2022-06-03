from graphics import *
class Hand():
    def __init__(self, win, cardY, name):
        self.win = win

        self.cards = []
        self.sum = 0
        self.active = True

        self.cardX = 400
        self.cardY = cardY

        self.label = {}
        self.name = name
        self.makeLabel()



    def makeLabel(self):
        self.label = Text(Point(self.cardX + 400, self.cardY), "{0} {1}".format(self.sum, self.name))
        self.label.setSize(25)
        self.label.setFill("white")
        self.label.draw(self.win)

    def updateText(self):
        self.label.setText("{0} {1}".format(self.sum, self.name))

    def deactivate(self):
        #hide the cards in the hand
        #show a rectangle image with hand sum in the right bottom corner
        #add this card to a to the splitHands list in Dealer class
        pass
    def draw(self, card):
        #adds the specific card to the hand
        #update the sum
        self.cards.append(card)
        card.moveCard(self.cardX,self.cardY)
        self.cardX += 40
        card.show()
        if(card.open):
            self.sum += card.value
        self.updateText()

    def openCard():
        ##opens dealers card
        pass

    def flipAce(self): #True if ace was flipped. False if no available aces
        for card in self.cards:
            if card.isAce:
                if card.value == 11:
                    card.value = 1
                    self.sum -= 10
                    return True
        return False

    def checkStatus(self): #Return 0 if less then 21 significant. Return 1 if sum == 21. Return 2 if sum > 21 (bust)
        if(self.sum == 21):
            return 1
        elif(self.sum > 21):
            if self.flipAce():
                self.checkStatus()
            else:
                return 2
        return 0
