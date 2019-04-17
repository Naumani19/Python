#Assignment2

#Pick the filese
file_1 = r"C:\Users\Sameer Naumani\Documents\Repos\Python\Assignment2\tinywaldo.jpg"
file_2 = r"C:\Users\Sameer Naumani\Documents\Repos\Python\Assignment2\tinyscene.jpg"
search = makePicture(file_1)
template = makePicture(file_2)

def greyScale(template,search):
  for px in getPixels(template):
    newRed = getRed(px) * 0.3
    newGreen = getGreen(px) * 0.6
    newBlue = getBlue(px) * 0.1
    luminance = newRed+newGreen+newBlue
    setColor(px,makeColor(luminance,luminance,luminance))
  for px in getPixels(search):
    newRed = getRed(px) * 0.3
    newGreen = getGreen(px) * 0.6
    newBlue = getBlue(px) * 0.1
    luminance = newRed+newGreen+newBlue
    setColor(px,makeColor(luminance,luminance,luminance))
  

#Compare at x and y the luminance of template and search function
def compareOne(template,search,x,y): 		#This function compares the luminance
  widthSearch = getWidth(search)
  heightSearch = getHeight(search)
  widthTemplate = getWidth(template)
  heightTemplate = getHeight(template)
  sum = 0
  matrixSearch = [[1000000 for i in range (widthSearch)] for j in range (heightSearch)]
  matrixTemplate = [[1000000 for i in range (widthTemplate)] for j in range (heightTemplate)]
  for partX in range(widthTemplate):
    for partY in range (heightTemplate):
      Pixsearch = getPixel(search,partX+x,partY+y) #gets pixel of search
      Pixtemplate = getPixel(template,partX,partY) #gets pixel of template
      luminanceSearch = (getRed(Pixsearch)+getGreen(Pixsearch)+getBlue(Pixsearch))/3
      luminanceTemplate = (getRed(Pixtemplate)+getGreen(Pixtemplate)+getBlue(Pixtemplate))/3
      matrixSearch[partY][partX] = luminanceSearch
      matrixTemplate[partY][partX] = luminanceTemplate
      luminanceDiff = abs(matrixSearch[partY][partX]-matrixTemplate[partY][partX])  #finds difference in luminance
      sum = sum + luminanceDiff
  return sum

#compare all positions and return a matrix with all the values
#This function utilizes the compareOne function to compute the total running sum
def compareAll(template,search):
  widthSearch = getWidth(search)
  heightSearch = getHeight(search)
  widthTemplate = getWidth(template)
  heightTemplate = getHeight(template)
  matrix = []
  matrixSearch = [[1000000 for i in range (widthSearch)] for j in range (heightSearch)]
  matrixTemplate = [[1000000 for i in range (widthTemplate)] for j in range (heightTemplate)]
  for x in range (getWidth(search)-getWidth(template)):
    for y in range(getHeight(search)-getHeight(template)):
      sum = compareOne(template,search,x,y)
      matrix.append(sum)  #creates a matrix with the difference in luminance
  return matrix


#After the matrix is returned, find the minimum value
#This value will resemble the closest match to the template
def find2Dmin(matrix):		#This functions finds the lowest element in the matrix
  min = 1000000
  x = -1
  y = 0
  i = 0
  for num in matrix:
    if i % (getHeight(search)-getHeight(template)) > 0: #doesnt compute around bottom and right edge of search image
      y = y + 1
      i = i + 1
    elif i % (getHeight(search)-getHeight(template)) == 0:
      x = x + 1
      y = 0
      i = i + 1
    if num < min:
      min = num
      
  column = x
  row = y
  
  return column,row
  
#We will add a green border around waldo or the matching template
#Make pixels on the top and bottom green by using getHeight
#Make pixels on either side green by using getWidth function
def displayMatch(search, column, row, widthTemplate, heightTemplate): #This function places a yellow rectangle around Waldo
  widthSearch = getWidth(search)
  heightSearch = getHeight(search)
  widthTemplate = getWidth(template)
  heightTemplate = getHeight(template)
  bottom = heightSearch-5
  right = widthSearch-5
  for px in getPixels(search):
    y = getY(px)
    x = getX(px)
    if (y<5):
      setColor(px,green)
    #Bottom Border
    if (y>bottom):
      setColor(px,green)
    #Left Side
    if (x<5):
      setColor(px,green)
    #Right Side
    if (x>right):
      setColor(px,green)
  

#call all functions in the driver function to locate waldo

def findWaldo(template,search):
  greyScale(template,search)
  widthSearch = getWidth(search)
  heightSearch = getHeight(search)
  widthTemplate = getWidth(template)
  heightTemplate = getHeight(template)
  matrix = compareAll(template,search)
  column,row = find2Dmin(matrix)
  displayMatch(search, column, row, widthTemplate, heightTemplate)
  explore(search)
