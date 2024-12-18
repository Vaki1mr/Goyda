class Vector:
    def __init__(self, x=0, y=0, z=0):
        if isinstance(x, str):
            x = x.strip('{}').split(',')
            assert len(x) == 3, "Строка должна содержать три компонента."
            self.x, self.y, self.z = map(float, x)
        else:
            self.x = float(x)
            self.y = float(y)
            self.z = float(z)

        assert all(isinstance(i, (int, float)) for i in (self.x, self.y, self.z)), "Компоненты должны быть числами."

    def abs(self):
        return (self.x ** 2 + self.y ** 2 + self.z ** 2) ** 0.5

    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y, self.z + other.z)
        raise TypeError("Можно складывать только с другим вектором.")

    def __sub__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y, self.z - other.z)
        raise TypeError("Можно вычитать только другой вектор.")

    def __mul__(self, other):
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y + self.z * other.z
        elif isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other, self.z * other)
        raise TypeError("Можно умножать только на другой вектор или число.")

    def __repr__(self):
        return f"Vector({self.x}, {self.y}, {self.z})"


# Пример использования:
v1 = Vector("{1, 2, 3}")
v2 = Vector(4, 5, 6)

print("Вектор v1:", v1)
print("Вектор v2:", v2)

v3 = v1 + v2
print("Сумма v1 и v2:", v3)

v4 = v1 - v2
print("Разность v1 и v2:", v4)

dot_product = v1 * v2
print("Скалярное произведение v1 и v2:", dot_product)

v5 = v1 * 2
print("Умножение v1 на 2:", v5)

print("Модуль вектора v1:", v1.abs())