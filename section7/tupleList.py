# Locale zh_CN.UTF-8
# 2022年 06月 27日 星期一 04:31:13 UTC
# José Luis Yáñez Páez

# Create a list with the numbers of the following tuple, but including only
# those that are less-than 5.

myTuple = (13,1,8,3,2,5,8)
myList = []

for i in myTuple:           # Going through the tuple
    
    if i < 5:               # Evaluate the current element
        myList.append(i)    # Append the current element to the end of the list
    
    # i += 1 is done automatically

print(myList)               # Print the final list

# END
