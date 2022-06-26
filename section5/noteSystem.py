# 25/06/2022

# User must insert a numeric note (1-10). This script must convert
# numeric note to letter note as follows
#   A: greater-than or equal to 9 and less-than or equal to 10
#   B: greater-than or equal to 8 and less-than 9
#   C: greater-than or equal to 7 and less-than 8
#   D: greater-than or equal to 6 and less-than 7
#   F: greather than or equal to 0 and less-than 6
#   Any other value must return: invalid value

myNote = int(input('Insert a numeric note (1-10): '))

if 10 >= myNote >= 9:
    print('Note: A')
elif 9 > myNote >= 8:
    print('Note: B')
elif 8 > myNote >= 7:
    print('Note: C')
elif 7 > myNote >= 6:
    print('Note: D')
elif 6 > myNote >= 0:
    print('Note: F')
else:
    print('Invalid value')


