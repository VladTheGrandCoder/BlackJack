from graphics import *
import random
import time
from Bank import Bank
from Card import Card
from Hand import Hand
from Button import Button
class Dealer():
    def __init__(self, win, bank):
        self.win = win
        self.bank = bank

        self.deck = [] #array of all possible card objects
        self.shoe = [0] *432 #8 sets of numbers from 0 to 51 representing a card indexes in the deck
                        #(every number is an index of a specific card in self.deck)
        self.shoeText = Text(Point(910,70), "{0}❏".format(len(self.shoe)))
        self.shoeText.setFill("white")
        self.shoeText.setSize(19)

        self.NumDrawn = 0 #reshuffle when this reaches self.marker (Reshuffles in self.showDeal)
        self.marker = random.randint(172,260) #random number between 40% and 60% of 432

        self.playerHand = Hand(self.win, 550, "Player")
        self.dealerHand = Hand(self.win, 170, "Dealer")

        self.splitHands = [] #list of split hands that are not being played at the moment

        self.standButton = Button(win,Point(710,360),60,"Stand","lightgreen")

        self.hitButton = Button(win, Point(300,360),60,"Hit","lightgreen")

        self.doubleButton = Button(win, Point(170, 360), 55,"X2", "lightgreen")
        self.doubleButton.label.setSize(27)

        self.splitButton = Button(win, Point(840, 360), 55, "Split", "lightgreen")
        self.splitButton.label.setSize(27)

        self.insuraceButton = Button(win, Point(80, 70), 45, "Insurance", "lightgreen")
        self.insuraceButton.label.setSize(15)
        self.insuraceButton.body.setWidth(1)

        self.insuranceText = Text(Point(150, 160), "")
        self.insuranceText.setTextColor("white")
        self.insuranceText.setSize(21)

        self.cashText = Text(Point(112, 690),"Cash: ${0:6<}".format(self.bank.cash))
        self.cashText.setTextColor("white")
        self.cashText.setSize(25)

        self.abstractX = 700 #Trash it

        self.fillDeck()
        self.shuffle()

    def updateCashText(self): 
        self.cashText.setText("Cash: ${0:6<}".format(self.bank.cash))
    def updateCashTest(self, newCash):#wanted this to be an overload, but gave it a different name. Keep it like that, works just fine
        self.cashText.setText("Cash: ${0:6<}".format(newCash))

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
        #fills the shoe with random indexes of 8 decks

    def updateShoeText(self):
        cardsLeft = len(self.shoe) - self.NumDrawn
        self.shoeText.setText("{0}❏".format(cardsLeft))

    def showDeal(self):
        #shows all the buttons that are available in the deal mode
        #check if reached the marker. If yes, shuffle and set numdrawn to 0
        if(432 - self.NumDrawn < self.marker):
            self.shuffle()
            self.NumDrawn = 0
            self.marker = random.randint(172,260)
            self.updateShoeText()

        self.standButton.show()
        self.hitButton.show()
        #self.doubleButton.show() #Delete later
        #self.splitButton.show() #Delete later
        #self.insuraceButton.show() #Delete later

        self.updateCashText()
        self.shoeText.draw(self.win)
        self.cashText.draw(self.win)

        self.playerHand.show()
        self.dealerHand.show()
        #called when the user hits the deal button

    def hideDeal(self):
        #called when the deal if over
        #hides all the dealer buttons

        self.playerHand.label.undraw() #Hide the labels
        self.dealerHand.label.undraw()
        self.shoeText.undraw()
        self.cashText.undraw()

        self.playerHand.hideVisuals() #Hide and emptry player's cards
        del self.playerHand.cards[:]

        self.dealerHand.hideVisuals() #Hide and empty dealer's cards
        del self.dealerHand.cards[:]

        for hand in self.splitHands: #Get rid of all the splits
            hand.hideVisuals()
        del self.splitHands[:]



        self.hitButton.hide() #Hide all the buttons
        self.standButton.hide()
        self.doubleButton.hide()
        self.splitButton.hide()
        self.insuraceButton.hide()

    def __drawCard__(self):
        self.NumDrawn += 1
        card = self.deck[self.shoe[-1-self.NumDrawn]].clone()
        self.updateShoeText()
        return card
        #Draws card from the deck. Returns the card drawn

    def initialDraw(self):
        #Make sure that the sums are zero and that the cards are properly lined up 
        self.playerHand.sum = 0
        self.playerHand.cardX = 400
        self.dealerHand.sum = 0
        self.dealerHand.cardX = 400
        #Start drawing cards
        card1 = self.__drawCard__()
        self.playerHand.draw(card1)
        
        card2 = self.__drawCard__()
        card2.open = False
        self.dealerHand.draw(card2) #hidden card

        card3 = self.__drawCard__()
        self.playerHand.draw(card3)

        card4 = self.__drawCard__()
        self.dealerHand.draw(card4)

    def readAction(self, hasMoneyForDouble):        #reads buttons and check hand values
        while(True):
            if(self.playerHand.sum == 21):#Check for BJ
                self.dealerHand.openCard()
                time.sleep(1.5)
                if(self.playerHand.sum == self.dealerHand.sum): #Check for Push
                    return 2
                else:
                    if(len(self.playerHand.cards) == 2): #Check if it is a 2 card BJ
                        return 4
                    else: 
                        self.dealerDraw()
                        if(self.dealerHand.sum == 21): #Check for Push
                            return 2
                        else:
                            return 3 #if not a 2 card BJ, return regular win (victory, not window)

            elif(self.playerHand.sum > 21):#Check bust
                self.dealerHand.openCard() #Show dealer's card, wait and return bust 
                time.sleep(1.5)
                return 1

            ###Check if can show the optional buttons
            if(len(self.playerHand.cards) == 2 ): #Check for split option
                if(self.playerHand.cards[0].value == self.playerHand.cards[1].value):
                    self.splitButton.show()
            if(hasMoneyForDouble and len(self.playerHand.cards) == 2): #Check for double option
                self.doubleButton.show()
            if(self.dealerHand.cards[1].value == 11 and hasMoneyForDouble and len(self.playerHand.cards) == 2):  #Check for insurance option
                self.insuraceButton.show()

            p = self.win.getMouse() #Read input

            if(self.hitButton.clicked(p)): #Check hit button
                card = self.__drawCard__() #Draw a card and hide x2 button and insurance button
                self.playerHand.draw(card)

                self.doubleButton.hide()
                self.insuraceButton.hide()
                self.splitButton.hide()
            elif(self.standButton.clicked(p)): #Check stand button
                self.doubleButton.hide()
                self.insuraceButton.hide()
                self.splitButton.hide()

                self.dealerHand.openCard()
                time.sleep(1.5)
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
                break
            
            elif(self.doubleButton.clicked(p)): #Check the Double button
                self.doubleButton.hide()
                self.insuraceButton.hide()
                self.splitButton.hide()

                self.updateCashTest(self.bank.cash - self.bank.bet) #Update cash considering the new Bet

                self.bank.updateBet(self.bank.bet * 2)
                

                card = self.__drawCard__() #Draw one card  
                self.playerHand.draw(card)

                if(self.playerHand.sum > 21): #Check for bust after drawing card
                    time.sleep(1.5)
                    self.dealerHand.openCard()
                    time.sleep(1.5)
                    return 21

                time.sleep(1.5)
                self.dealerHand.openCard() #Draw the dealer's cards
                time.sleep(1.5)
                self.dealerDraw()
                #Check the outcome
                d = self.dealerHand.sum
                p = self.playerHand.sum

                if(d > p and d < 22 or p > 21): #Check for player loose
                    time.sleep(1.5)
                    return 21
                elif(d == p):#Check for push
                    time.sleep(1.5)
                    return 2
                elif(d > 21 or d < p): #Check for dealer bust and dealer loose
                    time.sleep(1.5)
                    return 23
                pass

            elif(self.insuraceButton.clicked(p)): #Check insurance button
                #side bet equal to the original
                #check for BlackJack in the dealer
                #if BJ pay the insarance to the user, compare cards and return
                #else Subtract the insurance from cash
                self.insuraceButton.hide()
                sideBet = self.bank.bet
                sum = 0
                for card in self.dealerHand.cards:
                    sum += card.value
                if(sum == 21): 
                    self.dealerHand.openCard()
                    self.bank.cash += sideBet
                    self.insuranceText.setText("Insurance Triggered!")
                    self.insuranceText.draw(self.win)
                    time.sleep(1.5)
                    self.insuranceText.undraw()
                    return 1    #Return loose, because if the user had 21, it would have triggered above
                else:
                    self.bank.cash -= sideBet
                    self.updateCashText()
                    self.insuranceText.setText("Insurance Lost!")
                    self.insuranceText.draw(self.win)
                    time.sleep(1.5)
                    self.insuranceText.undraw()
                pass

            elif(self.splitButton.clicked(p)):
                pass

    def dealerDraw(self):
        while(True):
            if(self.dealerHand.sum < 17):
                card = self.__drawCard__()
                self.dealerHand.draw(card)
                self.dealerHand.checkStatus()
                time.sleep(1.5)
            else:
                break
        pass
        #keep drawing cards until self.dealerHand.sum >= 17

    def stand(self):
        ##Trash it
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

    def split(self):
        ##Probabl Trash It
        #make a new hand. Add one of the playerHand cards to the hand. Delete that card from playerHand.
        #add the new hand to the self.splitHands
        card = self.playerHand.cards[1].clone()

        splitHands.append(Hand(self.win))

        del self.playerHand.cards[1] 