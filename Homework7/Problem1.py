class Vector3D:

    def __init__(self, x, y, z):

        self.x = x
        self.y = y
        self.z = z

    def __add__(self,other):
        return (self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self,other):
        return (self.x - other.x, self.y - other.y, self.z - other.z)

    def scalmult(self):
        return (3*self.x, 3*self.y, 3*self.z)

    def dotproduct(self,other):
        dotproduct = 0.
        dotproduct += self.x*other.x
        dotproduct += self.y*other.y
        dotproduct += self.z*other.z
        return dotproduct

    def normvector(self):
        return(self.x**2 + self.y**2 + self.z**2)**0.5

v1 = Vector3D(1,2,3)
v2 = Vector3D(3,2,1)

print(v1+v2)
print(v1-v2)
print(v1.scalmult())
print(v2.scalmult())
print(v1.dotproduct(v2))
print(v1.normvector())
print(v2.normvector())

