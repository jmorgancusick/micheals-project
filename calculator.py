print "Weclome to my calculator!"

x = raw_input('Enter your first number: ')
y = raw_input('Enter your second number: ')

operation = raw_input('Enter your operation (+-*/): ')

answer = 0

def add(x,y):
return x + y

def mult(x,y):
return x * y

def sub(x,y):
return x - y

def div(x,y):
return x / y

if operation == '+':
  answer = add(x,y)

elif operation == '-':
  answer = sub(x,y)

elif operation == '*':
  answer = mult(x,y)

elif operation == '/':
   answer = div(x,y)

else:
 print "invalid operator"

 print answer
