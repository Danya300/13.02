import numpy as np
import matplotlib.pyplot as plt

class Vector3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def length(self):
        return np.sqrt(self.x**2 + self.y**2 + self.z**2)

    def dot_product(self, other):
        return self.x*other.x + self.y*other.y + self.z*other.z

    def cross_product(self, other):
        return Vector3D(self.y*other.z - self.z*other.y,
                        self.z*other.x - self.x*other.z,
                        self.x*other.y - self.y*other.x)

    def angle_cosine(self, other):
        dot = self.dot_product(other)
        return dot / (self.length() * other.length())

    def __add__(self, other):
        return Vector3D(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Vector3D(self.x - other.x, self.y - other.y, self.z - other.z)

    @staticmethod
    def random_vectors(N):
        return [Vector3D(np.random.rand(), np.random.rand(), np.random.rand()) for _ in range(N)]

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"

# Пример использования класса
v1 = Vector3D(1, 2, 3)
v2 = Vector3D(4, 5, 6)

print("Длина вектора v1:", v1.length())
print("Скалярное произведение v1 и v2:", v1.dot_product(v2))
print("Векторное произведение v1 и v2:", v1.cross_product(v2))
print("Косинус угла между v1 и v2:", v1.angle_cosine(v2))
print("Сумма векторов v1 и v2:", v1 + v2)
print("Разность векторов v1 и v2:", v1 - v2)

# Создание массива случайных векторов и их визуализация
random_vectors = Vector3D.random_vectors(10)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
for vec in random_vectors:
    ax.quiver(0, 0, 0, vec.x, vec.y, vec.z)
ax.set_xlim([0, 1])
ax.set_ylim([0, 1])
ax.set_zlim([0, 1])
plt.show()
