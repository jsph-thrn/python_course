# Locale zh_CN.UTF-8
# 2022年 06月 27日 星期一 16:16:12 CDT
# José Luis Yáñez Páez

# Create a function to multiply all the numeric inputs with undefined amount of
# arguments as input parameters. Return the product of multiplication of all the 
# inputs.

def mulInput(*inputs):
    res = 1                 # Result initialized to 1
    
    for value in inputs:    # Go through the values
        res *= value        # Multiply each value
    
    return res              # Return the product

print(mulInput(1,2,3,4,5,6))

# END
