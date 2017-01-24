
```from graphics import *```
***
GraphWin("Title",width,height)  --> Creates the window

_________________

Window Methods
_____________________

  setBackground("red")
  
  isClosed()   returns boolean
  
  isOpen()     returns boolean
  
  plotPixel(x,y,"red") (Use trig loops to draw curves)
  
  win.getMouse()  waits and returns the clicked position as Point(x,y)
  
  win.checkMouse()  returns last-clicked position, then resets
  
  win.getKey()    waits and returns the key pressed as a string
  
  win.checkKey()    returns the last key-pressed, then resets
  
  win.getHeight()
  
  win.getWidth()
  
  __________________
  
  Draw Objects
  _______________
  Point(x,y)   
  Line(Point,Point)
  Circle(Point,radius) 
  Rectangle(Point,Point)
  Polygon(Point,Point,Point...)   Infinite points
  Text(Point,"text")
  ____________________
  Draw Methods
  _________________
  setFill("Red")   changes interior color
  setOutline("Red")   changes outline color
  setWidth(int)   outline width
  move(x,y)    relative translation
  ______________
  Input Object: Entry(Point,width)
  Input Methods
  ______________
  getText()    gets text inside textbox 
  setText("string")
  setSize(int)  5-36, character font size
  setTextColor("red")
  move(x,y)
  draw(GraphWin)
  undraw()
  ___________________________
  Color uses X11: http://cng.seas.rochester.edu/CNG/docs/x11color.html
  _____________
  color_rgb(0,255,255)   red, green, blue, 0-255
  _________________
  _________________
  Example:
  ```
  from graphics import *
  win = GraphWin("Michael",500,300)
  for i in range(30):
    c = Circle(Point(20,30),40+i)
    c.draw(win)
    update(4)
    c.undraw()
    
  ```
