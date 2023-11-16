calculator = "do some culculation"
num1 = int(input('Enter the First number: '))
num2 = int(input('Enter the second number:'))
op =input('Enter the operator: ')

if op == '+':

  print('The addition is ', num1+num2)
  
elif op == '-':
  print
  print('The subtraction is ', num1-num2)
  
elif op == '*':
  print('multiplication is ')
  print( num1*num2)
   
  
elif op == '/':
  print('division is ')
  print( num1/num2)
  print( 'The divisionis ', abs(num1/num2))
else:
  print('Invalid Operator')
  
   