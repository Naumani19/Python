#Write 20 functions to manipulate a picture

#A start on the required program for assignment a1 in cps109.
# The object is to write and use 20 functions for modifying a picture.
# The functions are based on material from Chapters 1-4 of the course text.
# I am modifying the llama picture from the course resources, but
# you can use any picture of your own or from the media resources.

# Function 1 add Box
# This function puts a red box on the llama
# First explore to find the coordinates
def addBox(picture) :
  pixels = getPixels(picture)
  for pixel in pixels :
    x = getX(pixel)
    y = getY(pixel)
    if 171 < x < 233 and 152 < y < 188 :
      setColor(pixel, red)

# Function 2
# Function addBox2 is a parameterization so that we can put a
# box of a given color anywhere
def addBox2(picture, x1, y1, x2, y2, color ) :
  print 'finish'

# Function 3
# Add a circle of a given radius and color
def addCircle(picture, xc, yc, radius, color) :
  pixels = getPixels(picture)
  for pixel in pixels :
    x = getX(pixel)
    y = getY(pixel)
    distance = math.sqrt((x - xc)**2 + (y - yc)**2)
    if distance < radius :
      setColor(pixel, color)

# Function 4
# Draw a black line on the picture, given two points defining the line
# Given two points on a line: (x1, y1), (x2, y2)
# the slope is m = (y2 - y1) / (x2 - x1)
# the intercept is b = y1 - m * x1
# the line is y = m * x + b
def addLine(picture, x1, y1, x2, y2) :
  pixels = getPixels(picture)
  m = 1.0 * (y2 - y1) / (x2 - x1)
  b = y1 - m * x1
  for pixel in pixels :
    x = getX(pixel)
    y = getY(pixel)
    y_line = m * x + b
    if y == y_line :
    setColor(pixel, black)

# Function 5
# Draw a line on the picture, given two points defining the line
# and a parameter defining the thickness, and a parameter for color
# Given two points on a line: (x1, y1), (x2, y2)
# the slope is m = (y2 - y1) / (x2 - x1)
# the intercept is b = y1 - m * x1
# the line is y = m * x + b
def addLine2(picture, x1, y1, x2, y2, thickness, color) :
  pixels = getPixels(picture)
  m = 1.0 * (y2 - y1) / (x2 - x1)
  b = y1 - m * x1
  for pixel in pixels :
    x = getX(pixel)
    y = getY(pixel)
    y_line = m * x + b
    distance = int(abs(y_line - y) + 0.5)
    if distance < thickness / 2 :
      setColor(pixel, color)
# Below we are calling the functions and saving the picture
  f_llama = r"C:\Users\Sameer Naumani\Documents\Repos\Python\Assignment1\Images\llama.jpg"
  llama = makePicture(f_llama)
  addBox(llama)
  addCircle(llama, 16, 16, 16, red)
  W = getWidth(llama)
  H = getHeight(llama)
  addCircle(llama, W-17, 16, 16, green)
  addCircle(llama, W-17, H-17, 16, blue)
  addCircle(llama, 16, H-17, 16, cyan)
  addLine(llama, 0, 0, 10, 10)
  addLine2(llama, 0, 40, 10, 40, 16, magenta)
  explore(llama)
  writePictureTo(llama, '/home/eharley/1/a1.jpg')

#Picture 1
#Goku
f1 = r"C:\Users\Sameer Naumani\Documents\Repos\Python\Assignment1\Images\leafs.jpg"
p1 = makePicture(f1)
explore(p1)

#Leafs
#6 ligthen the picture
#7 greyscale the picture
#8 Change the line getColor
#9 Split in half

#Function 6
# Lighten the entire picture using makeLighter functions
def light(p1):
  for px in getPixels(p1):
   color = getColor(px)
   color = makeLighter(color)
   setColor(px ,color)

