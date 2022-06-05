from Card import Card
from graphics import *
from Bank import Bank
import random
from Hand import Hand
from Button import Button
class Dealer():
    def __init__(self, win, userCash):
        self.win = win

        self.deck = [] #array of all possible card objects
        self.shoe = [0] *432 #8 sets of numbers from 0 to 51 representing a card indexes in the deck
                        #(every number is an index of a specific card in self.deck)

        self.NumDrawn = 0 #reshuffle when this reaches 180

        self.userHand = Hand(self.win, 550, "Player")
        self.dealerHand = Hand(self.win, 170, "Dealer")

        self.splitHands = [] #list of split hands that are not being played at the moment

        self.standButton = Button(win,Point(710,360),60,"Stand","lightgreen")
        self.hitButton = Button(win, Point(300,360),60,"Hit","lightgreen")



        self.fillDeck()
        self.shuffle()



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

    def __makeIndex__(self, takenIndexes):
        index = random.randint(0,431)
        if not (index in takenIndexes):
                    takenIndexes.append(index)
                    return index
        else:
            return self.__makeIndex__(takenIndexes) #used to avoid index doubling when shuffling

    def shuffle(self):
        takenIndexes = []

        for i in range(8):
            for j in range(0,52,1):
                
                    index = self.__makeIndex__(takenIndexes)
                    takenIndexes.append(index)
                    self.shoe[index] = j

        pass #fills the shoe with random indexes of 8 decks

    def showDeal(self):
        #called when the user hits the deal button
        #shows all the buttons that are available in the deal mode
        #check if numDrawn is greater then 180. If yes, shuffle and set numdrawn to 0
        self.standButton.show()
        self.hitButton.show()

        self.userHand.show()
        self.dealerHand.show()
        pass

    def hideDeal():
        #called when someone busts, wins, or there is a draw
        #hides all the dealer buttons

        pass

    def __drawCard__(self):
        self.NumDrawn += 1
        card = self.deck[self.shoe[-1-self.NumDrawn]].clone()
        return card

    def initialDraw(self):
        card1 = self.__drawCard__()
        self.userHand.draw(card1)
        
        card2 = self.__drawCard__()
        card2.open = False
        self.dealerHand.draw(card2) #hidden card

        card3 = self.__drawCard__()
        self.userHand.draw(card3)

        card4 = self.__drawCard__()
        self.dealerHand.draw(card4)

    def readAction(self):        #reads buttons and check hand values
        while(True):

            if(self.userHand.checkStatus() == 1):
                print("blackJack")
                self.dealerHand.openCard()
                break
            elif(self.userHand.checkStatus() == 2):
                print("bust")
                self.dealerHand.openCard()
                break

            p = self.win.getMouse()

            if(self.hitButton.clicked(p)):
                card = self.__drawCard__()
                self.userHand.draw(card)
            elif(self.standButton.clicked(p)):
                self.dealerHand.openCard()
                break

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