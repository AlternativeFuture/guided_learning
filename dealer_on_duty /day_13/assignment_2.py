def triangle_type(x: float, y: float, z: float) -> str:
    if x == y == z:
        return "Equilateral triangle"
    elif x == y or y == z or x == z:
        return "Isosceles triangle"
    else:
        return "Scalene triangle"


if __name__ == '__main__':
    input_x = float(input("Enter length of side x: "))
    input_y = float(input("Enter length of side y: "))
    input_z = float(input("Enter length of side z: "))

    triangle_result = triangle_type(input_x, input_y, input_z)
    print(triangle_result)

