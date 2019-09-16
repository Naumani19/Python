#1
#Recall the keyword cipher programs from Chapter 3: buildCipher(key) and encode(string,
#alpha2), which you modified in lab2, question 10. The buildCipher function could create more
#complicated alphabets. As long as the receiver and sender build the cipher alphabet (alpha2)
#in the same way, we only need the keyword (not the special alphabet alpha2) and the
#message to encode and decode. Write encode2(message, key) which
#�?� builds alpha2 by putting the keyword at the end of the alphabet, rather than the front;
#�?� skips blanks and punctuation;
#�?� converts uppercase in the message to lowercase before encoding.
#encode2('Alan Turing defined computing', 'turing') . As an initial
#check, encode2('Ada Lovelace, first programmer', 'earth') should
#produce: bfbosegobdgilwxyuwsjwbppgw
def encode2(string, alpha2) :
  alpha1 = 'abcdefghijklmnopqrstuvwxyz'
  #alpha2 = 'bcdfgijklmnopqsuvwxyz' + alpha2
  secret = ''
  pile = ''
  #create cipher
  for l in alpha1:
    if l in alpha2:
      pile = pile
    if l not in alpha2:
      pile = pile + l
  pile = pile + alpha2
  print pile

  for letter in string.lower() :
   if letter not in pile:
      continue
   i = alpha1.find(letter)
   secret = secret + pile[i]
  return secret

#2
def encode3(string, alpha2):
 alpha1 = 'abcdefghijklmnopqrstuvwxyz'
 #alpha3 = 'zyxwvutsrqponmlkjihgfedcba'
 secret = ''
 alpha3 = ''
 pile = ''

 #reverse alpha by index
 for i in range(len(alpha1)-1,-1,-1):
     alpha3 = alpha3 + alpha1[i]
 print alpha3

 for l in alpha3:
    if l in alpha2:
      pile = pile
    if l not in alpha2:
      pile = pile + l
 pile = alpha2 + pile
 print pile

 for letter in string.lower() :
   if letter not in pile:
     continue
   index = alpha1.find(letter)
   secret = secret + pile[index]
 print secret


#3
def dupTimes3(something) :
  dup = '_'
  for index in range(0, len(something)) :
    dup = dup + something
  return dup

#4
def findem4(n) :
  letters = 'abcdefghijklmnopqrstuvwxyz'
  pile = ''
  for index in range(0, len(letters)) :
    pile = pile + letters[index % n]
  return pile

#5
def spacedout(string,n):
  pile = ''
  space = ' '
  for index in string:
    pile = pile + index + space*n
  print pile

#6
def spacedout2(string,n):
  pile = ''
  space = ' '
  for index in string:
    if not index in " ":
      pile = pile + index
    if index in " ":
      pile = pile + index + space*n
  print pile

#8
f = r"C:\Users\Sameer Naumani\Documents\Repos\Python\Lab3\images\caterpillar.jpg"
picture = makePicture(f)
#explore(picture)

def decreaseRed20(picture):
  for pixel in getPixels(picture):
    value = getRed(pixel)
    setRed(pixel,0.2 *value)
  explore(picture)
  file = r"C:\Users\Sameer Naumani\Documents\Repos\Python\Lab3\images\caterpillar2.jpg"
  writePictureTo(picture,file)


#10
f2 = r"C:\Users\Sameer Naumani\Documents\Repos\Python\Lab3\images\caterpillar.jpg"
picture2 = makePicture(f2)
#explore(picture2)

def swapRed(picture2):
  for pixel in getPixels(picture2):
    value1 = getRed(pixel)
    value2 = getGreen(pixel)
    setRed(pixel,value2)
    setGreen(pixel,value1)
  explore(picture2)
  
def words():  
  wordlist = ['cat','dog','rabbit']
  letterlist = [ ]
  for word in wordlist:
    for letter in word:
      if letter in letterlist:
        continue
      else:
        letterlist.append(letter)
  print(letterlist)
