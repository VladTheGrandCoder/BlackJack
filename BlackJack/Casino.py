from graphics import *
import time
from Button import Button
class Casino():
#Controller class responsible for the interactions between the dealer and the bank
    def __init__(self, win, bank, dealer):
            self.win = win
            self.bank = bank
            self.dealer = dealer
            self.quit = 0

            self.endText = Text(Point(500,360), "Bla Bla Bla") #Will pop up when the game is over and inform the user on what happened
            self.endText.setSize(36)
            self.endText.setTextColor("white")
            self.endRect = Rectangle(Point(0,0), Point(1000,720))
            self.endRect.setFill("green")
            self.endRect.setOutline("green")

    def endScreen(self,text):
        self.endText.setText(text)
        self.endRect.draw(self.win)
        self.endText.draw(self.win)
        time.sleep(1.5)
        self.endRect.undraw()
        self.endText.undraw()

    def cashOutScreen(self):
        rect = Rectangle(Point(200, 100), Point(800, 620))
        rect.setFill("lightblue")
        rect.setOutline("lightblue")

        message = ""
        whoWon = ""

        if self.bank.cash + self.bank.bet >= 1000:
            message = "Cash won: ${0}".format(abs(1000 - (self.bank.cash + self.bank.bet)))
            whoWon = "Player Wins!"
        else:
            message = "Cash lost: ${0}".format(1000 - (self.bank.cash + self.bank.bet))
            whoWon = "House Wins!"

        textWhoWon = Text(Point(500,200), whoWon)
        textWhoWon.setSize(27)
        textCashWon = Text(Point(500,300), message)
        textCashWon.setSize(20)
        textHighestBank = Text(Point(500, 400), "Highest Bank: ${0}".format(self.bank.top))
        textHighestBank.setSize(20)

        close = Button(self.win, Point(500,540),40, "Close", color_rgb(3, 152, 252))
        close.label.setSize(18)


        rect.draw(self.win)
        textWhoWon.draw(self.win)
        textCashWon.draw(self.win)
        textHighestBank.draw(self.win)
        close.show()

        while(True):
            p = self.win.getMouse()
            if close.clicked(p):
                break

    def play(self):
            while(self.bank.readBank() == 0):
                self.dealer.showDeal()
                self.dealer.initialDraw()
            
                status = self.dealer.readAction() #Nothing 0. Bust/loose 1. Push 2. Win 3. BJ 4.

                if(status == 1):
                    #Bust. Subtract bet from cash
                    if(self.bank.cash - self.bank.bet >= 0): #Make sure cash does not go negative
                        self.bank.cash -= self.bank.bet
                    else:#if cash goes negative, dont touch it, but remove the bet
                        self.bank.bet = 0
                        for chip in self.bank.stack:
                            chip.hide()
                        del self.bank.stackTracker[:] 

                    self.dealer.hideDeal()
                    #wait and show self.endText
                    self.endScreen("Dealer Wins")
                    self.bank.showBank()

                elif(status == 2):
                    #Push. Dont change cash
                    self.dealer.hideDeal()
                    #wait and show self.endText
                    self.endScreen("Push")
                    self.bank.showBank()

                elif(status == 3):
                    #Win. Add bet to the cash
                    self.bank.cash += self.bank.bet
                    self.dealer.hideDeal()
                    #wait and show self.endText
                    self.endScreen("Player Wins")

                    self.bank.showBank()

                elif(status == 4):
                    #BJ. Add bet *1.5 to the cash
                    self.bank.cash += (self.bank.bet * 1.5)
                    self.dealer.hideDeal()
                    #wait and show self.endText
                    self.endScreen("BlackJack!")

                    self.bank.showBank()

            self.cashOutScreen()