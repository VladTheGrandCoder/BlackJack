from graphics import *
class Abstract(): #used to represent split hands. Since I did not implement the split command, this has no use. 
    def __init__(self, win, x, value):
        self.win = win

        self.played = False

        self.number = Text(Point(x, y), value)
        self.number.setTextColor("white")

        self.frame = Rectangle(Point(x-20, 650-30),Point(x+20, 650+30))
        self.frame.setFill("lightred")
        self.frame.setOutline("darkred")
        self.frame.setWidth(2)

    def show(self):
        if(self.played):
            self.frame.setFill("lightgreen")
        self.frame.draw(self.win)
        self.number.draw(self.win)

    def hide(self):
        self.frame.undraw(self.win)
        self.number.undraw(self.win)