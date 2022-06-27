# Locale zh_CN.UTF-8
# 2022年 06月 27日 星期一 17:28:49 CDT
# José Luis Yáñez Páez

# Temp Convert

def relIntToRelUS(c):
    return 32 + 1.8 * c

def relUSToRelInt(f):
    return (f - 32) / 1.8

myTemp = float(input('Insert the temperature: '))
mySys = input('Which system? ')

if mySys == 'F' or mySys == 'f' or mySys == 'fahrenheit' or mySys == 'Fahrenheit' or mySys == 'us' or mySys == 'US':
    newTemp = relUSToRelInt(myTemp)
    print(f'{myTemp} °F equals to {newTemp:.2f} °C')    # .2f for two decimals
elif mySys == 'C' or mySys == 'c' or mySys == 'Celsius' or mySys == 'celsius' or mySys == 'International' or mySys == 'international':
    newTemp = relIntToRelUS(myTemp)
    print(f'{myTemp} °C equals to {newTemp:.2f} °F')
else:
    print('System not recognized!')
