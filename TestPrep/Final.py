#Final Practice
file = r"C:\Users\Sameer Naumani\Documents\Repos\Python\TestPrep\beach.jpg"
picture = makePicture(file)

#1
#Write a program catChrs(stringOfDigits) which takes in a string of digits, like '5419230' and returns the concatenated letters corresponding to the digits where each digit is used as an index into the alphabet.  
#Thus, catChrs('541') would return feb, since f is the  letter with index 5 in 'abcdefghij', e is letter with index 4, and b has index 1.  
def catChrs(stringOfDigits):
  alpha = "abcdefghijklmnopqrstuvwxyz"
  digits = stringOfDigits.split()
  pile = ""
  
  for num in stringOfDigits:
    num = int(num)
    pile = pile + alpha[num]
    
  print pile
  
#2
#Write a function blueify(picture) as follows. 
#Double the blue value of every pixel and cut the red and green value in half. 
def blueify(picture):
  for px in getPixels(picture):
    red = getRed(px)
    blue = getBlue(px)
    green = getGreen(px)
    setBlue(px,blue*2)
    setGreen(px,green*0.5)
    setRed(px,red*0.5)
  explore(picture)
    
#6
#Write a program sumRedByIndex(picture, index1, index2) which adds up the red values of the pixels of picture picture from indices index1 to index2, inclusive, where the pixels are obtained using getPixels(picture).  
#For example, sumRed(island, 2, 4) is 522, since the red values for indices 2, 3, 4 are all 174. 
# What is the result of sumRedByIndex(island, 50, 60)?
def sumRedByIndex(picture,index1,index2):
  pixels = getPixels(picture)
  sum = 0
  for index in range(index1,index2):
    pixel = pixels[index]
    red = getRed(pixel)
    sum = sum + red
  
  print sum
  
#7
# Write a function reflect(string), which prints a mirror of the string. 
# For example, reflect('Abc') produces the string 'cbAAbc', and reflect('rubber duck') produces the string: 'kcud rebburrubber duck'.
def reflect(string):
  pile = ""
  for letter in string:
    pile = letter + pile + letter
    
  print pile

#8
#Write a function replicate(sentence), which prints or returns a longer version of the input sentence, by doubling the first word, tripling the second word, quadrupling the third word, and so on.  For example, replicate('This is a hot day ') produces 
#'ThisThis isisis aaaa hothothothothot daydaydaydaydayday ', and replicate('0 1 2 3 4 5') produces '00 111 2222 33333 444444 5555555 '. 
# The string method split() will help you.

def replicate(sentence):
  pile = ""
  n = 0
  parts = sentence.split()
  
  for index in range(0,len(parts)-1):
    n += 1
    pile = pile + " " + parts[index]*n
    
  print pile

#9
#Write a function pinkify(picture) that pinkifies a picture. 
#For each pixel, if the three components are all over 100, then set the color of the pixel to pink, otherwise no change.  
 
def pinkify(picture):
  for px in getPixels(picture):
    red = getRed(px)
    blue = getBlue(px)
    green = getGreen(px)
    if(red > 100 and green >100 and blue>100):
      setColor(px,pink) 
  explore(picture)

#10
#Write a function redRange(picture, x1, y1, x2, y2) which looks at pixels in the rectangle defined by top left corner (x1, y1) 
# and bottom right corner (x2, y2).  
#If the color of the pixel has distance(color, white) < 110 then make the color of the pixel red.

def redRange(picture, x1,y1,x2,y2):
  for x in range(x1,x2):
    for y in range(y1,y2):
      pixel = getPixelAt(picture,x,y)
      color = getColor(pixel)
      if distance(color,white)<110:
        setColor(pixel,red)
        
  explore(picture)
  
  
#splice
file = r"C:\Users\Sameer Naumani\Documents\Repos\Python\TestPrep\Elliot-hello.wav"
sound = makeSound(file)

def normalize(sound):
  largest = 0
  for s in getSamples(sound):
    value = getSampleValue(s)
    largest = max(largest,value) 
  amplification = 32767.0/largest
  
  for s in getSamples(sound):
   louder = Amplification * getSampleValue(s)
   setSampleValue(s,louder)
   

def minValue(sound):
  s = getSamples(sound)
  minimum = getSampleValue(s[0])
  for s in getSamples(sound):
    value = getSampleValue(s)
    minimum = min(minimum,value)
    
  return minimum

def clip(sound,maxvalue):
  for s in getSamples(sound):
    value = getSampleValue(s)
    if (value>maxvalue):
      setSampleValue(s,maxvalue)
    elif (value<-maxvalue):
      setSampleValue(s,-maxvalue)
      
  explore(sound)
  
#increase half sound and decrease the other half
def increaseAndDecrease(sound):
  for index in range(0,getLength(sound)/2):
    value = getSampleValueAt(sound,index)
    setSampleValueAt(sound,index,value*2)
    
  
      
  






    
    