#3
def invertedpyramid(letter):
  space = " "
  print 6*space, letter
  print 4*space, 3*letter
  print 2*space, 5*letter
  print space, 7*letter
  print 9*letter

#4 ***
def textsquare(ch, n):
  space = " "
  string = ch*n
  string2 = ch + space*(n-2) +ch 
  
  print string
  
  #for each character in the range string length -2 since there are two rows taking up space
  for char in range(len(string)-2):  
    print string2
    
  print string

#5 for loop
def justConsonants(string):
  vowels = ""
  consonants = ""
  for letter in string:
    if letter in "AEIOUYaeiouy":
     vowels = vowels + letter
    if not (letter in "AEIOUYaeiouy"):
      consonants = consonants + letter
    
  print consonants

#6 .lower()
def justConsonants2(string):
  pile1 = ""
  pile2 = ""
  for letter in string:
    if letter.lower() in "aeiouy":
     pile1 = pile1 + letter
    if not (letter.lower() in "aeiouy"):
      pile2 = pile2 + letter
    
  print pile2

#7 Mirroring
def dup3(s) :
  target = ''
  for letter in s :
    target = letter + target + letter
  return target

#8 Mirroring
def dup5(string) :
  target = ''
  for letter in string :
    target = letter + "-" + target + "-" + letter 
  return target

#9 seperating
def seperate(string):
  Vowels = ""
  Consonants = ""
  for letter in string:
    if letter in "AEIOUYaeiouy":
     Vowels = Vowels + letter
    if not (letter in "AEIOUYaeiouy"):
      Consonants = Consonants + letter
    
  print "Vowels:", Vowels
  print"Consonants:", Consonants

#10
def encode2(string, alpha2):
  alpha1 = 'abcdefghijklmnopqrstuvwxyz'
  secret = ''
  secret2 = ''
  for letter in string :
    if letter not in alpha1:
      ##Skips to next iteration of for loop
      continue 
    index = alpha1.find(letter)
    secret = secret + alpha2[index]
  
  print secret






   
