# Locale zh_CN.UTF-8
# 2022年 06月 27日 星期一 10:38:05 CDT
# José Luis Yáñez Páez

# Dictionaries is a bidimensional collection which consist in a key and a
# corresponding element. Has no order but contents can be modified.

myDict = {      # Multiple pairs of keys and elements

        'IDE':'Integrated Development Environment',     # Key:Element
        'OOP':'Object Oriented Programming',
        'DBMS':'Database Management System'
}
print(myDict)
print(len(myDict))          # len() can be used as well.
print(myDict['IDE'])        # Returns the element that corresponds to the key
print(myDict.get('OOP'))    # Same function as the previous line.
myDict['IDE'] = 'integrated development environment'    # Modify an element
print(myDict)

for i in myDict:      # Returns just the keys by default
    print(i)

for i, v in myDict.items(): # items is used to return corresponding key and 
                            # and element respectively.
    print(i,v)

for i in myDict.keys():     # Returns keys only
    print(i)

for i in myDict.values():   # Returns the element corresponding to the key
    print(i)

print('IDE' in myDict)      # Looks for the existent of a element with
                            # specified key

myDict['PK'] = 'Primary Key'  # Insert a new element with given key

myDict.pop('DBMS')          # Removes the entry with given key
print(myDict)

myDict.clear()              # Same as previous reviewed collections.
print(myDict)

del myDict                  # deletes dictionary

# print(myDict) returns error now

# END
