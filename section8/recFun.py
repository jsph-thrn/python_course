# Locale zh_CN.UTF-8
# 2022年 06月 27日 星期一 16:57:06 CDT
# José Luis Yáñez Páez

# Calculate n! with a recursive function.
# A recursive function is the one that calls itself at some point of code 
# execution.

def recFactorial(n):
    if n == 1:
        return 1
    else:
        return n * recFactorial(n - 1) # calling the function inside it
print(recFactorial(int(input('Insert a number (integer): '))))

