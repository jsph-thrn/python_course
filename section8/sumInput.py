# Locale zh_CN.UTF-8
# 2022年 06月 27日 星期一 12:15:53 CDT
# José Luis Yáñez Páez

# Create a function to sum all the numeric inputs with undefined amount of
# arguments as input parameters. Return the sum of all the inputs.

def sumInput(*inputs):
    res = 0                 # Result initialized to 0
    
    for value in inputs:    # Go through the values
        res += value        # Sum each value
    
    return res              # Return the sum

print(sumInput(1,2,3,4,5,6))

# END
