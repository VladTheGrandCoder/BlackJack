from Chip import Chip
class Bank:
    def __init__(self, win, cash):
        self.win = win
        self.cash = cash
        self.bet = 0

        self.stack = [] #array of the chip values in the stack


        self.chips = [] #array of all chips on the screen (maybe change to just the chips 'in the bank') 


        self.chipVals = [1, 5, 25, 50, 100, 500, 1000, 2000, 5000, 10000]

    def makeChip(self, value, point):
        #create chip object and add it to self.chips

        chip = Chip(self.win, point, 60, value)
        chip.show()
        self.chips.append(chip)

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

            for chip in chips:
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

        #animation + update view + update bank
        #check whether clicked chip is visible
        #subtract chip value from self.cash and add it to the bet
        #add chip value to the end of the stack
        #run chip stack animation 
        #fill bank considering the updated self.cash value


        print()
    def removeChip():
        #animation + update view + update bank
        #check if the stack has chips 
        #if has, take the top chip and run "chip remove" animation updating the stack's picture to the next highest chip
        #remove chip value from bet and add it to cash
        #remove the last chip from self.stack (del self.stack[-1])
        #fill the bank considering the updated self.cash value
        print()
    



