#Lab 7

#1
setMediaPath("C:\Users\Sameer Naumani\Documents\Repos\Python\Lab7\Images")
picture = makePicture(getMediaPath("beach.jpg"))
picture1 = makePicture(getMediaPath("caterpillar.jpg"))
picture2 = makePicture(getMediaPath("house.jpg"))

def addSunset():
  addArcFilled(picture,526,90,104,100,0,180,yellow)
  show(picture)

#2
def addBullseye(picture1,x1,y1,width):
  addArcFilled(picture1,x1,y1,width,100,0,360,red)
  addArcFilled(picture1,x1+10,y1+10,width-20,80,0,360,blue)
  addArcFilled(picture1,x1+20,y1+20,width-40,60,0,360,yellow)
  show(picture1)
  
  
#3
def copy(picture2,canvas):
  targetX = 0
  for sourceX in range(0,getWidth(picture2)):
    targetY = 0
    for sourceY in range(0,getHeight(picture2)):
      color = getColor(getPixel(picture2,sourceX,sourceY))
      setColor(getPixel(canvas,targetX,targetY),color)
      targetY = targetY + 1
    targetX = targetX + 1 

def addHouse(picture2,x1,y1):
  canvas = makeEmptyPicture(200,200)
  for x in range(getWidth(x1)):
    for y in range(getHeight(y1)):
    
  
  show(canvas)
   