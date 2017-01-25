
##### Place this file in the same place/folder where you store your main python file. Then in your main python file, add this:
```python
from graphics import *
```
##### Make sure you're using IDLE
***
Window Object: `GraphWin("Title",width,height)`
------------

## Window Methods





  `setBackground("red")`
  
  `isClosed()`   returns boolean
  
  `isOpen()`     returns boolean
  
  `plotPixel(x,y,"red")` (Use trig loops to draw curves)
  
  `win.getMouse()`  waits and returns the clicked position as Point(x,y)
  
  `win.checkMouse()`  returns last-clicked position, then resets
  
  `win.getKey()`    waits and returns the key pressed as a string
  
  `win.checkKey()`    returns the last key-pressed, then resets
  
  `win.getHeight()`
  
  `win.getWidth()`
  
  __________________
  
## Draw Objects
  
  
  
  
  `Point(x,y)` 
  
  
  `Line(Point,Point)`
  
  
  `Circle(Point,radius)` 
  
  
  `Rectangle(Point,Point)`
  
  
  `Polygon(Point,Point,Point...)`   Infinite points
  
  
  `Text(Point,"text")`
  ____________________

## Draw Methods
  
  
  
  
  `setFill("Red")`   changes interior color
  
  
  `setOutline("Red")`   changes outline color
  
  
  `setWidth(int)`   outline width
  
  
  `move(x,y)`    relative translation
  ______________
## Input Object: `Entry(Point,width)`
  
## Input Methods
  
  
  
  
  `getText()`    gets text inside textbox 
  
  
  `setText("string")`
  
  
  `setSize(int)`  5-36, character font size
  
  
  `setTextColor("red")`
  
  
  `move(x,y)`
  
  
  `draw(GraphWin)`
  
  
  `undraw()`
  ___________________________
  Color uses X11: http://cng.seas.rochester.edu/CNG/docs/x11color.html
  
  `color_rgb(0,255,255)`  0-255, returns a color
  _________________
###  Example:
  ```python
from graphics import *
win = GraphWin("Michael",500,300)
for i in range(30):
  c = Circle(Point(100+i,100),40)
  c.draw(win)
  update(1)  #basically time.sleep(1)
  c.undraw()
```
