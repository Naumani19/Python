file = r"C:\Users\Sameer Naumani\Documents\Repos\Python\Lab6\Images\mountain.jpg"
picture = makePicture(file)

#1
def blueAndGold(picture):
  bottom = getHeight(picture) - 10
  rightside = getWidth(picture) - 10
  for px in getPixels(picture):
    gold = makeColor(255,233,0)
    y = getY(px)
    x = getX(px)
    #Top Border
    if (y < 10):
      setColor(px, makeColor(0,0,255))
    #Bottom Border
    if (y > bottom):
      setColor(px, makeColor(0,0,255))
    #Left Side
    if (x < 10):
      setColor(px, gold)
    #Right Side
    if (x>rightside):
      setColor(px, gold)
    
  explore(picture)
  
#2
file2 = r"C:\Users\Sameer Naumani\Documents\Repos\Python\Lab6\Images\face.jpg"
picture2 = makePicture(file2)
#explore(picture2)

def purpleTeeth(picture2):
  for px in getPixels(picture2):
    x = getX(px)
    y = getY(px)
    if 29<=x<=72:
      if 130<=y<=170:
        color = getColor(px)
        if distance(color,white)<20.0:
          purple = makeColor(128,0,128)
          setColor(px,purple)
  explore(picture2)


#3
def checkLuminance(r,g,b):
    newRed = r * 0.3
    newGreen = g * 0.6
    newBlue = b * 0.1
    luminance = newRed+newGreen+newBlue
    if luminance < 10:
      print("Thats going to be awfully dark.")
    elif (luminance > 50) and (luminance < 200):
      print("Looks like a good range.")
    elif luminance > 250:
      print("That's nearly white")
    else:
      print("seems legit")
      
#4
f3 = r"C:\Users\Sameer Naumani\Documents\Repos\Python\Lab6\Images\statue.jpg"
picture3 = makePicture(f3)
#explore(picture3)
f4 = r"C:\Users\Sameer Naumani\Documents\Repos\Python\Lab6\Images\moon.jpg"
background = makePicture(f4)
#explore(background)

def chromakeyBlueAbove(picture3, background, skyY):
  for px in getPixels(picture3):
    x = getX(px)
    y = getY(px)
    # If the sum of red and green are less than the blue background and the height is less than a specific value (height of the foreground picture)
    if (getRed(px) + getGreen(px) < getBlue(px) + 100) and (y < skyY):
      bgpx = getPixel(background,x,y)
      bgcol = getColor(bgpx)
      setColor(px,bgcol)
  explore(picture3)
      
      
#5
f4 = r"C:\Users\Sameer Naumani\Documents\Repos\Python\Lab6\Images\planet1.jpg"
f5 = r"C:\Users\Sameer Naumani\Documents\Repos\Python\Lab6\Images\planet2.jpg"
p1 = makePicture(f4)
p2 = makePicture(f5)
#explore(p1)
#explore(p2)


def interleave(p1,p2):
  W = getWidth(p1)
  H = getHeight(p1)
  canvas = makeEmptyPicture(W,H)
  for y in range(0,H):
    for x in range(0,W):
        pic1 = getPixel(p1,x,y)
        pic2 = getPixel(p2,x,y)
        newcanvas = getPixel(canvas,x,y)
        
        if(x<=20) or (40<x<=60) or (80<x<=100) or (120<x<=140) or (160<x<+180):
          color = getColor(pic1)
          setColor(newcanvas,color)
        else:
          color = getColor(pic2)
          setColor(newcanvas,color)             
  explore(canvas)

    

#6
f6 = r"C:\Users\Sameer Naumani\Documents\Repos\Python\Lab6\Images\caterpillar.jpg"
p6 = makePicture(f6)
explore(p6)

def getRegion(p6, x1,y1,x2,y2):
  W = getWidth(p6)
  H = getHeight(p6)
  canvas = makeEmptyPicture(W,H)
  
  # Now, do the actual copying
  targetX = 100
  for sourceX in range(x1,x2):
    targetY = 100
    for sourceY in range(y1,y2):
      color = getColor(getPixel(p6,sourceX,sourceY))
      setColor(getPixel(canvas,targetX,targetY), color)
      targetY = targetY + 1
    targetX = targetX + 1
  #show(src)
  show(canvas)
  return canvas
  
#7
def getRegionTwice(p6,x1,y1,x2,y2):
  W = x2 - x1
  H = y2 - y1
  canvas = makeEmptyPicture(2*W,2*H)
  
  # Now, do the actual copying
  targetX = 50
  for sourceX in range(x1,x2):
    targetY = 50
    for sourceY in range(y1,y2):
      color = getColor(getPixel(p6,sourceX,sourceY))
      setColor(getPixel(canvas,targetX,targetY), color)
      targetY = targetY + 1
    targetX = targetX + 1
  
  targetX = 50
  for sourceX in range(x1,x2):
    targetY = 0
    for sourceY in range(y1,y2):
      color = getColor(getPixel(p6,sourceX,sourceY))
      setColor(getPixel(canvas,targetX,targetY), color)
      targetY = targetY + 1
    targetX = targetX + 1
    
  #show(src)
  show(canvas)
  return canvas
  
