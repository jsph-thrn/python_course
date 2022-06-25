num = int(input("Insert a value between 0 and 5: "))
minValue = 0
maxValue = 5
isValid = num >= minValue and num <= maxValue
if isValid:
    print(f'Value {num} is within range.')
else:
    print(f'Value {num} is out of range.')
