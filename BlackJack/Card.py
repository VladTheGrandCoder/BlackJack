from graphics import *
class Card():
    def __init__(self, index, image, value, win):
        self.index = index #index from 1 to 52 ###I dont know if I actually need it 
        self.value = value #value in the game of BlackJack
        self.win = win

        self.front = Image(Point(0,0),image)    #front image
        self.back = 0                           #make it equal to the back image
        self.open = True                       #whether the front is open 
        self.isAce = False

    def moveCard(self, x, y):
        self.front.move(x,y)

    def show(self):
        self.front.draw(self.win)



