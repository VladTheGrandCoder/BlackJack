from Chip import Chip
from graphics import *
from Button import Button
class Bank:
    def __init__(self, win, cash):
        self.win = win

        self.cash = cash #all of the money subtract bet
        self.bet = 0 #total value in the stack
        self.top = cash #the maximum amount of money the user posessed through the game

        self.stack = [] #array of the chip chip objects in the center
        self.stackTracker = [] #tracks the indexes of stack (bottom to top)
        self.chips = [] #array of all chips in the "bank" area
        self.chipVals = [1, 5, 25, 50, 100, 500, 1000, 2000, 5000, 10000] #all the possible chips values 


        self.box = 0 ###PROBABLY DELETE # will represent the bank outline after the bank is created 
        self.betText = 0 #the bet value to the right of the stack
        self.cashText = 0 #the remaining cash on top of the box
        self.deal = 0 #deal button

        self.makeBank()

    def showBank(self):#called after the deal is over
        #shows the chips and the buttons + the box
        self.cashText.draw(self.win)
        self.deal.show()
        self.cashOut.show()
        self.box.draw(self.win)
        #update the top after the deal is over
        self.updateTop()
        #fills the bank
        self.fillBank()

    def hideBank(self):#called before the deal
        #hides everything except for the stack and the bet amount
        #called when the readBank loop breaks

        #hide the betting chips
        for chip in self.chips:
            chip.hide()

        #hide box, cash and the buttons
        self.box.undraw()
        self.cashText.undraw()
        self.deal.hide()
        self.cashOut.hide()
        #active the Dealer class and call DealCards() method
 
    def makeChip(self, value, point):#create chip object and hide it
            chip = Chip(self.win, point, 60, value)
            chip.hide()
            return chip

    def makeBank(self):
        ##Add cashOut button
        self.cashOut = Button(self.win,Point(80,70),45,"Cash Out","lightgreen")
        self.cashOut.body.setWidth(1)
        self.cashOut.label.setSize(15)
        self.cashOut.show()
        ##Add deal button
        self.deal = Button(self.win,Point(890, 610),60,"Deal","lightgreen")
        self.deal.body.setWidth(2)
        self.deal.label.setSize(27)
        self.deal.show()
        ##Show bet value beside the stack
        self.betText = Text(Point(580, 360),"${0}".format(self.bet))
        self.betText.setTextColor("white")
        self.betText.setSize(30)
        self.betText.draw(self.win)
        ##Add cash value
        self.cashText = Text(Point(112, 415),"Cash: ${0:6<}".format(self.cash))
        self.cashText.setTextColor("white")
        self.cashText.setSize(25)
        self.cashText.draw(self.win)
        #draw the box for the chips and hide it
        p1 = Point(730, 710)
        p2 = Point(10, 435)
        self.box = Rectangle(p1,p2)
        self.box.setWidth(3)
        self.box.setOutline(color_rgb(54, 61, 53))
        self.box.setFill(color_rgb(94, 115, 92))
        self.box.draw(self.win)
        ## Fill the center stack with invisible chips of every possible value
        center = Point(450, 360) 
            ###Show bet value to the right of the stack at all times
        for i in range(0,10,1):
            value = self.chipVals[i]
            chip = self.makeChip(value, center)
            chip.bet = True #used in readBank for differentiating the kind of chip clicked
            self.stack.append(chip)

        #Fill the bank with chip of every possible value and hide them
        i = 1
        while(i < 11):
            x = 0
            y = 0
            if(i<6):
                x =  (i * 140) - 50
                y = 440 + 66
            else:
                j = i - 5
                x =  (j * 140 ) - 50
                y = 440 + (66 *3)

            center = Point(x,y)
            value = self.chipVals[i-1]
            chip = self.makeChip(value, center)
            self.chips.append(chip)
            i +=1

            self.fillBank()

    def fillBank(self):#fill bank with the highest possible chips 
        #update money values
        self.cashText.setText("Cash: ${0:6<}".format(self.cash))
        self.betText.setText("${0}".format(self.bet))

        #hide all chips
        for chip in self.chips: 
           chip.hide()

        #goes through every chip. If chip value is within cash, make chip visible
        for chip in self.chips:
            if(chip.value <= self.cash):
                chip.show()

    def updateTop(self):
        curVal = self.cash + self.bet
        if (curVal > self.top):
            self.top = curVal
        pass

    def readBank(self):
        #determines what was clicked
        #keep reading until the user decides to deal cards
        ###ADD a button that would allow to finish the game by withdrawling cash
        ###CHECK if the user has any money left. End game if no
        while(True):
            p = self.win.getMouse()

            #Check the deal button
            if(self.deal.clicked(p)):
                self.hideBank()
                return 0

            if(self.cashOut.clicked(p) or (self.cash + self.bet) < 1):
                #show withdrawl screen with highscore and amount withdrawn
                return 1

            #check every chip in the bank
            for i in range(0,10,1): 
                chip = self.chips[i]
                if(chip.clicked(p) and chip.visible): #chech if the clicked chip is approprite to interact with
                    v = chip.value
                    #add to the bet
                    self.cash -= v
                    self.bet += v
                    try:
                        self.stack[self.stackTracker[-1]].hide() #hide the old chip (if there is one)
                    except:
                        pass
                    self.stackTracker.append(i) #add the new chip index
                    self.stack[i].show() #show the new chip
                    #adding animation
                    self.fillBank()
                    break

            #check every chip in the stack
            for i in range(0,10,1):
                chip = self.stack[i]
                if(chip.clicked(p) and chip.visible):
                    v = chip.value
                    self.cash += v
                    self.bet -= v
                    self.stack[self.stackTracker[-1]].hide() #hide the top chip
                    try:                     
                        self.stack[self.stackTracker[-2]].show() #try showing the next top chip (if there is one)
                    except:
                        pass

                    del self.stackTracker[-1] #delete the old top chip index from the tracker
                    #removing animation
                    self.fillBank()
                    break
        pass