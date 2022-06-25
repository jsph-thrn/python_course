myAge = int(input("Insert your age: "))
"""

inTwenties = myAge >= 20 and myAge < 30
inThirties = myAge >= 30 and myAge < 40
if inTwenties or inThirties:

"""    

# if (myAge >= 20 and myAge < 30) or (myAge >= 30 and myAge < 40):

if (20 <= myAge < 30) or (30 <= myAge < 40):
    print(f"Your age, {myAge}, is within range.")
    
    # if inTwenties:
    
    # if myAge >= 20 and myAge < 30:
    
    if 20 <= myAge < 30:

        """

        \ backslash is used to make an escape sequence so special caracters are pointed
        thus, while using '' to state the argument of the function, the ' doesn't close
        the argument.

        """
       
        print('Within 20\'s')

    # elif is used to state other case than the main case and the else case within a if.

    # elif inThirties:
    
    # elif (myAge <= 30 and myAge < 40):

    elif 30 <= myAge < 40:
        print('Within 30\'s')
    else:
        print('Out of range.')
else:
    print(f"Your age, {myAge}, is out of range.")

