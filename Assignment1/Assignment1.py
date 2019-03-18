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
#Leafs
f1 = r"C:\Users\Sameer Naumani\Documents\Repos\Python\Assignment1\Images\leafs.jpg"
p1 = makePicture(f1)
#explore(p1)

#Leafs St.Patrick's Theme
#6 ligthen the picture
#7 Change white parts to Green
#8 Add a green border
#9 Split in half

#Function 6
# Lighten the entire picture using makeLighter functions
def light(p1):
  for px in getPixels(p1):
   color = getColor(px)
   color = makeLighter(color)
   setColor(px ,color)

# Function 7
# Leafs St.Patricks Theme
# Change the white color to green.
# If any of the pixels are white, change them to green
def greenify(p1):
  for px in getPixels(p1):
    green = getGreen(px)
    if (px > 250):
      setColor(px,makeColor(0,green,0))

          
#Function 9
# Add a green border to the picture
# Make the pixels on the top and bottom green by using getHeight function
# Make the pixels on either side green by using getWidth function
def border(p1):
  bottom = getHeight(p1) -10
  rightside = getWidth(p1) - 10
  for px in getPixels(p1):
    y = getY(px)
    x = getX(px)
    #Top Border
    if (y<10):
      setColor(px,green)
    #Bottom Border
    if (y>bottom):
      setColor(px,green)
    #Left Side
    if (x<10):
      setColor(px,green)
    #Right Side
    if (x>rightside):
      setColor(px,green)
  
#Function 10
# Mirror the picture 
def mirror(p1):
  pixels = getPixels(p1)
  target = len(pixels) -1
  for index in range(0,len(pixels)/2):
    px1 = pixels[index]
    color1 = getColor(px1)
    # Copy the details of the pixels to the target which is on the opposite side
    px2 = pixels[target]
    setColor(px2,color1)
    #decrement target 
    target -= 1
  
# Use functions (6-10) to create final product and save picture
def Leafs(p1):
  light(p1)
  greenify(p1)
  border(p1)
  mirror(p1)
  explore(p1)
  writePictureTo(p1, 'C:\Users\Sameer Naumani\Documents\Repos\Python\Assignment1\Images\Leafs2.jpg')
  

f2 = r"C:\Users\Sameer Naumani\Documents\Repos\Python\Assignment1\Images\goku.jpg"
p2 = makePicture(f2)
#explore(p2)

#Function 11
# Greyscale. 
# luminance values
def greyscale(p2):
  for px in getPixels(p2):
    newRed = getRed(px) * 0.3
    newGreen = getGreen(px) * 0.6
    newBlue = getBlue(px) * 0.1
    luminance = newRed+newGreen+newBlue
    setColor(px,makeColor(luminance,luminance,luminance))


  
#Function 12
# Changing his hair colour and aura around him to red
# Fun Fact: The red transformation is also known as super saiyan 4 
def superred(p2):
  for px in getPixels(p2):
    if (getRed(px)>100) and (getGreen(px)>100) and (getBlue(px)<50):
      setColor(px,makeColor(255,0,0))
  explore(p2)

#Function 13
# Sepia tint
def sepia(p2):
  greyscale(p2)
  for px in getPixels(p2):
    red = getRed(px)
    blue = getBlue(px)
    #tint shadows
    if(red<65):
      red = red*1.1
      blue = blue*0.8
    #tint midtones
    if (red > 64 and red < 195):
      red = red*1.15
      blue = blue*0.85
     #tint highlights
    if (red > 191):
      red = red*1.08
      if (red > 255):
        red = 255

      blue = blue*0.93
   
     #set the new color values
    setBlue(px, blue)
    setRed(px, red)
  
     
# Use function 11-13 
def goku(p2):
  superred(p2)
  sepia(p2)
  show(p2)
 
f3 = r"C:\Users\Sameer Naumani\Documents\Repos\Python\Assignment1\Images\nature.jpg"
p3 = makePicture(f3)
#explore(p3)

# Function 14
# Add Text
def addtext(p3):
  #import java.awt.Font as Font
  str = "Banff, Alberta"
  #myFont = makeStyle("Arial", Font.BOLD, 24)
  addText(p3,420,450,str, yellow)
 

#Function 15
# Custom Text2 in a box
def addtext2(p3, str2):
  #import java.awt.Font as Font
  addRect(p3, 645,480, 300,150, cyan)
  str = "How was your trip?"
  #myFont = makeStyle("Arial", Font.BOLD, 24)
  addText(p3,650,500,str, yellow)
  addText(p3,710,520,str2, white)
 

#Function 16
#darken photo
def darken(p3):
  for px in getPixels(p3):
   color = getColor(px)
   color = makeDarker(color)
   setColor(px ,color)
  

#Function 17 
# Decrease blue on half the picture
def decreaseBlue(p3):
    pixels = getPixels(p3)
    for index in range(0,len(pixels)/2):
      pixel = pixels[index]
      value = getBlue(pixel)
      setBlue(pixel,value * 0.5)
    

#Use functions 14-17 to manipulate picture
def nature(p3):
  darken(p3)
  addtext(p3)
  addtext2(p3, "great")
  decreaseBlue(p3)
  explore(p3)

f4 = r"C:\Users\Sameer Naumani\Documents\Repos\Python\Assignment1\Images\plane.jpg"
p4 = makePicture(f4)
#explore(p2)

#Function 18
# Negate Picture
# Subtract each value by 255
def negate(p4):  
  for p in getPixels(p4):
    red=getRed(p)
    green=getGreen(p)
    blue=getBlue(p)
    negColor=makeColor( 255-red, 255-green, 255-blue)
    setColor(p,negColor)

#Function 19
# split mirror
def mirrorsplit(p4):
  middle = getWidth(p4) / 2
  width = getWidth(p4)
  for y in range(0,getHeight(p4)):
    for x in range(0,middle):
      leftPixel = getPixel(p4,x,y)
      rightPixel = getPixel(p4, width-x-1,y)
      color = getColor(leftPixel)
      setColor(rightPixel,color)
  
  
#function 20
# Increase color on the bottom half of the picture
def increaseBlue(p4):
    pixels = getPixels(p4)
    for index in range(len(pixels)-1, len(pixels)/2, -1):
      pixel = pixels[index]
      value = getBlue(pixel)
      setBlue(pixel,value * 1.5)

# Use functions 18 to 20 
def plane(p4):
  mirrorsplit(p4)
  negate(p4)
  increaseBlue(p4)
  explore(p4)
  
# Use all functions
f_llama = r"C:\Users\Sameer Naumani\Documents\Repos\Python\Assignment1\Images\llama.jpg"
llama = makePicture(f_llama)
def all(llama):
  Leafs(llama)
  goku(llama)
  plane(llama)
  nature(llama)
  explore(llama)
