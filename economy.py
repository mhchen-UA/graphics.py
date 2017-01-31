""" 
 ___     ___   _         _  	           _____   _       ____   _       _____
|   \   /   | |_|  ___  | |      _____    |  __ | | |     |  __| | |     |  __ |  ______
| |\ \_/ /| |  _  |  _| | |___  |  _  |   |  ___| | |     | |    | |___  |  ___| \   _  |
| | \___/ | | | | | |_  |  _  | | |_| |_  | |___  | |     | |__  |  _  | | |___   | | | |
|_|       |_| |_| |___| |_| |_| |_______| |_____| |_|     |____| |_| |_| |_____|  |_| |_|     
 Date: 1/31/17
 Period:1
 """

from graphics import *
import random

class Window:
    def __init__(self):
        self.x = 800
        self.y = 600
        self.day = 0
        self.textSize = 25
        self.e = None #Input
        self.revenue = 0   #Revenue
        self.stock = 0  #Quanity owned
        self.inputCost = 0 #Input Cost
        self.profit = self.revenue - self.inputCost #Profit
        self.name = "" #User's name

    def createInterface(self): #makes the window and divides the sections with lines
        self.win = GraphWin("Window",self.x,self.y)
        self.line1 = Line(Point(self.x//2,self.y),Point(self.x//2,0))
        self.line2 = Line(Point(self.x//2,self.y//2),Point(self.x,self.y//2))
        self.line3 = Line(Point(0,self.y//6),Point(self.x//2,self.y//6))
        self.line4 = Line(Point(0,self.y//3),Point(self.x//2,self.y//3))
        self.line5 = Line(Point(0,self.y//2),Point(self.x//2,self.y//2))
        self.line6 = Line(Point(0,(self.y*2)//3),Point(self.x//2,(self.y*2)//3))
        self.line7 = Line(Point(0,(self.y*5)//6),Point(self.x//2,(self.y*5)//6))
        self.line1.draw(self.win)#Drawing the lines to organize
        self.line2.draw(self.win)
        self.line3.draw(self.win)
        self.line4.draw(self.win)
        self.line5.draw(self.win)
        self.line6.draw(self.win)
        self.line7.draw(self.win)
        self.textDay = Text(Point(self.x//4,self.y//12),self.name+"'s shop. Day "+str(self.day)) #setting texts
        self.textDay.setSize(self.textSize)
        self.textDay.draw(self.win)
        self.e = Entry(Point((self.x//4)+30,self.y//4),20)#Setting input price box
        self.e.draw(self.win)
        self.eText = Text(Point((self.x//4)-80,self.y//4),"Price: $")
        self.eText.setSize(self.textSize)
        self.eText.draw(self.win)
        self.textRevenue = Text(Point(self.x//4,(self.y*5)//12),"Stock: "+str(self.stock))
        self.textRevenue.setSize(self.textSize)
        self.textRevenue.draw(self.win)
        self.textStock = Text(Point(self.x//4,(self.y*7)//12),"Revenue: "+str(self.revenue))
        self.textStock.setSize(self.textSize)
        self.textStock.draw(self.win)
        self.textInputCost = Text(Point(self.x//4,(self.y*3)//4),"Input Cost: "+str(self.inputCost))
        self.textInputCost.setSize(self.textSize)
        self.textInputCost.draw(self.win)
        self.textProfit = Text(Point(self.x//4,(self.y*11)//12),"Profit: "+str(self.revenue - self.inputCost))
        self.textProfit.setSize(self.textSize)
        self.textProfit.draw(self.win)
        self.newsText = Text(Point((self.x*3)//4,(self.y*9)//16),"News")
        self.newsText.setSize(26)
        self.newsText.draw(self.win)
        
    def getProduct(self): #ask the user for product to sell
        product = button("Gas, Car, or Cake?")
        if product.lower() == "cake" or product.lower() == "car" or product.lower() == "gas":   
            return product
        return self.getProduct()
    
    def setGraph(self): #create curve based on elasticity
        self.graph = Rectangle(Point((self.x*9)//16,(self.y)//16),Point((self.x*15)//16,(self.y*7)//16))
        self.graph.draw(self.win)
        pass

    def getNews(self, product):  #gets random news
        def cakeNews():
            #[Title,text,demand-shift]
            news = [
                ["CAKES ARE UNHEALTHY","The University of Anarctica has\nfound a shocking discovery on\nthe strong correlation between cakes and\ndiabetes. \'They have too much\nsugar, the public should really refrain\nfrom eating them\' says Dr. Michael,\nthe leading scientist in this study.",-20],
                ["POLICE SHOOTING SPARKS\nPROTESTS","An amateur video shot by a\nbystander, officer Repucci fatally shot an\nunarmed 9 year old girl while she was\nmaking cake. Protesters are encouraging\neveryone to buy cakes to support their\ncampaign in prosecuting Repucci.",50],
                ["NATIONAL CAKE DAY","The President of the United States has\nofficial declared this day to be National\nCake Day. Citizens world-wide are\ncelebrating by buying more cake.",200],
                ]
            selector = random.randint(0,len(news)-1)
            return news[selector]
        def carNews(): 
            news = [
                ["MITSUBISHI OPENS UP\nSTORES","The foreign company, Mitsubishi, has\nopened their ever-popular shop at the\nother side of town. Hurry up and\nget there to get the cheapest prices!\nSorry to the other car firms that have\nto compete with Mitusbishi.\nMay you rest in peace.",-40],
                ["ECONOMY BOOST","Statisticians have estimated a large increase in the incomes of many Americans. \'I am delighted by this shift\' says economist Dr. David. \'I expect an increase in purchases of expensive products like cars.\'",20],
                ["SEVERE WEATHER\nDESTROYS PARKING LOT","Severe thunderstorms were blamed for the destruction of a university's parking lot. Investigators say that large hail damaged the cars, which leaked gasoline, and a struck of lightning lit the floor on fire.",5], 
                ]
            selector = random.randint(0,len(news)-1)
            return news[selector]
        def gasNews():
            news = [
            ["BOYCOTT "+self.name.upper()+"!",self.name+"'s oil rig exploded over the Gulf\nof Mexico, prompting ocean wildlife\nprotestors to boycott their gas.",0],
            ["BP DROPS OUT","The massive company, BP, has\nofficially announced on twitter that\n they're going out of business. \'That's\none less competitor for the gas\n industry\' says economist Rempala.",20]
            ]
            selector = random.randint(0,len(news)-1)
            return news[selector]
        if product == "cake":
            return cakeNews()
        elif product == "car":
            return carNews()
        elif product == "gas":
            return gasNews()

    def setNews(self,product):
        self.newsBox = Rectangle(Point((self.x*9)//16,(self.y*19)//32),Point((self.x*15)//16,(self.y*15)//16))
        self.newsBox.draw(self.win)
        self.newsTitle = Text(Point((self.x*3)//4,(self.y*11)//16),product[0])
        self.newsTitle.setSize(20)
        self.newsTitle.draw(self.win)
        self.newsBody = Text(Point((self.x*3)//4,(self.y*13)//16),product[1])
        self.newsBody.setSize(15)
        self.newsBody.draw(self.win)
        
    def start(self,product,w): #Starts from Day 1, asks for price, then calculates revenue based on graph
        news = w.getNews(product)
        w.setNews(news)
        update(1)
        self.newsTitle.undraw()
        self.newsBody.undraw()
        self.win.setBackground(color_rgb(random.randint(1,255),random.randint(1,255),random.randint(1,255)))

    def getName(self):
        self.name = button("Name")

def button(text): #I Used ABSTRACTION to make a button with a flexible text for input
        w = GraphWin("",300,200)
        TEXT = Text(Point(150,30),text)
        TEXT.setSize(25)
        TEXT.draw(w)
        e = Entry(Point(150,75),20)
        e.setSize(20)
        e.draw(w)
        button = Rectangle(Point(100,110),Point(200,150))
        button.setFill("Cyan") #Making a submit button
        button.draw(w)
        textSubmit = Text(Point(150,130),"Submit")
        textSubmit.setSize(15)
        textSubmit.draw(w)
        a = True
        Input = ""
        while(a):
            b = w.getMouse() #Event for if the mouse is clicked in the rectangle
            if b.getX()<200 and b.getX()>100 and b.getY() >110 and b.getY()<150:
                a = False
                Input = e.getText()
        w.close()    
        return Input

def main():
    w = Window()
    w.getName()
    w.createInterface() 
    product = w.getProduct()
    w.setGraph()
    while True:
        w.start(product,w)

main()
