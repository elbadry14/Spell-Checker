import difflib
dicti= open ('1.txt','r')
dictionary=dicti.read().splitlines()
name=input('please enter the phrase :')
x=name.split()
thecorrectedphrase=[]
for i in x :
 def binarySearch(n, m):
   correct=[]
   first = 0
   last = len(n)-1
   itr=0
   while first<=last:
       midpoint = (first + last)//2
       if n[midpoint] == m:
           return 1
             
       else:
           if m < n[midpoint]:
                     last = midpoint-1
           else:
                   first = midpoint+1
   return 0      
        
        
 def suggest ( n,m  ) :
  print ( m , " this word isn't correct\n" )
  mkm=[]
  n.sort()
  number=int(input("please enter the number of similar words you want\n"))
  print (difflib.get_close_matches(m,n, number))
  mkm=input ("what is the word you meant\n")
  return mkm 
 if  binarySearch(dictionary,i)==1:
     thecorrectedphrase.append(i)
 else :
     
     
     thecorrectedphrase.append(suggest(dictionary,i))
  
a= " ".join(thecorrectedphrase)
print ("the correct phrase is :",  a)
