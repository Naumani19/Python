def convert_string(val):
  pile = ""
  for c in val:
    a = ord(c)
    if a%2 == 0:
      pile = pile + '2'
    elif a%3 ==0:
      pile = pile + '3'
    elif a%2==0 and a%3==0:
      pile = pile + '2'
    else:
      pile = pile + '0'
  return pile

 # These questions are for the sample midterm

# Let's define at the top some global variables
f_beach = '/home/eharley/1/beach.jpg'
beach = makePicture(f_beach)
setMediaPath('/home/eharley/1/')

# Question 1: exploring a picture to find a value somewhere
# Question 2: ASCII for 'e' ord('e')
# Question 3: letter after 'z' ... chr(ord('z') + 1)

# Question 4: sumOrds
# add the ordinal values of all the letters in
# the given string
def sumOrds(string) :
  sum = 0
  for letter in string :
    sum = sum + ord(letter)
  print sum

# Question 5: catChrs
# A function to convert a string of digits that represent
# single digit indices into the alphabet into the corresponding letters
# which are concatenated to form a string
def catChrs(stringDigits) :
  alpha = 'abcdefghijklmnopqrstuvwxyz'
  pile = ''
  for letter in stringDigits :
    i = int(letter)
    pile = pile + alpha[i]
  print pile

# Question 6: sumRed
# A function to sum the red in the first n pixels of a given picture
def sumRed(picture, n) :
  pixels = getPixels(picture)
  sum = 0
  for i in range(n) :
    r = getRed(pixels[i])
    print r
    sum = sum + r
  print 'sum of red in first ', n, ' pixels is', sum

# Question 7: sumRedByIndex()
# A function to sum the red in the pixels with indices
# start ot end, inclusive, of a given picture
def sumRedByIndex(picture, start, end) :
  pixels = getPixels(picture)
  sum = 0
  for i in range(start, end + 1) :
    r = getRed(pixels[i])
    print r
    sum = sum + r
  print 'sum of red ', sum

# Question 8: flipCase()
# A function that takes a string like 'aBCd' and flips the case
# of each letter, to print a string like 'AbcD', for this example.
# If a letter is neither upper nor lower, then it is not included in the
# output string, so flipCase('aa3CC') prints AAcc.

def flipCase(string) :
  pile = ''
  for letter in string :
    if letter.islower() :
      pile = pile + letter.upper()
    if letter.isupper() :
      pile = pile + letter.lower()
  print pile

# Question 9:
# To mirror and double letters
def mirror2(string) :
  pile = ''
  for letter in string :
    pile = letter + letter + pile + letter + letter
  print pile

# Question 10:
# Keyword Cipher, where build the alphabet by putting the
# key after the first five other letters, and followed by the rest.
def encode2(string, key) :
  alpha1 = 'abcdefghijklmnopqrstuvwxyz'
  alpha2 = ''
  count = 0
  for letter in alpha1 :
    if not letter in key :
      alpha2 = alpha2 + letter
      count = count + 1
      if count == 5 :
        alpha2 = alpha2 + key
  print alpha2, len(alpha2)
  pile = ''
  for letter in string :
    index = alpha1.find(letter)
    pile = pile + alpha2[index]
  print pile
