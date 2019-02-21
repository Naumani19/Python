#1

f = r"C:\Users\Sameer Naumani\Documents\Repos\Python\Lab4\images\fun-butterfly.png"
picture = makePicture(f)
explore(picture)

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

  


  
