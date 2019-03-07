file = r"C:\Users\Sameer Naumani\Documents\Repos\Python\TestPrep\beach.jpg"
picture = makePicture(file)
#explore(picture)

#2
def sumRedByIndex(picture,index1,index2):
  pixels = getPixels(picture)
  sum = 0
  #range from 2 to 4 
  for i in range(index1, index2+1):
    r = getRed(pixels[i])
    print r
    sum = sum + r
  print 'sum of red:', sum
  
#3 Write a program catChrs(stringOfDigits) which takes in a string of digits, like '5419230' 
#and returns the concatenated letters corresponding to the digits where each digit is used as an index into the alphabet.  
#Thus, catChrs('541') would return feb, since f is the  letter with index 5 in 'abcdefghij', e is letter with index 4, and b has index 1.  
#After you write your program into the file test1.py, run it from the Command area as catChrs('05443106') and give the output as the answer. 
#Do not type the quote marks, just the letters.
def catChrs(stringOfDigits):
  alpha = "abcdefghijklmnopqrstuvwxyz"
  pile = ""
  for index in stringOfDigits:
    #convert string to integer very important
    index_int = int(index)
    letter = alpha[index_int]
    pile = pile +letter
  print pile
  
  
#4sumRed
#Write a program sumRed(picture, n) which and adds up the red values of the first n pixels of picture picture, where the pixels are obtained using getPixels(picture).  
#Write your program in test1.py, which already has code for making the picture object from beach.jpg.  
#Run the function in the Command area to obtain the result of sumRed(beach, 50).
def sumRed(picture, n):
  pixels = getPixels(picture)
  sum = 0
  for i in range(0,n+1):
    r = getRed(pixels[i])
    sum = sum + r
  print sum
  
#5 What is the ASCII mapping (ordinal value) of 'e'?  
#You can determine this in the JES command area using ord().  Your answer should be a number.
def ASCII(s):
  print ord(s)
#ans 101
  
#6 What is the letter that follows 'z' in the ASCII mapping.  
#The functions ord() and chr() will help you.  Your answer should be one letter.
def ASCII2(s):
  val = ord(s)
  print chr(val+1)
  print chr(ord('z') + 1)
#Ans {

#7 Write a function mirror2(string) that mirrors a string but doubles each letter at the same time, so mirror2('abC') would print 'CCbbaaaabbCC'.  
# What is the output of your function for mirror2('This is a dog!'). 
# As usual, your program must produce the output you say it does, and it must work for any string, otherwise you lose more marks than you gain by putting in the right output.
def mirror2(string):
  pile = ""
  for letter in string:
    pile = letter*2 + pile + letter*2
  print pile

#Ans !!ggoodd  aa  ssii  ssiihhTTTThhiiss  iiss  aa  ddoogg!!

#8
#Write a function flipCase(string), which prints the given string but with the case of each letter changed.  
#For example, flipCase('aBCd') prints 'AbcD'.  
#You can use the string methods lower(), upper() which were introduced in Chapter 3, as well as the methods islower() and isupper() which return True or False depending on the case of the letter.  
#If a letter is neither upper nor lower, then it is left out of the output string.  For example, flipCase('aa3CC') is 'AAcc'.  
#What is the output for flipCase('WinchESteR 3CaThEDraL!'). 
def flipCase(string):
  pile = ""
  for letter in string:
    if (letter.isupper() == true):
      pile = pile + letter.lower()
    elif (letter.islower() == true):
      pile = pile + letter.upper()
    else:
      continue
  print pile

#Ans: wINCHesTErcAtHedRAl

#9
#Write a function encode2(string, key) that does a keyword cipher using the keyword key to create the alternate alphabet by placing the key after the first five other letters, followed by the rest of the letters. 
#For example, if the key is 'earth', then the alternate alphabet is 'bcdfgearthijklmnopqsuvwxyz'.  
#In that case, encode2('deed', 'earth') would produce 'fggf'. 
#What is the output from your function for encode2('goodolddays', 'blue')?  
#Letters from string which are not in the alphabet are automatically coded to the last letter of the alternate alphabet.
def encode2(string,key):
  alpha = "abcdefghijklmnopqrstuvwxyz"
  alpha2 = ""
  #create cipher
  for letter in alpha: 
    if letter not in key:
      #then just print the letter
      alpha2 = alpha2 + letter
    if letter in key:
      #then skip for now
      continue
  
  #put the key word after the first five letters
  print alpha2
  alpha3 = ""
  temp = ""
  
  #print the first 5 letters
  for index in range(len(alpha2)-1):
    if index < 5:
      alpha3 = alpha3 + alpha2[index]
 
  #print the rest of the letters
  for letter in alpha2:
    if letter not in alpha3:
      temp = temp + letter
      
  #combine all together
  alpha3 = alpha3 + key + temp
  print alpha3
  
  #Encrypt the message. We have our cipher alpha3
  secret = ""
  for letter in string:
    index = alpha.find(letter)
    secret = secret + alpha3[index]
  
  print secret

#Ans: lnnfnjffayr


#10
#Write a program sumOrds(string) to add the ordinal values of all the letters in a given string.  
#For example, sumOrds('aac') prints 293, since ord('a') is 97 and ord('c') is 99, and the sum 97 + 97 + 99 is 293.  
#What is sumOrds('abcdefghijklmnopqrstuvwxyz')? 
def sumOrds(string):
  sum = 0
  for letter in string:
    val= ord(letter)
    sum = sum + val
  print sum
  
#Ans: 2847
    

    
    
  
    

    
      
        
    

    
    