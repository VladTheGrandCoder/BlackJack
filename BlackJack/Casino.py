class Casino():
#Controller class responsible for the interactions between the dealer and the bank
    def __init__(self, bank, dealer):
            self.bank = bank
            self.dealer = dealer
            self.quit = 0

            self.endText = 0 #Will pop up when the game is over and inform the user on what happened

    def play(self):
            while(self.bank.readBank() == 0):
                self.dealer.initialDraw()
                self.dealer.showDeal()
            
                status = self.dealer.readAction()

                if(status == 1):
                    #Bust. Subtract bet from cash
                    self.bank.cash -= self.bank.bet
                    self.dealer.hideDeal()
                    #wait and show self.endText
                    self.bank.showBank()

                elif(status == 2):
                    #Push. Dont change cash
                    self.dealer.hideDeal()
                    #wait and show self.endText
                    self.bank.showBank()

                elif(status == 3):
                    #Win. Add bet to the cash
                    self.bank.cash += self.bank.bet
                    self.dealer.hideDeal()
                    #wait and show self.endText
                    self.bank.showBank()

                elif(status == 4):
                    #BJ. Add bet *1.5 to the cash
                    self.bank.cash += (self.bank.bet * 1.5)
                    self.dealer.hideDeal()
                    #wait and show self.endText
                    self.bank.showBank()
                #Initial draw 