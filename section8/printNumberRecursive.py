# Locale zh_CN.UTF-8
# 2022年 06月 27日 星期一 16:58:18 CDT
# José Luis Yáñez Páez

# Print numbers from 5 to 1 in descending order using recursive function. If
# negative numbers were to be used as parameters, don't print anything.

def printNumbers(hL):
   if hL < 1:
        return ''
    else:
        print(hL)
        printNumbers(hL - 1)
    
myNum = int(input('Insert a positive number: '))
printNumbers(myNum)
