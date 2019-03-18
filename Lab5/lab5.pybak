file = r"C:\Users\Sameer Naumani\Documents\Repos\Python\Lab5\plane.jpg"
picture = makePicture(file)
#explore(picture)

def changeColor(picture, amount, rgbNumber):
   for px in getPixels(picture):
     red = getRed(px)
     green = getGreen(px)
     blue = getBlue(px)
     if rgbNumber == 1:
       fraction = red*amount
       red = red + fraction
     setRed(px,red)
     if rgbNumber == 2:
       fraction = green*amount
       green = green + fraction
     setGreen(px,green)
     if rgbNumber == 3:
       fraction = blue*amount
       blue = blue + fraction
     setBlue(px,blue)
         
   explore(picture)
  
#2
def posterize8(picture):
  for px in getPixels(picture):
    red = getRed(px)
    green = getGreen(px)
    blue = getBlue(px)
    if red <100:
      setColor(px, black)
    else:
      setColor(px, white)
    if green <100:
      setColor(px, black)
    else:
      setColor(px, white)
    if blue <100:
      setColor(px, black)
    else:
      setColor(px, white)
  explore(picture)
  
#3
def border(picture,borderwidth,bordercolor):
  bottom = getHeight(picture) - borderwidth
  rightside = getWidth(picture) - borderwidth
  for px in getPixels(picture):
    y = getY(px)
    x = getX(px)
    #Top Border
    if (y<borderwidth):
      setColor(px,bordercolor)
    #Bottom Border
    if (y>bottom):
      setColor(px,bordercolor)
    #Left Side
    if (x<borderwidth):
      setColor(px,bordercolor)
    #Right Side
    if (x>rightside):
      setColor(px,bordercolor)
    
  explore(picture)
  
#4
def drawXequalsYline(picture, color):
  W = getWidth(picture)
  H = getHeight(picture)
  pixels = getPixels(picture)
  m = min(W,H)
  print m 
  b = 0 - m * 0
  for pixel in pixels :
    x = getX(pixel)
    y = getY(pixel)
    y_line =  x
    if y == y_line :
      setColor(pixel, color)
  explore(picture)

#5 
def drawQuadrants(picture,color):
  pixels = getPixels(picture)
  W = getWidth(picture)
  H = getHeight(picture)
  middleW = W/2
  middleH = H/2
  #slope for horizontal line is zero
  #slope for vertical line is undefined
  for pixel in pixels:
    x = getX(pixel)
    y = getY(pixel)
    y_line = middleH
    x_line = middleW
    if y == y_line:
      setColor(pixel,color)
    elif x == x_line:
      setColor(pixel,color)
  explore(picture)

#6 
def drawDiagonalLine2(picture,color):
  W = getWidth(picture)
  H = getHeight(picture)
  H1 = H-1
  W1 = W-1
  pixels = getPixels(picture)
  # (0, H-1) and (W-1,0)
  m = (H1-0)/(0-W1)
  b = H1 - m * 0
  for px in pixels:
    x = getX(px)
    y = getY(px)
    y_line = m*x + b
    if y == y_line:
      setColor(px,color)
  explore(picture)
  
#7
def posterize3(picture):
  for px in getPixels(picture):
    red = getRed(px)
    green = getGreen(px)
    blue = getBlue(px)
    
    if red > 180:
      setColor(px, makeColor(255,0,0))
    elif blue > 180:
      setColor(px, makeColor(0,0,255))
    elif green > 180:
      setColor(px, makeColor(0,255,0))
    else:
      setColor(px, black)
  
  explore(picture)
  
#8
def pinkify(picture):
  for px in getPixels(picture):
    red = getRed(px)
    green = getGreen(px)
    blue = getBlue(px)
    if red > 100 and green > 100 and blue > 100:
      setColor(px,pink)
  explore(picture)
  
#9
def downupRed(picture):
  W = getWidth(picture)
  Half = W/2
  for px in getPixels(picture):
    red = getRed(px)
    x = getX(px)
    if x < Half:
      red = red*0.5
    elif x > Half:
      red = (200 * red)/100
    setRed(px,red)
  explore(picture)

#10
def thirds(picture):
  H = getHeight(picture)
  print H
  top3rd = H/3
  middle3rd = 2*H/3
  for px in getPixels(picture):
    red = getRed(px)
    green = getGreen(px)
    blue = getBlue(px)
    y = getY(px)
    
    if y < top3rd:
      color = getColor(px)
      color = makeLighter(color)
      setColor(px,color)
    elif y > top3rd and y < middle3rd:
      red = red * 0.3
      green = green * 0.3
      setColor(px, makeColor(red,green,blue))
    elif y > middle3rd:
      negColor=makeColor( 255-red, 255-green, 255-blue)
      setColor(px, negColor)
  
  explore(picture)
      
  

       