from graphics import *
from Abstract import Abstract
import time
class Hand():
    def __init__(self, win, cardY, name):
        self.win = win

        self.cards = [] #Arrays of card objects the hand contains
        self.sum = 0    #Total sum of all of the card values in the hand
        self.active = True #Whether the hand is being played right now, or has been set aside due to split

        self.cardX = 400        #Coordinates of the cards in the hand
        self.cardY = cardY

        self.label = {}         #The next 3 lines generate the label or "player name" and the hand's score
        self.name = name
        self.makeLabel()

        self.abstract = 0      #The rectangle with a number in the bottom right corner. Used to keep track of splits

    def makeLabel(self):        #Creates a lable Text object which shows Hand.name and Hand.sum
        self.label = Text(Point(self.cardX + 400, self.cardY), "{0} {1}".format(self.sum, self.name))
        self.label.setSize(25)
        self.label.setFill("white")

    def updateText(self):       #Updates the sum value when a card is added/removed from the hand
        self.label.setText("{0} {1}".format(self.sum, self.name))

    def show(self):     #Shows all of the hand's visuals.
        self.label.draw(self.win)
        for card in self.cards:
            try:
                card.show()
            except:
                pass
        pass

    def deactivate(self):
        #Hide the cards in the hand. Show a self.abstract
        #add the Hand to a to the Dealer.splitHands
        self.label.undraw()
        for card in self.cards:
            card.hide()
        self.abstract.show()
        
    def activate(self):
        #Hide the self.abstract and show the cards with the label
        #Remove the hand from Dealer.splitHands
        self.abstract.hide()
        self.show()
        
    def makeAbstract(self, x): #initializes self.abstract
        self.abstract = Abstract(self.win, x, self.sum)

    def draw(self, card):
        #add the specific card to the hand
        #update the sum
        self.cards.append(card)
        card.moveCard(self.cardX,self.cardY)
        self.cardX += 40
        card.show()
        if(card.open):
            self.sum += card.value
            self.checkStatus()
        self.updateText()

    def openCard(self): #opens hidden card. Only called once
        card = self.cards[0]
        card.open = True
        self.sum += card.value
        card.show()
        self.checkStatus()
                
        for card in self.cards: #this loop stacks card on top of each other so they overlap properly
            card.hide()
            card.show()

        self.updateText()

    def __flipAce__(self): #True if ace was flipped. False if no available aces
        for card in self.cards:
             if card.value == 11:
                 card.value = 1
                 self.sum -= 10
                 return True
        return False

    def checkStatus(self): #Responsible for ace controll. I need to fix the return statements
        if(self.sum == 21):
            return 1
        elif(self.sum > 21):
            if self.__flipAce__():
                self.checkStatus()
            else:
                return 2
        return 0

    def hideVisuals(self):
        for card in self.cards:
            card.hide()
        self.label.undraw()
        try:
            self.abstract.hide()
        except:
            pass

