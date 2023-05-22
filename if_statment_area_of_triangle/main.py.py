def area_triangle(side1, side2, side3):
    if side1 < side2+side3 and side1 >= side2 and side1 >= side3:
        s = (side1+side2+side3)/2                              # s = semi-perimeter of triangle
        return ((s * (s - side1) * (s - side2) * (s - side3))) ** (1/2)        # Heron's Formula
    elif side2 < side1+side3 and side2>=side1 and side2>=side3:
        s = (side1 + side2 + side3) / 2
        return ((s * (s - side1) * (s - side2) * (s - side3))) ** (1/2)
    elif side3 < side1 + side2 and side3>=side2 and side3>=side1:
        s = (side1+side2+side3)/2
        return ((s*(s-side1)*(s-side2)*(s-side3)))**(1/2)

    else:
        print("Lenghts of tringle is invalid!")

side1 = float(input("Enter the length of side 1: "))
side2 = float(input("Enter the length of side 2: "))
side3 = float(input("Enter the length of side 3: "))
area = area_triangle(side1,side2,side3)
print("Area of triangle is: {:.2f} sq.units".format(area))