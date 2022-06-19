from graphics import *
from Button import Button
from Chip import Chip
from Bank import Bank
from Dealer import Dealer
from Casino import Casino

def main():
    win = GraphWin("BlackJack", 1000, 720)
    win.setBackground("green")
    
    bank = Bank(win, 1000)
    dealer = Dealer(win, 1020)
    casino = Casino(win, bank, dealer)
    casino.play()

    win.close()

main()