##################################################
#SETUP SECTION OF THE GAME  
##################################################
def setup():
#this function draws our boat and places
#the turtle at the start position
  boat = makeWorld(500,500)
  turtle = makeTurtle(boat)
  drawBoat(turtle,boat)
  location(turtle,"quay")
#end setup

def square(turtle,x,y):
#Function to draw a square, called by drawBoat
  penUp(turtle)
  moveTo(turtle,x,y)
  penDown(turtle)
    
  for x in range(0,4):
    forward(turtle,50)
    turnLeft(turtle)
#end square

def drawBoat(turtle,boat):
#Function to draw the representation of our boat
  #Make sure the pen is down
  penDown(turtle)
  
  #starting square  
  square0 = square(turtle,140,275)       
  
  #50x50 squares, spaced 10 apart, 5x3 grid  
  for x in range(200,500,60):
    for y in range(215,395,60):
      square(turtle,x,y)
#end drawBoat

def location(turtle,name):
#Function to move the turtle to a location
  #move the turtle witout drawing a line
  penUp(turtle)                  
  
  #List of locations on the boat 
  if name == "quay":
    moveTo(turtle,115,250)
  elif name == "deck":
    moveTo(turtle,175,250)
  elif name == "foreCastle":
    moveTo(turtle,175,190)
  elif name == "aftCastle":
    moveTo(turtle,175,310)
  elif name == "gunDeck":
    moveTo(turtle,235,250)
  elif name == "crew":
    moveTo(turtle,235,190)
  elif name == "gunPowder":
    moveTo(turtle,235,310)
  elif name == "tweenDeck":
    moveTo(turtle,295,250)
  elif name == "bunk":
    moveTo(turtle,295,190)
  elif name == "passengers":
    moveTo(turtle,295,310)
  elif name == "hold":
    moveTo(turtle,355,250)
  elif name == "food":
    moveTo(turtle,355,190)
  elif name == "liveStock":
    moveTo(turtle,355,310)
  elif name == "ballast":
    moveTo(turtle,415,250)
  elif name == "rum":
    moveTo(turtle,415,190)
  elif name == "incaGold":
    moveTo(turtle,415,310)     
#end location

##################################################
#END --- SETUP SECTION OF THE GAME  
##################################################
    
