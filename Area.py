# Area of circle, triaangle, square, rectangle using funtion

def area_circle():
    r = int(input("Enter radius : "))
    print("Area of circle is : ",3.14*r*r)

def area_triangle():
    h = int(input("Enter the height : "))
    b = int(input("Enter the base : "))
    print("Area of triangle is : ", h*b)

def area_square():
    s = int(input("Enter side : "))
    print("Area of square is : ",s*s)

def area_rect():
    l = int(input("Enter length : "))
    b = int(input("Enter breath : "))
    print("Area of rectangle is : ",l*b)
