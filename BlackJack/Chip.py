from Button import Button
from graphics import *

class Chip(Button):
    def __init__(self, win, center, radius, value):
        #Creates a chip that has all the parameters of a button
        super().__init__(win, center, radius, value, "black")

        self.label.setText(value)

        value = int(value)
        self.value = value
        self.bet = False #used in readChip (future readBank method for differenting what was clicked)

        self.paint(value)

    def paint(self, v):
        #set the colour of the chip depending on the value
        chipColors = ["white", "red", "lightgreen", "lightblue", "darkgrey", "yellow", "purple", "orange", "pink", "gold"]
        chipVals = [1, 5, 25, 50, 100, 500, 1000, 2000, 5000, 10000]

        for i in range(0,10,1):
            if(v == chipVals[i]):
                self.body.setFill(chipColors[i])
                break

    def moveChip(self, initialPoint, finalPoint):
        #make a clone
        #show it move
        #delete the clone
        print()