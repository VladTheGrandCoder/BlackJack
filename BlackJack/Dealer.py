from Card import Card
from graphics import *
from Bank import Bank
import random
from Hand import Hand
class Dealer():
    def __init__(self, win, userCash):
        self.win = win
        self.bank = Bank(win, userCash)

        self.deck = [] #array of all possible card objects
        self.shoe = [0] *432 #sets decks of numbers from 0 to 52 representing a card 
                        #(every number is an index of a specific card in self.deck)
        self.NumDrawn = 0

        self.userHand = Hand(self.win, 550)
        self.dealerHand = Hand(self.win, 170)

        self.splitHands = [] #list of split hands that are not being played at the moment

        self.bank.hideBank()
        self.fillDeck()
        self.shuffle()
        self.initialDraw()

        #self.bank.readBank()
    def fillDeck(self):#fills self.deck with appropriate card objects
        i = 1
        val = 2
        for suit in ["clubs", "diamonds", "hearts", "spades"]:
            val = 2
            for face in ['2','3','4','5','6','7','8','9','10','jack','queen','king','ace']:
                path = "Cards\{0}_of_{1}.png".format(face, suit)
                card = self.makeCard(i, path, val)
                if i%13 == 0:

                    card.isAce = True
                    card.value = 11
                    
                self.deck.append(card)

                i+=1
                if val < 10:
                   val +=1
        pass

    def makeCard(self, index, image, value):
        card = Card(index, image, value, self.win)
        return card#creates a card object

    def makeIndex(self, takenIndexes):
        index = random.randint(0,431)
        if not (index in takenIndexes):
                    takenIndexes.append(index)
                    return index
        else:
            return self.makeIndex(takenIndexes) #used to avoid index doubling when shuffling

    def shuffle(self):
        takenIndexes = []

        for i in range(8):
            for j in range(0,54,1):
                
                    index = self.makeIndex(takenIndexes)
                    takenIndexes.append(index)
                    self.shoe[index] = j

        pass #fills the shoe with random indexes of 8 decks

    def showDeal():
        #called when the user hits the deal button
        #shows all the buttons that are available in the deal mode
        #check if numDrawn is greater then 180. If yes, shuffle and set numdrawn to 0
        pass

    def hideDeal():
        #called when someone busts, wins, or there is a draw
        #hides all the dealer buttons

        pass

    def initialDraw(self):
        card1 = self.deck[self.shoe[-1-self.NumDrawn]]
        self.NumDrawn += 1
        self.userHand.draw(card1)
        
        card2 = self.deck[self.shoe[-1-self.NumDrawn]]
        card2.open = False
        self.NumDrawn += 1
        self.dealerHand.draw(card2) #hidden card

        card3 = self.deck[self.shoe[-1-self.NumDrawn]]
        self.NumDrawn += 1
        self.userHand.draw(card3)

        card4 = self.deck[self.shoe[-1-self.NumDrawn]]
        card4.open = False
        self.NumDrawn += 1
        self.dealerHand.draw(card4) #hidden card

    def play(self):
        self.initialDraw()

        self.readAction()

    def readAction(self):
        #reads buttons
        pass
    
    def drawCard(self):
        
        pass

    def hit():
        pass

    def stand():
        pass

    def doubleUp():
        pass

    def split():
        pass

    def insurace():
        pass
    
    def nextHand():
        pass