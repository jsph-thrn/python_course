# Locale zh_CN.UTF-8
# 2022年 06月 27日 星期一 23:32:54 CDT
# José Luis Yáñez Páez

class Arithmetic:
    """
    For executing arithmetic operations
    """

    def __init__(self, opA, opB): # dunder-init
        self.opA = opA
        self.opB = opB

    def add(self):
        return self.opA + self.opB

    def sub(self):
        return self.opA - self.opB

    def mul(self):
        return self.opA * self.opB

    def div(self):
        return self.opA / self.opB


ob1 = Arithmetic(2,3)
print(ob1.add())
print(ob1.sub())
print(ob1.mul())
print(ob1.div())
