# Using zh_CN.UTF-8 locale
# 2022年 06月 27日 星期一 02:21:17 UTC
# José Luis Yáñez Páez

# In python, [] (square brakets) are used to declare a list or array of data.
# Elements are separated with , (commas).

# Declaring a list with string data.

myNames = ['John', 'Karla', 'Richard', 'Maria']

# Index:    0       1           2       3
# Negative: -4      -3          -2      -1

print(myNames[2])   # Pull a specific element of a list, printing 'Richard'

print(myNames[-3])  # Using negative index, printing 'Karla'

print(myNames[0:2]) # Print a range within the list (indiexes 0-1)
                    # Lastly specified index is not included

print(myNames[:3])  # Include all elements which are before the specified
                    # element.

print(myNames[1:])  # Specify a starting point, get all the elementes that
                    # are after the starting point.

myNames[3] = 'Ivone' # Change the value of a specified element.

print(myNames)

for i in myNames:   # Going through the list
    print(i)
else:
    print('No more names in the list')

# len() is used to get the length of the list (number of elements).

print(len(myNames)) # Printing the length

# myList.append(<newElement>) can be used to add a new element after the
# last one.

myNames.append('Lorenz')
print(myNames)

# myList.insert(index, <newElement>) is used to insert a new element in a
# desired position. Elements after the new element move to the right.

myNames.insert(1, 'Octavie') # Octavie gets the 1 index, Karla 2 and so on.
print(myNames)

# myList.remove(<element>) removes an specified element, not index. Elements
# after the removed element move to the left.

myNames.remove('Octavie')   # Karla gets the 1 index again.
print(myNames)

# myList.pop() removes the last element of the list (default behaviour if no
# arguments specified).

myNames.pop()   # Removed Lorenz
print(myNames) 

del myNames[0]  # Same function as myList.remove() but by inserting an index.
print(myNames)

# myList.clear() removes all the elements of the list.

myNames.clear()
print(myNames)  # Console input should be "[]" (a void list).

del myNames     # del deletes a variable from memory. In this case, the whole list

# print(myNames) now returns an error

# END
