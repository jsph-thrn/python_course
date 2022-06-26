# Using a zh_CN.UTF-8 locale
# 2022年 06月 25日 星期六 22:25:51 CDT

# For cycle, also known as for each, can be used to iterate data in a data array
# Such as a character string. Data in arrays are stored with id or indexes starting
# at position 0.

# i.e. "Holland":
# str       H   o   l   l   a   n   d
# index:    0   1   2   3   4   5   6
# for index in dataArray:

myStr = 'Holland'
id = 0
for i in myStr:
    print(f'Char: {i}, id: {id}')
    id +=1
else:
    print('End for cycle')

# break reserved word can be used to interrumpt a cycle (for or while). For example,
# Stopping the cycle when a letter l is found.

for i in myStr:
    print(f'Char: {i}')
    if i == 'l':
        print(f'Letter {i} found. Stopping cycle...')
        break
    
    # this if has no else code
    
else:
    print('Letter l not found.')

# continue word is used to skip a code block left within a cycle and start the next 
# iteration.

# range() is a function to return a continuous integer range starting from 0. The int
# defined as argument is the quantity of integers within the range.
# i.e. range(8) will return an array containing integers from 0 to 7.

# Example, printing even numbers in within a range:

# for i in range(6):
#   if i % 2 == 0:
#       print(f'Value: {i}')

for i in range(6):
    if i % 2 != 0:  # if i is odd
        continue    # skip code and go to the next iteration
    print(f'Value: {i}')
