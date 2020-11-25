import math

print("Эта программа находит точки пересечения прямой и сферы. Координаты необходимо вводить через пробел (Пример: x y z).")
print("Начало отрезка:")
startOfTheSegment = input().split(" ")
print("Конец отрезка:")
endtOfTheSegment = input().split(" ")
print("Центр окружности:")
centerOfTheSphere = input().split(" ")
print("Радиус окружности:")
sphereRadius = float(input())

def FindTheIntersectionPoints(startOfTheSegment, endtOfTheSegment, centerOfTheSphere, sphereRadius):
    differenceX = float(endtOfTheSegment[0]) - float(startOfTheSegment[0])
    differenceY = float(endtOfTheSegment[1]) - float(startOfTheSegment[1])
    differenceZ = float(endtOfTheSegment[2]) - float(startOfTheSegment[2])

    differenceX2 = float(startOfTheSegment[0]) - float(centerOfTheSphere[0])
    differenceY2 = float(startOfTheSegment[1]) - float(centerOfTheSphere[1])
    differenceZ2 = float(startOfTheSegment[2]) - float(centerOfTheSphere[2])

    productOfDifferences1 = differenceX * differenceX2
    productOfDifferences2 = differenceY * differenceY2
    productOfDifferences3 = differenceZ * differenceZ2

    sumOfSquares1 = pow(differenceX,2) + pow(differenceY,2) + pow(differenceZ,2)
    sumOfSquares2 = pow(differenceX2,2) + pow(differenceY2,2) + pow(differenceZ2,2)

    discriminant = pow((2 * (productOfDifferences1 + productOfDifferences2 + productOfDifferences3)), 2) - (4 * sumOfSquares1 * (sumOfSquares2 - pow(sphereRadius,2)))
    if discriminant < 0: return "Коллизий не найдено"
    else:
        rootOfTheDiscriminant = math.sqrt(discriminant)

        t1 = (-2 * (productOfDifferences1 + productOfDifferences2 + productOfDifferences3) + rootOfTheDiscriminant) / (2*sumOfSquares1)
        t2 = (-2 * (productOfDifferences1 + productOfDifferences2 + productOfDifferences3) - rootOfTheDiscriminant) / (2*sumOfSquares1)

        X1 = t1*(differenceX) + float(endtOfTheSegment[0])
        Y1 = t1*(differenceY) + float(endtOfTheSegment[1])
        Z1 = t1*(differenceZ) + float(endtOfTheSegment[2])
        str1 = X1, Y1, Z1

        X2 = t2*(differenceX) + float(endtOfTheSegment[0])
        Y2 = t2*(differenceY) + float(endtOfTheSegment[1])
        Z2 = t2*(differenceZ) + float(endtOfTheSegment[2])
        str2 = X2, Y2, Z2

        return str1 and str2

print("Прямая пересекается со сферой в точках: ")
print(FindTheIntersectionPoints(startOfTheSegment, endtOfTheSegment, centerOfTheSphere, sphereRadius))