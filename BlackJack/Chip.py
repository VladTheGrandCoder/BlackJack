from Button import Button
from graphics import *

class Chip(Button):
    def __init__(self, win, center, radius, value, colour, outlineColour):
        #Creates a chip that has all the parameters of a button
        super().__init__(win, center, radius, value, colour, outlineColour)
        self.value = value
        value = str(value)
        self.label.setText(value)

    def moveTo(self, point):
        #position in the bank 
        print()
    def add():
        #add the chip to the bet and remove from the bank
        print()

    def remove():
        #remove chip from the bet and add to the bank
        print()

