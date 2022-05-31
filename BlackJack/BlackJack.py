from graphics import *
from Button import Button
from Chip import Chip
from Bank import Bank
from Dealer import Dealer

def end(win):
    win.getMouse()
    win.close()

def main():
    #change
    win = GraphWin("BlackJack", 1000, 720)
    win.setBackground("green")
    
    #bank = Bank(win, 1020, "dealer")
    dearler = Dealer(win, 1020)

    

    end(win)
main()

