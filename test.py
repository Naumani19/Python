file = r"C:\Users\Sameer Naumani\Documents\Repos\Python\Lab7\Images\Capture.JPG"
picture = makePicture(file)

def mirrorhalf(picture):
  W = getWidth(picture)
  H = getHeight(picture)
  mirrorpoint = W/2
  for x in range(mirrorpoint,W):
    for y in range(0,H):
      px = getPixel(picture,x,y)
      r = getRed(px)
      g = getGreen(px)
      b = getBlue(px)
      luminance = (r+g+b)/3
      if luminance<64:
        setColor(px,black)
      elif luminance >120:
        setColor(px,white)
      else:
        setColor(px,red)
      negColor = makeColor(255-r,255-g,255-b)
      leftPixel = getPixel(picture,x,y)
      rightPixel = getPixel(picture,W - x - 1,y)
      color = getColor(leftPixel)
      setColor(rightPixel,color)

      #setColor(px,negColor)
  explore(picture)
      
    