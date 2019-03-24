#swaps the red and blue channels for every pixel where thee green value is less than 125
file = r"C:\Users\Sameer Naumani\Documents\Repos\Python\quiz6\plane.jpg"
picture = makePicture(file)
explore(picture)

def swap_colors(picture):
  for px in getPixels(picture):
    red = getRed(px)
    green = getGreen(px)
    blue = getBlue(px)
    if (green<125):
      setColor(px, makeColor(blue,green,red))
  explore(picture)