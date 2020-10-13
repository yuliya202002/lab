def read_int_variable(variable_name):
    variable = 0
    while True:
        variable_str = input("Введите " + variable_name + ": ")
        if variable_str.isdigit():
            variable = int(variable_str)
            break
        else:
            print("Ввёдённое значение не является целым числом")
            continue
    return variable
import math
k1 = int(input("Введите k1"))
k2 = int(input("Введите k2"))
k3 = int(input("Введите k3"))
if k1 > 5:
 y1 = 1
elif k1 == 5:
 y1 = k1 * k2
else:
 y1 = k3
if y1 < k1:
 y2 = math.sqrt(abs(k1 - k2))
else:
 y2 = k1 / k2
print("y1 = ", y1, "y2 = ", y2)