#Function 7
# Turn the picture into greyscale. We will first use the luminance values to reduce red, blue and green values.
# After which negate the values by subtracting each from 255
def greyScale(p1):
  for px in getPixels(p1):
    newRed = getRed(px) * 0.3
    newGreen = getGreen(px) * 0.6
    newBlue = getBlue(px) * 0.1
    luminance = newRed+newGreen+newBlue
    setColor(px,makeColor(luminance,luminance,luminance))
  show(picture)
  for p in getPixels(p1):
    red=getRed(p)
    green=getGreen(p)
    blue=getBlue(p)
    negColor=makeColor( 255-red, 255-green, 255-blue)
    setColor(p,negColor)
  show(picture)

# Function 8
# Change the color of the bottom line
def linechange(p1):
    for px in getPixels(p1):


def Zero(picture):
  for pixel in getPixels(picture):
    setRed(pixel,0)
    setGreen(pixel,0)
    setBlue(pixel,0)
  explore(picture)


#2
#def max(picture):
  for pixel in getPixels(picture):
    setRed(pixel,255)
    setGreen(pixel,255)
    setBlue(pixel,255)
  explore(picture)

#3
def test4(picture) :
  for pixel in getPixels(picture) :
    red = getRed(pixel)/3
    green = getGreen(pixel)/3
    blue = getBlue(pixel)/3
    color = makeColor(red, green, blue)
    setColor(pixel, color)
  show(picture)

#4
def blue(picture):
  for pixel in getPixels(picture):
    blue = getBlue(pixel)
    if (blue < 150):
      setBlue(pixel,255)
      setGreen(pixel,255)
      setRed(pixel,255)
  explore(picture)

#5
def blueish(picture):
  for pixel in getPixels(picture):
    blue = getBlue(pixel)
    if (blue>100):
      newblue = getBlue(pixel)*2
      setBlue(pixel,newblue)
  explore(picture)


#6
def blueify(picture):
  for pixel in getPixels(picture):
    blue = getBlue(pixel)*2
    red = getRed(pixel)/2
    green = getGreen(pixel)/2
    color = makeColor(red, green, blue)
    setColor(pixel,color)
  show(picture)

#7
def greyScale(picture):
  for px in getPixels(picture):
    newRed = getRed(px) * 0.3
    newGreen = getGreen(px) * 0.6
    newBlue = getBlue(px) * 0.1
    luminance = newRed+newGreen+newBlue
    setColor(px,makeColor(luminance,luminance,luminance))
  show(picture)
  for p in getPixels(picture):
    red=getRed(p)
    green=getGreen(p)
    blue=getBlue(p)
    negColor=makeColor( 255-red, 255-green, 255-blue)
    setColor(p,negColor)
  show(picture)

#8
def decomposition(picture):
  greyscale(picture)
  negate(picture)

def greyscale(picture):
  for px in getPixels(picture):
    newRed = getRed(px) * 0.3
    newGreen = getGreen(px) * 0.6
    newBlue = getBlue(px) * 0.1
    luminance = newRed+newGreen+newBlue
    setColor(px,makeColor(luminance,luminance,luminance))
  explore(picture)

def negate(picture):
  for p in getPixels(picture):
    red=getRed(p)
    green=getGreen(p)
    blue=getBlue(p)
    negColor=makeColor( 255-red, 255-green, 255-blue)
    setColor(p,negColor)
  explore(picture)

#9
def lighten(picture):
  for px in getPixels(picture):
    red = getRed(px) + 75
    green = getGreen(px) +75
    blue = getBlue(px) + 75
    #greyscale
    newRed = getRed(px) * 0.3
    newGreen = getGreen(px) * 0.6
    newBlue = getBlue(px) * 0.1
    luminance = newRed+newGreen+newBlue
    setColor(px,makeColor(luminance,luminance,luminance))
  explore(picture)

#10
def lighter(picture):
  light(picture)
  greyscale(picture)

def light(picture):
  for px in getPixels(picture):
   color = getColor(px)
   color = makeLighter(color)
   setColor(px ,color)
