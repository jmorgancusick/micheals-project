print 'Welcome to my calculator!'

x = raw_input('Enter your first number: ')
y = raw_input('Enter your second number: ')

operation = raw_input('Enter your operation (+-*/): ')

answer = 0

if operation == '+':
    answer = float(x) + float(y)

elif operation == '-':
    answer = float(x) - float(y)

elif operation == '/':
    answer = float(x) / float(y)

elif operation == '*':
    answer = float(x) * float(y)
else:
	print "invalid operation"

int_answer = answer - int(answer)
if int_answer == 0:
	print int(answer)

else:
	print float(answer)
