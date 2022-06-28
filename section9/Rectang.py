# Locale zh_CN.UTF-8
# 2022年 06月 27日 星期一 23:44:26 CDT
# José Luis Yáñez Páez

class Rectang:

    def __init__(self, base, height): # init method
        self.base = base
        self.height = height

    def calcSurface(self):
        return self.base * self.height

b = float(input("Enter rectangle's base: "))
h = float(input("Enter rectangle's height: "))

newRectang = Rectang(b,h)

print(f'Rectangle surface: {newRectang.calcSurface()}')

