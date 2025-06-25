class calci () :

    def area1(self,pi,r):
        circle = pi*r**2
        return circle

    def area2(self,b,h):
        triangle = 1/2*b*h
        return triangle

    def area3(self,a):
        square = a**2
        return square

r = int(input("Enter the value of r : "))
b = int(input("Enter the value of b : "))
h = int(input("Enter the value of h : "))
a = int(input("Enter the value of a : "))
pi = 3.14

print('''
Enter you choice : 
    1.circle
    2.triangle
    3.square

''')

ch = int(input("Enter your choice : "))
j = calci()

if ch == 1:
    k = j.area1(pi,r)
    print("The area of circle is : ",k)
    
elif ch == 2:
    l = j.area2(b,h)
    print("The area of triangle is : ",l)
    
elif ch == 3:
    m = j.area3(a)
    print("The area of square is : ",m)
    
else:
    print("Invalid choice")

# j = calci()
# k = j.area3(a)
# print(k)



