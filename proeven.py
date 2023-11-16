num = int(input('Enter a number :'))
if num%2==0:
   print('Even number ')
else:
  print('Od number ')
  
  ####prime numbers 
  num = int(input('enter a number: '))
  if "num%1 num"==0:
    
    print('Prime numbers')
  else:
    print('not a prime number')
num = 29
### to take input fro thr user 
#num = int(input('Enter the number:'))

##definition of flag 
flag= False 
if num ==1:
  print(num, " is not a prime number ")
elif num > 1:
  ##check for factors
  for i in range(2,num):
    if (num % i) == 0:
      ##if factor is found settle 
      flag =True

##break out of loop
    break 
  ###if flag is TRUE
  
  if flag:
    print(num, "is not prime number ")
  else:
    print(num,"is a prime number")
  
   
    
    
    
    
    ###########
from math import*
factorial(6)
from math import*
print(sqrt(144))
print(factorial(8))
    
print(gcd(3, 1))
print(lcm(12, 16, 20))