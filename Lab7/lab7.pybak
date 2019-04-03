#Lab 7

#1
setMediaPath("C:\Users\Sameer Naumani\Documents\Repos\Python\Lab7\Images")
picture = makePicture(getMediaPath("beach.jpg"))
picture1 = makePicture(getMediaPath("caterpillar.jpg"))
picture2 = makePicture(getMediaPath("house.jpg"))
picture3 = makePicture(getMediaPath("llama.jpg"))
explore(picture3)

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
def addHouse(picture2,x1,y1):
  targetX = x1
  W = getWidth(picture2)
  H = getHeight(picture2)
  incrementY=0
  canvas = makeEmptyPicture(500,500)
  for sourceX in range(0,W):
    targetY = y1
    for sourceY in range(0,H):
      color = getColor(getPixel(picture2,sourceX,sourceY))
      for i in range(0,getWidth(canvas)-65,65):
        setColor(getPixel(canvas,targetX+i,targetY),color)
        for j in range(0,getHeight(canvas)-80,80):
          setColor(getPixel(canvas,targetX+i,targetY+j),color)
      targetY = targetY + 1
    targetX = targetX + 1 
    
  explore(canvas)
  

  
#4
def drawGrid(picture1,spacing):
  W = getWidth(picture1)
  H = getHeight(picture1)
  ycort=0
  xcort=0
  for x in range(0,W,spacing):
    xcort = x
    for y in range(0,H,spacing):
      ycort=y
      #vert
      addLine(picture1,xcort,ycort,xcort,H,black)
      addLine(picture1,xcort,ycort,W,ycort,black)
  show(picture1)
      
      

def drawGrid12(picture, color):

  w = getWidth(picture)
  h = getHeight(picture)

  printNow(str(w) + " x " + str(h))

  w_offset = 20  # Vertical lines offset
  h_offset = 10  # Horizontal lines offset

  # Starting at 1 to avoid drawing on the border
  for y in range(1, h):     
    for x in range(1, w):
      # Here is the trick: we draw only 
      # every offset (% = modulus operator)
      if (x % w_offset == 0) or (y % h_offset == 0):
        px = getPixel(picture, x, y)
        setColor(px, color)
        

#5 not done
def drawGrid2(picture1):
  spacing = 5
  W = getWidth(picture1)
  H = getHeight(picture1)
  x = 5
  y = 5
  totaln=0
  for n in range(0,W):
    totaln=totaln+n
    #vert
    addLine(picture1,x+totaln,y,x+totaln,H,black) 
    addLine(picture1,x,y+totaln,W,y+totaln,black)    
    
      #horiz   
   # addLine(picture1,x,y,W,y,black)

  explore(picture1)
  

def flip_horiz(picture3):
    width = getWidth(picture3)
    height = getHeight(picture3)

    for y in range(0, height):
        for x in range(0, width/2):
            sourcePixel = getPixel(picture3, x, y)
            targetPixel = getPixel(picture3, width - x - 1, y)
            color = getColor(sourcePixel)
            setColor(sourcePixel, getColor(targetPixel))
            setColor(targetPixel, color)

    show(picture3)


#6 not done
def flipHorizontally(picture3):
  W = getWidth(picture3)
  H = getHeight(picture3)
  for x in range(W,0,-1):
    for y in range(H,0,-1):
      px = getPixel(picture3,x-1,y-1)
      newpx = getPixel(picture3,x-1,y-1)
      color = getColor(px)
      setColor(px,color)
  show(picture3)
  

#7
def scaleup(picture1):
  W = getWidth(picture1)
  H = getHeight(picture1)
  canvas = makeEmptyPicture(1000,1000)
  sourceX = 0
  for targetX in range(0,W*2):
    sourceY = 0
    for targetY in range(0,H*2):
      color = getColor(getPixel(picture1,int(sourceX),int(sourceY)))
      setColor(getPixel(canvas,targetX,targetY), color)
      sourceY = sourceY + 0.5
    sourceX = sourceX + 0.5
  
  explore(canvas)

#8
def scaledown(picture1):
  W = getWidth(picture1)
  H = getHeight(picture1)
  canvas = makeEmptyPicture(1000,1000)
  sourceX = 0
  for targetX in range(0,W/2):
    sourceY = 0
    for targetY in range(0,H/2):
      color = getColor(getPixel(picture1,sourceX,sourceY))
      setColor(getPixel(canvas,targetX,targetY),color)
      sourceY = sourceY + 2
    sourceX = sourceX + 2
  show(canvas)

#9
def mirror20(picture1):
  mirrorPoint = 20
  width = getWidth(picture1)
  for y in range(0,getHeight(picture1)):
    for x in range(0,mirrorPoint):
      leftPixel = getPixel(picture1,x,y)
      rightPixel = getPixel(picture1,width - x - 1,y)
      color = getColor(rightPixel)
      setColor(leftPixel,color)
  
  show(picture1)





      

   