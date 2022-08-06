from IdenticalNumberException import *

res = None # Declared outside try/except block. Otherwise, it wouldn't be detected by code outside the block.
e = 'No error'

try:
    a = int(input('Insert a number: '))
    b = int(input('Insert another number: '))

    if a == b:
        raise IdenticalNumberException('Identical numbers detected')
        e = 'IdenticalNumberException'

    res = a/b # ArithmeticException > DivisionByZeroException
    # except Exception as e: # handles the exception as a generic exception.
    # BaseException > Exception > ArithmeticError > ZeroDivisionError

except ZeroDivisionError as e:
    print(f'An error as occurred: DIVISION BY ZERO DETECTED.')

except TypeError as e:
    print(f'An error as ocurred: UNSUPPORTED TYPE DETECTED')

except Exception as e:
    print(f'An error as ocurred: {e}')

else: # in case no exceptions detected
    print('No errors detected.')

print(f'Result: {res}')

