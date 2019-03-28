#Transpose Image

file = r"C:\Users\Sameer Naumani\Documents\Repos\Python\q7\statue.jpg"
picture = makePicture(file)
explore(picture)

def transpose(picture):
  W = getWidth(picture)
  H = getHeight(picture)
  canvas = makeEmptyPicture(W,H)   
  #row
  for y in range(0,H):
    #column
    for x in range(0,W):
      original = getPixel(picture,x,y)
      transposePixel = getPixel(canvas,y/2,x/2)
      
      color = getColor(original)
      setColor(transposePixel,color)
      

  
  explore(canvas)
  
    
    
    