from graphics import *
from Button import Button
from Chip import Chip
from Bank import Bank
from Dealer import Dealer
from Casino import Casino

def end(win):
    win.getMouse()
    win.close()

def main():
    #change
    win = GraphWin("BlackJack", 1000, 720)
    win.setBackground("green")
    
    bank = Bank(win, 10020)
    dealer = Dealer(win, 1020)
    casino = Casino(bank, dealer)
    casino.play()

    end(win)
main()

