from graphics import *
import math

class Button:
    def __init__(self, win, center, radius, label, colour):
        self.x = center.getX()
        self.y = center.getY()
        self.r = radius
        self.win = win

        self.circ = Circle(center, radius)
        self.circ.setFill(colour)
        self.circ.setWidth(3)
        self.circ.setOutline("black")

        self.label = Text(center, label)
        self.label.setSize(30)

        self.visible = False

    def hide(self):
        #hides the button from the user and does not check if clicked 
        if(self.visible):
            self.circ.undraw()
            self.label.undraw()
            self.visible = False

    def show(self):
        #shows the button to the user and checks if clicked
        if(not self.visible):
            self.circ.draw(self.win)
            self.label.draw(self.win)
            self.visible = True

    def clicked(self, point):
        #checks if clicked
        x2 = point.getX()
        y2 = point.getY()

        distance = math.sqrt((self.x - x2)**2 + (self.y - y2) **2)
        if(distance < self.r and self.visible):
            return True
        else:
            return False

