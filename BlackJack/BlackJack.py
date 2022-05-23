from graphics import *
from Button import Button
from Chip import Chip

def end(win):
    win.getMouse()
    win.close()

def main():
    win = GraphWin("BlackJack", 1000, 720)
    win.setBackground("green")

    chip = Chip(win, Point(500, 360), 60, 100, "white", "black")
    chip.show()

    p1 = Point(730, 710)
    p2 = Point(10, 435)
    rect = Rectangle(p1,p2)
    rect.draw(win)

    i = 1

    chipColors = ["white", "red", "lightgreen", "lightblue", "darkgrey", "yellow", "purple", "orange", "pink", "gold"]

    while(i < 11):
        x = 0
        y = 0

        if(i<6):
            x =  (i * 140) - 50
            y = 440 + 66
        else:
            j = i - 5
            x =  (j * 140 ) - 50
            y = 440 + (66 *3)

        center = Point(x,y)
        radius = 60
        c = Chip(win,center,radius,i*100,chipColors[i-1],"black")
        c.show()
        i +=1


    while(True):
        p = win.getMouse()
        if(chip.clicked(p)):
            chip.hide()
            print(chip.value)
        else:
            chip.show()
        

    card = Image(Point(500, 200-50), "Cards/9_of_diamonds.png")
    card.draw(win)

    card2 = Image(Point(500, 500+70), "Cards/9_of_diamonds.png")
    card2.draw(win)

    end(win)
main()

