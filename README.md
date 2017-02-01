
##### Place this file in the **same** place/folder as your main python file. (Like put both in desktop) Then in your main python file, add this:
```python
from graphics import *
```
##### Make sure you're using IDLE
***
## Window Object: `GraphWin("Title",width,height)`

##### Example: `win = GraphWin("Mikey",400,300)`

#### Coordinate System:

![Image Not Displaying Correctly](https://cloud.githubusercontent.com/assets/15696473/22276676/34aafcb2-e283-11e6-8ff3-a6e6f97dc931.png "Coordinate System")

## Window Methods


  `setBackground("red")`
  
  `isClosed()`   returns boolean
  
  `isOpen()`     returns boolean
  
  `plotPixel(x,y,"red")` (Use trig loops to draw curves)
  
  `getMouse()`  waits and returns the clicked position as Point(x,y)
  
  `checkMouse()`  returns last-clicked position, then resets
  
  `getKey()`    waits and returns the key pressed as a string
  
  `checkKey()`    returns the last key-pressed, then resets
  
  `getHeight()`
  
  `getWidth()`
  
  __________________
## Point Object: Point(x,y)

## Point Methods:

`getX()` 

`getY()`

 `move(x,y)` Relative Translation
 
  ________________
  
## Draw Objects
  

  `Line(Point,Point)`
  
  
  `Circle(Point,radius)` 
  
  
  `Rectangle(Point,Point)` Top-left point, bottom-right point
  
  
  `Polygon(Point,Point,Point...)`   Infinite points
  
  
  `Text(Point,"text")`
  ____________________

## Draw Methods
  
  
  
  `setFill("Red")`   changes interior color
  
  
  `setOutline("Red")`   changes outline color
  
  
  `setWidth(int)`   outline width
  
  
  `move(x,y)`    relative translation
  
  `draw(GraphWin)`  draws it
  
  `undraw()`   removes it
  
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
X11 Colors: http://cng.seas.rochester.edu/CNG/docs/x11color.html
  
  `color_rgb(0,255,255)`  0-255, returns a color
  _________________
###  Example:
  ```python
from graphics import *
win = GraphWin("Michael",500,300) #Window of height 500px and width 300px
for i in range(30):
  c = Circle(Point(100+i,100),40) #Creates a Circle with radius 40px
  c.draw(win)  #Actually draws it
  update(1)  #basically time.sleep(1)
  c.undraw()  #Removes it
```



------------
