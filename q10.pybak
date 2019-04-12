#quiz 10

def inverse(binarystring):
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