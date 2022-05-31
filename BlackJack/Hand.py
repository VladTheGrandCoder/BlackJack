class Hand():
    def __init__(self, win, cardY):
        self.cards = []
        self.sum = 0
        self.active = True

        self.cardX = 400
        self.cardY = cardY


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

        pass

    def checkBust(self):
        #if over 21, check for aces 
        #if aces present, change them to 1
        #if no aces, bust, hideDealer, showBank
        pass
