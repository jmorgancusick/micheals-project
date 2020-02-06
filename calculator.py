print 'Welcome to my calculator!'

x = raw_input('Enter your first number: ')
y = raw_input('Enter your second number: ')

operation = raw_input('Enter your operation (+-*/): ')

answer = 0

if operation == '+':
    answer = x + y


print answer
