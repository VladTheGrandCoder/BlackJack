from graphics import *
class Card():
    def __init__(self, index, image, value, win):
        self.win = win

        self.index = index #index from 1 to 52 
        self.image = image #used for cloning (path to the image file)
        self.value = value #value in the game of BlackJack

        self.front = Image(Point(0,0),image)    #front image
        self.back = Image(Point(0,0), "Cards\card_back.png")  #back image
        self.open = True                       #whether the front is open 

    def moveCard(self, x, y): #moves card to (x, y). Only call upon the initial creation of the card.
        self.front.move(x,y)
        self.back.move(x,y)

    def show(self):#Make the card visible
        if self.open:
            try:
                self.back.undraw()
            except:
                pass
            self.front.draw(self.win)
        else:
            self.back.draw(self.win)
        pass

    def hide(self):#Hide the card
        self.front.undraw()

    def clone(self): #Returns the copy of the card
        return Card(self.index,self.image,self.value,self.win)