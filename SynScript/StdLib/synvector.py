"""
SynScript Standard Library - Vector Module
2D ve 3D vektör işlemleri
"""

import math as _math

class Vector2:
    """2D vektör"""
    
    def __init__(self, x: float = 0.0, y: float = 0.0):
        self.x = x
        self.y = y
    
    def length(self) -> float:
        """Vektörün uzunluğu"""
        return _math.sqrt(self.x ** 2 + self.y ** 2)
    
    def normalized(self) -> 'Vector2':
        """Normalleştirilmiş vektör"""
        length = self.length()
        if length == 0:
            return Vector2(0, 0)
        return Vector2(self.x / length, self.y / length)
    
    def dot(self, other: 'Vector2') -> float:
        """Nokta çarpım"""
        return self.x * other.x + self.y * other.y
    
    def distance_to(self, other: 'Vector2') -> float:
        """Başka bir vektöre olan mesafe"""
        dx = self.x - other.x
        dy = self.y - other.y
        return _math.sqrt(dx ** 2 + dy ** 2)
    
    def angle_to(self, other: 'Vector2') -> float:
        """Başka bir vektöre olan açı (radyan)"""
        return _math.atan2(other.y - self.y, other.x - self.x)
    
    def lerp(self, other: 'Vector2', t: float) -> 'Vector2':
        """Doğrusal interpolasyon"""
        return Vector2(
            self.x + (other.x - self.x) * t,
            self.y + (other.y - self.y) * t
        )
    
    def __add__(self, other: 'Vector2') -> 'Vector2':
        return Vector2(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other: 'Vector2') -> 'Vector2':
        return Vector2(self.x - other.x, self.y - other.y)
    
    def __mul__(self, scalar: float) -> 'Vector2':
        return Vector2(self.x * scalar, self.y * scalar)
    
    def __truediv__(self, scalar: float) -> 'Vector2':
        return Vector2(self.x / scalar, self.y / scalar)
    
    def __repr__(self) -> str:
        return f"Vector2({self.x}, {self.y})"


class Vector3:
    """3D vektör"""
    
    def __init__(self, x: float = 0.0, y: float = 0.0, z: float = 0.0):
        self.x = x
        self.y = y
        self.z = z
    
    def length(self) -> float:
        """Vektörün uzunluğu"""
        return _math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)
    
    def normalized(self) -> 'Vector3':
        """Normalleştirilmiş vektör"""
        length = self.length()
        if length == 0:
            return Vector3(0, 0, 0)
        return Vector3(self.x / length, self.y / length, self.z / length)
    
    def dot(self, other: 'Vector3') -> float:
        """Nokta çarpım"""
        return self.x * other.x + self.y * other.y + self.z * other.z
    
    def cross(self, other: 'Vector3') -> 'Vector3':
        """Çapraz çarpım"""
        return Vector3(
            self.y * other.z - self.z * other.y,
            self.z * other.x - self.x * other.z,
            self.x * other.y - self.y * other.x
        )
    
    def distance_to(self, other: 'Vector3') -> float:
        """Başka bir vektöre olan mesafe"""
        dx = self.x - other.x
        dy = self.y - other.y
        dz = self.z - other.z
        return _math.sqrt(dx ** 2 + dy ** 2 + dz ** 2)
    
    def __add__(self, other: 'Vector3') -> 'Vector3':
        return Vector3(self.x + other.x, self.y + other.y, self.z + other.z)
    
    def __sub__(self, other: 'Vector3') -> 'Vector3':
        return Vector3(self.x - other.x, self.y - other.y, self.z - other.z)
    
    def __mul__(self, scalar: float) -> 'Vector3':
        return Vector3(self.x * scalar, self.y * scalar, self.z * scalar)
    
    def __truediv__(self, scalar: float) -> 'Vector3':
        return Vector3(self.x / scalar, self.y / scalar, self.z / scalar)
    
    def __repr__(self) -> str:
        return f"Vector3({self.x}, {self.y}, {self.z})"
