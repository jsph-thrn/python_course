# Operator overload refers to the different behaviours of a specific operator, i.e., +, given some circunstances.

a = 2
b = 3
print(a + b) # + operator acts as sum operator.

a = 'Hello '
b = 'World'
print(a + b) # + operator concatenates.

a = [1, 2, 3]
b = [6, 7, 8]
print(a + b) # + operator appends list elements.

# With classes
#
# +     __add__(self, other)
# -     __sub__(self, other)
# *     __mul__(self, other)
# /     __truediv__(self, other)
# //    __floordiv__(self, other)
# %     __mod__(self, other)
# **    __pow__(self, other)
# <     __lt__(self, other)
# >     __gt__(self, other)
# <=    __le__(self, other)
# >=    __ge__(self, other)
# ==    __eq__(self, other)
# !=    __ne__(self, other)
# -=    __isub__(self, other)
# +=    __iadd__(self, other)
# *=    __imul__(self, other)
# /=    __idiv__(self, other)
# //=   __ifloordiv__(self, other)
# %=    __imod__(self, other)
# **=   __ipow__(self, other)
# UNARY OPERATORS
# -     __neg__(self, other)
# +     __pos__(self, other)
# ~     __invert__(self, other)


