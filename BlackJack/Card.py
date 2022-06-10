from graphics import *
class Card():
    def __init__(self, index, image, value, win):
        self.index = index #index from 1 to 52 ###I dont know if I actually need it 
        self.image = image #used for cloning
        self.value = value #value in the game of BlackJack
        self.win = win

        self.front = Image(Point(0,0),image)    #front image
        self.back = Image(Point(0,0), "Cards\card_back.png")  #back image
        self.open = True                       #whether the front is open 
        self.isAce = False                      ##Mybe dump this variable and just check for value 11

    def moveCard(self, x, y): #moves card to (x, y). Only call upon the initial creation of the card.
        self.front.move(x,y)
        self.back.move(x,y)

    def show(self):
        if self.open:
            try:
                self.back.undraw()
            except:
                pass
            self.front.draw(self.win)
        else:
            self.back.draw(self.win)
        pass#Make the card visible

    def hide(self):#Hide the card
        self.front.undraw()

    def clone(self): #Returns the copy of the card
        return Card(self.index,self.image,self.value,self.win)