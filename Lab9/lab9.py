#lab9

#3
def twoscomplement(binarystring):
  complement = list(binarystring) 
  i=0
  size = len(binarystring)
  while i<size:
    if complement[i] == '1':
      complement[i] = '0'
    else:
      complement[i] = '1'
    i += 1
  
  size -= 1
  carry = 1 
  while size>=0:
    if complement[size]=='1' and carry==1:
      complement[size] = '0'
    elif complement[size]=='0' and carry==1:
      complement[size] = '1'
      carry = 0
    size -= 1

  complement =  "".join(complement) 
  print complement
    
#4
def intToBinaryString(n):
  binary = ""
  while n>0:
    binary = binary + String(n % 2)
    n = n/2
    
  return (16-len(binary))*'0' + binary
  
#5
file = r"C:\Users\Sameer Naumani\Documents\Repos\Python\Lab9\croak.wav"
file2 = r"C:\Users\Sameer Naumani\Documents\Repos\Python\Lab9\Elliot-hello.wav"
soundfile = makeSound(file)
sound = makeSound(file2)
explore(soundfile)

def doubleAmplitude(soundfile):
  for sample in getSamples(soundfile):
    value = getSampleValue(sample)
    setSampleValue(sample,value*2)
  explore(soundfile)

#6
def doublehalf(sound):
  for sample in getSamples(sound):
    value = getSampleValue(sample)
    if(value > 0):
      setSampleValue(sample,value*2)
    else:
      setSampleValue(sample,value*0.5)
  explore(sound)

def zeronegative(sound):
  for sample in getSamples(sound):
    value = getSampleValue(sample)
    if(value > 0):
      setSampleValue(sample,0)
  explore(sound)

#7
def minValue(sound):
  minimum = 0
  for s in getSamples(sound):
    minimum = min(minimum,getSampleValue(s))
    
  print minimum
  
#8
def countZeros(sound):
  count = 0
  for s in getSamples(sound):
    if (getSampleValue(s) == 0):
      count += 1
  return count
    
#9
def clip(sound,maxvalue):
  for s in getSamples(sound):
    if(getSampleValue(s) > maxvalue):
      setSampleValue(s,maxvalue)
    elif(getSampleValue(s) < -maxvalue):
      setSampleValue(s,-maxvalue)
  explore(sound)
  
#10
def falseIncreaseVolume(sound,increment):
  for s in getSamples(sound):
    value = getSampleValue(s)
    setSampleValue(s,value + increment)
  explore(sound)
    
  



      
      