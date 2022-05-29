from graphics import *
from Button import Button
from Chip import Chip
from Bank import Bank

def end(win):
    win.getMouse()
    win.close()

def main():
    #change
    win = GraphWin("BlackJack", 1000, 720)
    win.setBackground("green")
    
    bank = Bank(win, 1020)
    bank.makeBank()
    bank.readBank()
    end(win)
main()

