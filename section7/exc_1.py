# Using a zh_CN.UTF-8 locale
# 2022年 06月 27日 星期一 03:31:42 UTC
# José Luis Yáñez Páez

myRange = range(11) # range(0,11,1) for start, end, steps

for i in myRange:   # Going through the range
    if i % 3 == 0:  # Evaluate if number is divisible by 3
        print(i)    # Printing the number
    # i += 1 is made automatically
