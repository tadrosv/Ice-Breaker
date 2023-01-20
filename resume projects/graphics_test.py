
from graphics import *

def graphics_test():
    win = GraphWin("Testing graphics.py", 400, 400)
            
    rect = Rectangle(Point(100, 100), Point(300, 300))
    rect.setFill("blue")
    rect.setOutline("blue")
    rect.draw(win)
    win.getMouse()
    rect.setFill("maroon")
#
    win.getMouse()
    egg = Oval(Point(50, 100), Point(350, 300))
    egg.setWidth(10)
    egg.draw(win)
#
    win.getMouse()
    circ = Circle(Point(110, 110), 100)
    circ.setFill("magenta")
    circ.setOutline("magenta")
    circ.draw(win)
    
    win.getMouse()
    circ.move(190, 190)
#
    win.getMouse()
    point_list = [Point(100, 100),
                  Point(200, 200),
                  Point(200, 100)]
    polygon = Polygon(point_list)
    polygon.setFill("orange")
    polygon.draw(win)
#
    win.getMouse()
    text = Text(Point(150, 50), "Banjo")
    text.draw(win)
    text.setSize(36)
    
    win.getMouse()
    
    text.setText("Fiddle")
    text.setTextColor("purple")

    win.getMouse()     
    enter = Entry(Point(200, 350), 10)
    enter.setSize(36)
    enter.draw(win)
    
    win.getMouse()
    
    
    enter_text = Text(Point(275, 50), "")
    enter_text.draw(win)
    enter_text.setSize(36)
    win.getMouse()
    
    enter_text.setText(enter.getText())
    
    win.getMouse()

    banjo = Image(Point(200, 200), "banjo.gif")
    banjo.draw(win)
    
    
    win.getMouse()
   
    win.close()

graphics_test()
