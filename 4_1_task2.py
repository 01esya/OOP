import math


class Triangle:
    def __init__(self):
        self.sides = [0, 0, 0]  # Стороны треугольника
        self.angles = [0, 0, 0]  # Углы треугольника

    def read(self):
        print("Введите длины сторон треугольника:")
        for i in range(3):
            self.sides[i] = int(input(f"Сторона {i + 1}: "))

        print("Введите углы треугольника (в градусах):")
        for i in range(3):
            self.angles[i] = int(input(f"Угол {i + 1}: "))

    def display(self):
        print("Стороны треугольника:", self.sides)
        print("Углы треугольника:", self.angles)

    def perimeter(self):
        return sum(self.sides)

    def area(self):
        # Используем формулу Герона для вычисления площади
        s = self.perimeter() / 2
        area = math.sqrt(s * (s - self.sides[0]) * (s - self.sides[1]) * (s - self.sides[2]))
        return round(area)

    def heights(self):
        # Высота по каждой стороне
        area = self.area()
        heights = [round(2 * area / side) for side in self.sides]  # Округление высот до целых чисел
        return heights

    def triangle_type(self):
        a, b, c = self.sides
        if a == b == c:
            return "Равносторонний"
        elif a == b or b == c or a == c:
            return "Равнобедренный"
        elif (a ** 2 + b ** 2 == c ** 2) or (a ** 2 + c ** 2 == b ** 2) or (b ** 2 + c ** 2 == a ** 2):
            return "Прямоугольный"
        else:
            return "Разносторонний"


if __name__ == '__main__':
    triangle = Triangle()
    triangle.read()
    triangle.display()

    print("Периметр треугольника:", triangle.perimeter())
    print("Площадь треугольника:", triangle.area())
    print("Высоты треугольника:", triangle.heights())
    print("Вид треугольника:", triangle.triangle_type())
