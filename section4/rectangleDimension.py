""" 
Create int variables height and width. User must input variable values and return
using the following format
    
    Insert rectangle's height: 
    Insert rectangle's width: 
    Area: <area>
    Perimeter: <perimeter>

"""

hei: int = int(input("Insert rectangle's height: "))
wid: int = int(input("Insert rectangle's width: "))
sur: int = hei * wid
per: int = (hei + wid) * 2
print(f'Area: {sur}' )
print(f'Perimeter: {per}' )
