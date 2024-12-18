class Vector:
    def __init__(self, coordinates):
        coordinates = coordinates.strip('{}')
        x, y, z = map(float, coordinates.split(','))

        self.x = x
        self.y = y
        self.z = z

    def abs(self):
        return (self.x ** 2 + self.y ** 2 + self.z ** 2) ** 0.5

    def __add__(self, other):
        return Vector(f'{{{self.x + other.x}, {self.y + other.y}, {self.z + other.z}}}')

    def __sub__(self, other):
        return Vector(f'{{{self.x - other.x}, {self.y - other.y}, {self.z - other.z}}}')

    def __mul__(self, other):
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y + self.z * other.z
        elif isinstance(other, (int, float)):
            return Vector(f'{{{self.x * other}, {self.y * other}, {self.z * other}}}')
        else:
            raise ValueError("Multiplication is only supported with another Vector or a scalar.")


# Упражнение №1.1: Нахождение координат центра масс
def center_of_mass(vectors):
    if not vectors:
        return None

    total_vector = Vector('{0, 0, 0}')
    for vec in vectors:
        total_vector += vec

    num_vectors = len(vectors)
    center = Vector(
        f'{{{total_vector.x / num_vectors}, {total_vector.y / num_vectors}, {total_vector.z / num_vectors}}}')

    return center


# Пример использования
points = ["{1, 2, 3}", "{4, 5, 6}", "{7, 8, 9}"]
vectors = [Vector(point) for point in points]
center = center_of_mass(vectors)

print(f"Координаты центра масс: {{{center.x}, {center.y}, {center.z}}}")

