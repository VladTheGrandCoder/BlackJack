from graphics import *
import random
import time
from Bank import Bank
from Card import Card
from Hand import Hand
from Button import Button
class Dealer():
    def __init__(self, win, userCash):
        self.win = win

        self.deck = [] #array of all possible card objects
        self.shoe = [0] *432 #8 sets of numbers from 0 to 51 representing a card indexes in the deck
                        #(every number is an index of a specific card in self.deck)

        self.NumDrawn = 0 #reshuffle when this reaches 180

        self.playerHand = Hand(self.win, 550, "Player")
        self.dealerHand = Hand(self.win, 170, "Dealer")

        self.splitHands = [] #list of split hands that are not being played at the moment

        self.standButton = Button(win,Point(710,360),60,"Stand","lightgreen")
        self.hitButton = Button(win, Point(300,360),60,"Hit","lightgreen")
        self.doubleButton = 0
        self.splitButton = 0
        self.insuraceButton = 0

        self.abstractX = 700

        self.fillDeck()
        self.shuffle()



    def fillDeck(self):
        i = 1
        val = 2
        for suit in ["clubs", "diamonds", "hearts", "spades"]:
            val = 2
            for face in ['2','3','4','5','6','7','8','9','10','jack','queen','king','ace']:
                path = "Cards\{0}_of_{1}.png".format(face, suit)
                card = self.__makeCard__(i, path, val)
                if i%13 == 0:

                    card.isAce = True
                    card.value = 11
                    
                self.deck.append(card)

                i+=1
                if val < 10:
                   val +=1
        pass
        #fills self.deck with appropriate card objects

        
    def __makeCard__(self, index, image, value):
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
        #shows all the buttons that are available in the deal mode
        #check if numDrawn is greater then 180. If yes, shuffle and set numdrawn to 0
        self.standButton.show()
        self.hitButton.show()

        self.playerHand.show()
        self.dealerHand.show()
        #called when the user hits the deal button

    def hideDeal(self):
        #called when the deal if over
        #hides all the dealer buttons

        self.playerHand.label.undraw() #Hide the labels
        self.dealerHand.label.undraw()

        for card in self.playerHand.cards:
            card.hide()
            del card

        for card in self.dealerHand.cards:
            card.hide()
            del card

        for i in range(len(self.splitHands) - 1): #empty split hands list
            #make sure to properly undraw everything before deleting
            del self.splitHands[i]

        self.hitButton.hide() #Hide all the buttons
        self.standButton.hide()
        #self.doubleButton.hide()
        #self.splitButton.hide()
        #self.insuraceButton.hide()

    def __drawCard__(self):
        self.NumDrawn += 1
        card = self.deck[self.shoe[-1-self.NumDrawn]].clone()
        return card
        #Draws card from the deck. Returns the card drawn

    def initialDraw(self):


        card1 = self.__drawCard__()
        self.playerHand.draw(card1)
        
        card2 = self.__drawCard__()
        card2.open = False
        self.dealerHand.draw(card2) #hidden card

        card3 = self.__drawCard__()
        self.playerHand.draw(card3)

        card4 = self.__drawCard__()
        self.dealerHand.draw(card4)

    def readAction(self):        #reads buttons and check hand values
        while(True):
            p = self.win.getMouse()

            if(self.playerHand.sum == 21):#Check for BJ
                self.dealerHand.openCard()
                time.sleep(1.5)
                if(self.playerHand.sum == self.dealerHand.sum): #CheckFor Push
                    return 2
                else:
                    if(len(self.dealerHand.cards) == 2): #Check if it is a 2 card BJ
                        return 4
                    else: 
                        return 3 #if not a 2 card BJ, return regular win (victory, not window)

            elif(self.playerHand.sum > 21):#Check bust
                self.dealerHand.openCard() #Show dealer's card, wait and return bust 
                time.sleep(1.5)
                return 1

            if(self.hitButton.clicked(p)): #Check hit button
                card = self.__drawCard__()
                self.playerHand.draw(card)
                #Check status after a hit
                if(self.playerHand.sum > 21):#Check bust
                    self.dealerHand.openCard() #Show dealer's card, wait and return bust 
                    time.sleep(1.5)
                    return 1

            elif(self.standButton.clicked(p)): #Check stand button
                self.dealerHand.openCard()
                self.dealerDraw()

                d = self.dealerHand.sum
                p = self.playerHand.sum

                if(d > 21 or d < p): #Check for dealer bust and dealer loose
                    time.sleep(1.5)#maybe delete this and delay in Casino class
                    return 3
                elif(d == p):#Check for push
                    time.sleep(1.5)
                    return 2
                elif(d > p): #Check for player loose (dont check for bust, because that was done at the start)
                    time.sleep(1.5)
                    return 1
                print("Oops! reacAction standButton command is broken!")
                break
        pass

    def dealerDraw(self):
        while(True):
            if(self.dealerHand.sum < 17):
                card = self.__drawCard__()
                self.dealerHand.draw(card)
                time.sleep(1.5)
            else:
                break
        pass
        #keep drawing cards until self.dealerHand.sum >= 17

    def hit():
        pass

    def stand(self):

        for i in range(len(self.splitHands)): #Checks for unplayed hands in the split
            hand = self.splitHands[i]
            if (not hand.abstract.played): #If the Hand has not been played, play if
                self.playerHand.makeAbstract(self.abstractX)
                self.playerHand.abstract.show()
                self.splitHands[i] = self.playerHand

                self.playerHand = hand
                self.playerHand.show()
                #self.readAction() Idk what is the best way to get back to reading the action and break from here at the same time
                #Got to figure it out next time


    def doubleUp():
        pass

    def split(self):
        #make a new hand. Add one of the playerHand cards to the hand. Delete that card from playerHand.
        #add the new hand to the self.splitHands
        card = self.playerHand.cards[1].clone()

        splitHands.append(Hand(self.win))

        del self.playerHand.cards[1]


    def insurace():
        pass
    