class Casino():
#Controller class responsible for the interactions between the dealer and the bank
    def __init__(self, bank, dealer):
            self.bank = bank
            self.dealer = dealer


    def play(self):
        self.bank.readBank()

        self.dealer.initialDraw()
        self.dealer.showDeal()
        self.dealer.readAction()