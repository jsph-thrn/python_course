# Locale zh_CN.UTF-8
# 2022年 06月 27日 星期一 23:57:50 CDT
# José Luis Yáñez Páez

# Cube volume

class Cube:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def calcVolume(self):
        return self.x * self.y * self.z

x = float(input('Enter the width of the cube: '))
y = float(input('Enter the height of the cube: '))
z = float(input('Enter the thickness of the cube: '))

myNewCube = Cube(x,y,z)

print(f'Cube volume: {myNewCube.calcVolume()} cubic units')
