# Locale zh_CN.UTF-8
# 2022年 06月 27日 星期一 09:16:58 CDT
# José Luis Yáñez Páez

# Set is a collection of data which, opposed to lists or tuples, this has no
# order within elements and it cannot store duplicated elements. Nevertheless
# It is possible add and delete elements, opposed to tuples.

myPlanets = {'Mars', 'Jupiter', 'Venus'}    # Declaring a set with {}
print(myPlanets)        # Data in a set prints in random order.
print(len(myPlanets)        # How much elements this set has
print('Marte' in myPlanets)     # To check if a element is present in a set.
myPlanets.add('Earth')      # add method to insert a new element
print(myPlanets)
myPlanets.remove('Earth')       # remove method to delete a present element.
print(myPlanets)

# If the specified element is not present in a set, remove method returns an
# error.

myPlanets.discard('Jupiters')   # Doesn't return error if element is not found.
myPlanets.clear()       # Delete all the elements in a set
print(myPlanets)
del myPlanets       # Delete this variable

# print(myPlanets) returns error.

# END
