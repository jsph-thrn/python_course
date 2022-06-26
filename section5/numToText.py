myNum = int(input('Insert a number between 1 and 3: '))

# Best practice to declare the variable out of if function

myText = ''

if myNum == 1:
    myText = 'Number one'
elif myNum == 2:
    myText = 'Number two'
elif myNum == 3:
    myText = 'Number three'
else:
    myText = 'Out of range'

print(f'Input received: {myNum} - {myText}')
