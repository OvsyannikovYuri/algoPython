#  По введенным пользователем координатам двух точек вывести уравнение прямой вида y = kx + b, проходящей через эти точки.

point_A_x = float(input("введите значение абциссы координаты точки 1"))
point_A_y = float(input("введите значение ординаты координаты точки 1"))
point_B_x = float(input("введите значение абциссы координаты точки 2"))
point_B_y = float(input("введите значение ординаты координаты точки 2"))
print(point_A_x,point_A_y)
print(point_B_x,point_B_y)
k_koef = (point_A_y - point_B_y)/(point_B_x - point_A_x)
b_koef = (point_A_x*point_B_y - point_B_x*point_A_y)/(point_B_x-point_A_x)
print("y =",round(k_koef,2), "x  +",round(b_koef,2))