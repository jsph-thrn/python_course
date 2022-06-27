# Locale zh_CN.UTF-8
# 2022年 06月 27日 星期一 11:44:34 CDT
# José Luis Yáñez Páez

# Function recommended nomenclature 
    #   functionName()
    #   function_name()
# Parameters are the name of the arguments inserted into the function. It takes
# data so it would be used within the function.

# def to define a new function. if parameters were to be define here, those
# would be the default values.

# Complete (but redundant) syntaxis
# def myFuntion(a:<type> = <default value>, b:<type> = <default value>)

def myFunction(name = 'Unknown', surname= ''):  
    print(f'Greetings from myFunction(), {name} {surname}!')

myFunction('José Luis', 'Yáñez')    # inserting a name and a surname
myFunction()                        # using default parameters

# anotherFuntion()  This function wasn't defined. Error is returned

def sum(a, b):
    return a + b

# print(f'Result of sum: {sum(a, b)}')

res = sum(5,3)
print(f'Result of sum: {res}')

def listNames(*myNames):    # Undefined (variable) amount of parameters (tuple)
    for name in myNames:    
        print(name)

listNames('John', 'Karla', 'Maria', 'Ernest')
listNames('Laura', 'Carl')

def listTerms(**kwargs):    # Input a dictionary (key:value) into a function
                            # Undefined amount of pairs
    for key, value in kwargs.items(): # Get the items of a dictionary
        print(f'{key}: {value}')

listTerms(IDE='Integrated Development Environment', PK = 'Primary Key')
listTerms(DBMS='Database Management System')

# END
