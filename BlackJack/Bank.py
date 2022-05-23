class Bank:
    def __init__(self, cash):
        self.cash = cash
        self.bet = 0
        self.stack = {}
        self.chipVals = [1, 5, 25, 50, 100, 500, 1000, 2000, 5000, 10000]

    def addChip(self, value, point):
        #create chip object and add it to self.chips
        print()


    def fillBank(self):
        #clear bank first
        #fill bank with the highest possible chips 
        #stack max 3 chips on top (if self.cash if equal to 3 or more of those chips) 
        #Start with the largest chip, check if it matches cash
        #if yes, add the number chips equivalent to total cash to the bank (no more then 3) 
        #repeat with lower chips. After first 3 chip, fill the rest with 3chips automatically
        print()

    def addChip():
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
    



