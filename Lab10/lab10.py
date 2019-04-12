#Lab 10


file = r"C:\Users\Sameer Naumani\Documents\Repos\Python\Lab10\Elliot-hello.wav"
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
  samplingRate = int(getSamplingRate(sound2))
  for sample in getSamples(sound2):
    largest = max(largest,abs(getSampleValue(sample)))
  amplification = 32767.0/largest
 
  #normalize first second
  if(samplingRate>getLength(sound2)):
    for s in range(0,getLength(sound2)):
      louder = amplification * getSampleValueAt(sound2,s)
      setSampleValueAt(sound2,s,louder)
      
  for sampleindex in range(0,samplingRate):
    value = getSampleValueAt(sound2,sampleindex)
    setSampleValueAt(sound2,sampleindex,largest)
    
    factor = int(largest/5)
    starting = samplingRate
    i=2
    
    while(starting <getLength(sound)):
      if((starting + samplingRate) < getLength(sound)):
        for sindex in range(starting,(starting+samplingRate)):
          value = getSampleValueAt(sound2,sindex)
          setSampleValueAt(sound,setSampleValueAt(sindex,value*(largest-factor)))
          factor=factor*i
          i +=1
          starting = starting + samplingRate
      else:
        for sindex in range(starting, getLength(sound)):
          value = getSampleValueAt(sound2,sindex)
          setSampleValueAt(sound2,sindex,value*(largest-factor))
          break
          
      
     
  explore(sound2)
            

#3
def thisistest(sound):
  target = duplicateSound(sound)
  targetIndex = 0
  for sourceIndex in range(0,11135):
    setSampleValueAt(target,targetIndex,getSampleValueAt(sound,sourceIndex))
    
  
  
       
    
    
  
    