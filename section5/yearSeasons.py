# 25/06/2022

myMonth = int(input('Insert month of the year (1-12): '))

# None is equivalent to 'null' in other programming languages.

mySeason = None

if myMonth == 1 or myMonth == 2 or myMonth == 12:
    mySeason = 'Winter'
elif 5 >= myMonth >= 3:
    mySeason = 'Spring'
elif 8 >= myMonth >= 6:
    mySeason = 'Summer'
elif 11 >= myMonth >=9:
    mySeason = 'Autumn'
else:
    mySeason = 'not existent'

print(f'For month {myMonth}, the season of the year is {mySeason}')
