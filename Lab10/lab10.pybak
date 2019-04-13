#Lab 10


file = r"C:\Users\Sameer Naumani\Documents\Repos\Python\Lab10\moondog.Bird_sLament.wav"
sound = makeSound(file)
explore(sound)

#1
def increaseDecrease(sound, position):
  length = getLength(sound)
  for index in range(0,length):
    if(index < position*length):
      value = getSampleValueAt(sound,index)
      setSampleValueAt(sound,index,value*2)
    else:
      value = getSampleValueAt(sound,index)
      setSampleValueAt(sound,index,value*0.2)
    
  explore(sound)
  
#2
def increaseDecrease2(sound):
  sound2 = duplicateSound(sound)
  largest = 0
  second = 1
  #samples/sec
  samplingRate = int(getSamplingRate(sound2))
  for sample in getSamples(sound2):
    largest = max(largest,abs(getSampleValue(sample)))
  amplification = 32767.0/largest
 
  #normalize first second  
  for s in range(0,getLength(sound2)):
    seconds = int(getLength(sound2)/samplingRate)
    #normalize first second
    if(s <= samplingRate):
      louder = amplification * getSampleValueAt(sound2,s)
      setSampleValueAt(sound2,s,louder)
    else:
      for second in (0,seconds):
        amplification = 1 - (0.2)*second
        volume = amplification * getSampleValueAt(sound2,s)
        setSampleValueAt(sound2,s,volume)
      
  explore(sound2)
      
 
            

#3
def thisistest(sound):
  target = duplicateSound(sound)
  targetIndex = 11730
  for sourceIndex in range(0,11135):
    setSampleValueAt(target,targetIndex,getSampleValueAt(sound,sourceIndex))
    targetIndex = targetIndex+1
  
  targetIndex2 = 43095
  for sourceIndex in range(12240,19210):
    setSampleValueAt(target,targetIndex2,getSampleValueAt(sound,sourceIndex))
    targetIndex2 = targetIndex2+1

#4    
def reverse(sound):
  target = makeEmptySound(getLength(sound))
  #start at end
  sourceIndex = getLength(sound)-1
  s = getSamples(sound)
  for index in range(0,getLength(target)):
    value = getSampleValue(s[sourceIndex])
    setSampleValueAt(target,index,value)
    sourceIndex = sourceIndex-1
  
  explore(target)

#5  
def clip(sound,start,end):
  target = makeEmptySound(end-start)
  tIndex = 0
  s = getSamples(sound)
  for index in range(start,end):
    value = getSampleValue(s[index])
    setSampleValueAt(target,tIndex, value)
    tIndex = tIndex + 1
  
  explore(target)
  
  
       
    
    
  
    