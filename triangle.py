import math
"""
Output for T:
Triangle: Triangle(A(5,30), B(27,43), C(18,8))
Area: 326.5
Perimeter: 87.25
Longest Side: 36.14
Classify by Side Length: Isosceles
Is Right Triangle: True
Centroid: (16.67, 27.0)

Output for RT:
Triangle: Triangle(A(0,0), B(3,0), C(0,4))
Area: 6.0
Perimeter: 12.0
Longest Side: 5.0
Classify by Side Length: Scalene
Is Right Triangle: True
Centroid: (1.0, 1.33)
0
0.9272952180016123
0.6435011087932844
"""
# !!!!!READ ME!!!!!!
# Do not input your data points as tuples!
# A(0,0) B(3,0), C(0,4) is put in as RT = Right(0,0,3,0,0,4)
# Input consecutively


class Triangle(object):

    def __init__(self, Ax, Ay, Bx, By, Cx, Cy):
        self.Ax = Ax
        self.Ay = Ay
        self.Bx = Bx
        self.By = By
        self.Cx = Cx
        self.Cy = Cy
        self.AB = math.sqrt((self.Bx - self.Ax) ** 2 + (self.By - self.Ay) ** 2)
        self.AC = math.sqrt((self.Cx - self.Ax) ** 2 + (self.Cy - self.Ay) ** 2)
        self.BC = math.sqrt((self.Cx - self.Bx) ** 2 + (self.Cy - self.By) ** 2)

    def __str__(self):
        return "Triangle: Triangle(A({},{}), B({},{}), C({},{}))".format(self.Ax, self.Ay, self.Bx, self.By, self.Cx, self.Cy)

    def Area(self):
        S = ((self.AB + self.AC + self.BC) / 2)
        area = round(math.sqrt(S * ((S - self.AB) * (S - self.AC) * (S - self.BC))), 2)
        return "Area: " + str(area)

    def Perimeter(self):
        return "Perimeter: " + str(round((self.AB + self.AC + self.BC), 2))

    def LongestSide(self):
        return "Longest Side: " + str(round(max(self.AB, self.AC, self.BC), 2))

    def ClassifyBySideLength(self):
        if self.AB == self.BC == self.AC:
            return "Classify by Side Length: Equilateral"
        elif self.AB == self.BC or self.AB == self.AC or self.BC == self.AC:
            return "Classify by Side Length: Isosceles"
        else:
            return "Classify by Side Length: Scalene"

    def IsRightTriangle(self):
        a = min(self.AB, self.AC, self.BC)
        c = max(self.AB, self.AC, self.BC)
        b = self.AB + self.AC + self.BC - a - c
        if round(math.sqrt(a ** 2 + b ** 2), 4) == round(c, 4):
            return "Is Right Triangle: True"
        else:
            return "Is Right Triangle: False"

    def Centroid(self):
        x = round((self.Ax + self.Bx + self.Cx)/3, 2)
        y = round((self.Ay + self.By + self.Cy)/3, 2)
        return "Centroid: ({}, {})".format(x, y)


class Right(Triangle):
    def __init__(self, Ax, Ay, Bx, By, Cx, Cy):
        super().__init__(Ax, Ay, Bx, By, Cx, Cy)
        self.AB = math.sqrt((self.Bx - self.Ax) ** 2 + (self.By - self.Ay) ** 2)
        self.AC = math.sqrt((self.Cx - self.Ax) ** 2 + (self.Cy - self.Ay) ** 2)
        self.BC = math.sqrt((self.Cx - self.Bx) ** 2 + (self.Cy - self.By) ** 2)

    def Sin(self, other):
        hyp = max(self.AB, self.AC, self.BC)
        if other == 'A':
            return math.asin(self.BC/hyp)
        elif other == 'B':
            return math.asin(self.AC/hyp)
        else:
            return math.asin(self.AB/hyp)

    def Cos(self, other):
        hyp = max(self.AB, self.AC, self.BC)
        if other == 'A':
            if self.BC == hyp:
                return 0
            elif self.AC == min(self.AB, self.AC, self.BC):
                return math.acos(self.AC/hyp)
            else:
                return math.acos(self.AB/hyp)
        elif other == 'B':
            if self.AC == hyp:
                return 0
            elif self.AB == min(self.AB, self.AC, self.BC):
                return math.acos(self.AB/hyp)
            else:
                return math.acos(self.BC/hyp)
        else:
            if self.AB == hyp:
                return 0
            elif self.BC == min(self.AB, self.AC, self.BC):
                return math.acos(self.BC / hyp)
            else:
                return math.acos(self.AC / hyp)

    def Tan(self, other):
        hyp = max(self.AB, self.AC, self.BC)
        if hyp == self.BC:
            if other == 'A':
                return "Undefined"
            elif other == 'B':
                return math.atan(self.AC / self.AB)
            else:
                return math.atan(self.AB / self.AC)

        elif hyp == self.AB:
            if other == 'C':
                return "Undefined"
            elif other == 'B':
                return math.atan(self.AC / self.BC)
            else:
                return math.atan(self.BC / self.AC)
        else:
            if other == 'B':
                return "Undefined"
            elif other == 'A':
                return math.atan(self.BC / self.AB)
            else:
                return math.atan(self.AB / self.BC)


def main():
    T = Triangle(5, 30, 27, 43, 18, 8)
    RT = Right(0, 0, 3, 0, 0, 4)
    print(T)
    print(T.Area())
    print(T.Perimeter())
    print(T.LongestSide())
    print(T.ClassifyBySideLength())
    print(T.IsRightTriangle())
    print(T.Centroid())
    print('\n')
    print(RT)
    print(RT.Area())
    print(RT.Perimeter())
    print(RT.LongestSide())
    print(RT.ClassifyBySideLength())
    print(RT.IsRightTriangle())
    print(RT.Centroid())
    print(RT.Cos('A'))
    print(RT.Sin('B'))
    print(RT.Tan('C'))


main()




