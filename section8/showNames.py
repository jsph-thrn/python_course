# Locale zh_CN.UTF-8
# 2022年 06月 27日 星期一 16:30:44 CDT
# José Luis Yáñez Páez

def showNames(myNames): 
    for name in myNames:
        print(name)

myNames = ['John', 'Karla', 'Maxime']
showNames(myNames)
showNames('Carl') # strings are list of characters
# showNames(10) would return an error because int is not iterable
# showNames(10,11)  in this case, arguments are recognized as two different
#                   parameters.

showNames((10,11))  # tuples are iterable
showNames([10,11])  # lists are iterable

# END

