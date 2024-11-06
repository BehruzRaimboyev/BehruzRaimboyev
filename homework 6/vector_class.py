import math

class Vector:
    def __init__(self, *components):
        self.components = list(components)
    
    def __repr__(self):
        return f"Vector({', '.join(map(str, self.components))})"
    
    def __str__(self):
        return f"({', '.join(map(str, self.components))})"
    
    def __len__(self):
        return len(self.components)
    
    def __add__(self, other):
        if len(self) != len(other):
            raise ValueError("Vectors must have the same dimension for addition.")
        return Vector(*[a + b for a, b in zip(self.components, other.components)])
    
    def __sub__(self, other):
        if len(self) != len(other):
            raise ValueError("Vectors must have the same dimension for subtraction.")
        return Vector(*[a - b for a, b in zip(self.components, other.components)])
    
    def __mul__(self, scalar):
        return Vector(*[a * scalar for a in self.components])
    
    def __rmul__(self, scalar):
        return self.__mul__(scalar)
    
    def __truediv__(self, scalar):
        if scalar == 0:
            raise ValueError("Cannot divide by zero.")
        return Vector(*[a / scalar for a in self.components])
    
    def __eq__(self, other):
        return self.components == other.components
    
    def dot(self, other):
        if len(self) != len(other):
            raise ValueError("Vectors must have the same dimension for dot product.")
        return sum(a * b for a, b in zip(self.components, other.components))
    
    def magnitude(self):
        return math.sqrt(sum(x ** 2 for x in self.components))
    
    def normalize(self):
        mag = self.magnitude()
        if mag == 0:
            raise ValueError("Cannot normalize a zero vector.")
        return self * (1 / mag)
    
    def __bool__(self):
        return any(c != 0 for c in self.components)

    def __getitem__(self, index):
        return self.components[index]
    
    def __setitem__(self, index, value):
        self.components[index] = value
    
    def __delitem__(self, index):
        del self.components[index]

    def __abs__(self):
        return self.magnitude()
    
    def __neg__(self):
        return Vector(*[-x for x in self.components])
    
    def scale(self, scalar):
        return Vector(*[x * scalar for x in self.components])

v1 = Vector(1, 4, 6)
          

v2 = Vector(3, 7, 2)
b=v1 + v2                
a=v1 - v2               
c=v1 * v2  
print(b)
print(a)
print(c)
             
                