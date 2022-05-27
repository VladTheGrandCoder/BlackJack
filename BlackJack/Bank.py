from Chip import Chip
from graphics import *
class Bank:
    def __init__(self, win, cash):
        self.win = win
        self.cash = cash #all of the money subtract bet
        self.bet = 0 #total value in the stack
        self.top = 0 #this variable represents the index of top chip (from 0 to 9)


        self.stack = [] #array of the chip chip objects in the center
        self.chips = [] #array of all chips in the "bank" area
        self.box = 0 ## will represent the bank outline after the bank is created

        self.chipVals = [1, 5, 25, 50, 100, 500, 1000, 2000, 5000, 10000] #all the possible chips values 



    def showBank():
        #shows the chips and calls readChip method



        print()

    def hideBank():
        #hides everything except for the stack and the bet amount
        #called when the readChip loop breaks


        print()



    def makeBank(self):#

        def makeChip(self, value, point):#create chip object and hide it
            chip = Chip(self.win, point, 60, value)
            chip.hide()
            return chip


        #draw the box for the chips and hide it
        p1 = Point(730, 710)
        p2 = Point(10, 435)
        self.box = Rectangle(p1,p2)
        self.box.setWidth(2)
        self.box.setOutline("darkblue")

        ## Fill the center stack with invisible chips of every possible value
        center = Point(500, 360) 
            ###Show bet value to the right of the stack at all times
        for i in range(0,10,1):
            value = self.chipVals[i]
            chip = makeChip(self, value, center)
            chip.bet = True #used in readChip (readBank) for differentiating the kind of chip clicked
            self.stack.append(self.chipVals[i])

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
            chip = makeChip(self, value, center)
            self.chips.append(chip)
            i +=1

    

    def fillBank(self):
        #clear bank first
        #fill bank with the highest possible chips 
        #stack max 3 chips on top (if self.cash if equal to 3 or more of those chips) # dump this idea, too complex
        #Start with the largest chip, check if it matches cash
        #if yes, add the number chips equivalent to total cash to the bank (no more then 3) 
        #repeat with lower chips. After first 3 chip, fill the rest with 3chips automatically #no 3 chips. All one

        for i in range(len(chips)-1): #clears the bank
            self.chips[i].hide()
            #del self.chips[i] # I dont think I need to delete it if I can just hide it. This should save some memory 

        

        #bank filling loop 
        #Check for the highest chip value that matches cash
        #show that and all of the below chips

    def readChip(self, deal):
        #determines which chip was clicked
        #keep reading until the user decides to deal card (or quit, pass true if showing endscreen) 
        while(not deal):
            p = self.win.getMouse()

            for chip in chips: ###REVIEW AND IF NEEDED OVERWRITE
                if(chip.clicked(p) and chip.visible): #chech if the clicked chip is approprite to interact with
                    v = chip.value
                    #chech if chip is in the center, act correspondingly
                    if(chip.bet): #remove
                        self.cash += v
                        self.bet -= v
                        del self.stack[-1]
                        #removing animation
                        fillBank()

                    else: #add
                        self.cash -= v
                        self.bet += v
                        self.stack.append(chip.value)
                        #adding animation
                        fillBank()

    def addChip(): #i'll probably get rid of add and remove methods, because readChip performs their function
                    # maybe change these into 'animation methods' 
                    #PROBABLY DELETE COMPLETELY AND MAKE ANIMATION METHODS FOR THE CHIP CLASS INSTEAD

        #animation + update view + update bank
        #check whether clicked chip is visible
        #subtract chip value from self.cash and add it to the bet
        #add chip value to the end of the stack
        #run chip stack animation 
        #fill bank considering the updated self.cash value


        print()
    def removeChip():#PROBABLY DELETE COMPLETELY AND MAKE ANIMATION METHOD FOR THE CHIP CLASS INSTEAD

        #animation + update view + update bank
        #check if the stack has chips 
        #if has, take the top chip and run "chip remove" animation updating the stack's picture to the next highest chip
        #remove chip value from bet and add it to cash
        #remove the last chip from self.stack (del self.stack[-1])
        #fill the bank considering the updated self.cash value
        print()
    



