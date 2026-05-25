import math

class Figure:
    def dimension(self):
        raise NotImplementedError()

    def perimetr(self):
        return None

    def square(self):
        return None

    def squareSurface(self):
        return None

    def squareBase(self):
        return None

    def height(self):
        return None

    def volume(self):
        raise NotImplementedError()



class Triangle(Figure):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        if a <= 0 or b <= 0 or c <= 0 or (a + b <= c) or (a + c <= b) or (b + c <= a):
            raise ValueError("Трикутник із такими сторонами не існує")

    def dimension(self):
        return "двовимірна"

    def perimetr(self):
        return self.a + self.b + self.c

    def square(self):
        p = self.perimetr() / 2
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))

    def volume(self):
        return self.square()


class Rectangle(Figure):
    def __init__(self, a, b):
        self.a = a
        self.b = b
        if a <= 0 or b <= 0:
            raise ValueError("Сторони мають бути додатними")

    def dimension(self):
        return "двовимірна"

    def perimetr(self):
        return 2 * (self.a + self.b)

    def square(self):
        return self.a * self.b

    def volume(self):
        return self.square()


class Trapeze(Figure):
    def __init__(self, a, b, c, d):
        self.a = a  # Основа 1
        self.b = b  # Основа 2
        self.c = c  # Бічна 1
        self.d = d  # Бічна 2
        if a <= 0 or b <= 0 or c <= 0 or d <= 0 or a == b:
            raise ValueError("Некоректні параметри трапеції")

    def dimension(self):
        return "двовимірна"

    def perimetr(self):
        return self.a + self.b + self.c + self.d

    def square(self):
        try:
            num = (-self.a + self.b + self.c + self.d) * (self.a - self.b + self.c + self.d) * \
                  (self.a - self.b + self.c - self.d) * (self.a - self.b - self.c + self.d)
            if num < 0: raise ValueError
            h = math.sqrt(num) / (2 * abs(self.a - self.b))
            return ((self.a + self.b) / 2) * h
        except:
            raise ValueError("Трапеція не існує")

    def volume(self):
        return self.square()


class Parallelogram(Figure):
    def __init__(self, a, b, h):
        self.a = a
        self.b = b
        self.h = h
        if a <= 0 or b <= 0 or h <= 0 or h > b:
            raise ValueError("Некоректні параметри паралелограма")

    def dimension(self):
        return "двовимірна"

    def perimetr(self):
        return 2 * (self.a + self.b)

    def square(self):
        return self.a * self.h

    def volume(self):
        return self.square()


class Circle(Figure):
    def __init__(self, r):
        self.r = r
        if r <= 0:
            raise ValueError("Радіус має бути додатним")

    def dimension(self):
        return "двовимірна"

    def perimetr(self):
        return 2 * math.pi * self.r

    def square(self):
        return math.pi * (self.r ** 2)

    def volume(self):
        return self.square()




class Ball(Figure):
    def __init__(self, r):
        self.r = r
        if r <= 0:
            raise ValueError("Радіус має бути додатним")

    def dimension(self):
        return "тривимірна"

    def volume(self):
        return (4 / 3) * math.pi * (self.r ** 3)


class TriangularPyramid(Triangle):
    def __init__(self, a, h_pyramid):
        super().__init__(a, a, a)
        self._h = h_pyramid
        if h_pyramid <= 0:
            raise ValueError("Висота має бути додатною")

    def dimension(self):
        return "тривимірна"

    def squareBase(self):
        return super().square()

    def height(self):
        return self._h

    def volume(self):
        return (1 / 3) * self.squareBase() * self._h


class QuadrangularPyramid(Rectangle):
    def __init__(self, a, b, h_pyramid):
        super().__init__(a, b)
        self._h = h_pyramid
        if h_pyramid <= 0:
            raise ValueError("Висота має бути додатною")

    def dimension(self):
        return "тривимірна"

    def squareBase(self):
        return super().square()

    def height(self):
        return self._h

    def volume(self):
        return (1 / 3) * self.squareBase() * self._h


class RectangularParallelepiped(Rectangle):
    def __init__(self, a, b, c):
        super().__init__(a, b)
        self.c = c
        if c <= 0:
            raise ValueError("Третє ребро має бути додатним")

    def dimension(self):
        return "тривимірна"

    def squareBase(self):
        return super().square()

    def height(self):
        return self.c

    def volume(self):
        return self.squareBase() * self.c


class Cone(Circle):
    def __init__(self, r, h):
        super().__init__(r)
        self._h = h
        if h <= 0:
            raise ValueError("Висота має бути додатною")

    def dimension(self):
        return "тривимірна"

    def squareBase(self):
        return super().square()

    def height(self):
        return self._h

    def volume(self):
        return (1 / 3) * self.squareBase() * self._h


class TriangularPrism(Triangle):
    def __init__(self, a, b, c, h):
        super().__init__(a, b, c)
        self._h = h
        if h <= 0:
            raise ValueError("Висота має бути додатною")

    def dimension(self):
        return "тривимірна"

    def squareBase(self):
        return super().square()

    def height(self):
        return self._h

    def volume(self):
        return self.squareBase() * self._h