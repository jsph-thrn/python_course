# Locale zh_CN.UTF-8
# 2022年 06月 27日 星期一 04:06:50 UTC
# José Luis Yáñez Páez

# Tuples are similar to lists but elements cannot be modified or deleted.

myFruits = ('Orange', 'Banana', 'Guava') # Using () to declare instead of []
print(myFruits)

print(len(myFruits))        # Print the number of elements inside the tuple.
print(myFruits[0])          # Access a specific element.
print(myFruits[-1])         # Inverse navigation (in this case, index 2).
print(myFruits[0:2])        # Access a range (0-1) 

# If a tuple will have just one element, it should be declared as:

anotherFruit = ('Pear',)    # Adding a comma at the end
print(anotherFruit)

# EXTRA: to avoid line break in print function, set a end value:

for i in myFruits:
    print(i, end=' ')       # default value is "end='\n'". Check documentation.

# It is possible to modify a tuple but it should be done as follows:

fruitList = list(myFruits)  # list() gets a list from a tuple
fruitList[0] = 'Pear'       # Modifying an element in the list variable.
myFruits = tuple(fruitList) # Reassigning elements to the tuple.
print('\n',myFruits)        # Adding a line break because of the last print().

# However, this is not recommended as list variables already exists.

del myFruits                # delete tuple enterely

# print(myFruits) should return error now.

# END
