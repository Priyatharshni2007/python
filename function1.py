def add_numbers(a,b) :
    sum=a**2+b**2
    return (sum)

# r = add_numbers (x,y)

# print(r)

def mul_numbers(a,b) :
    sum=a**2+b**2+2
    return (sum)

# s = mul_numbers (x,y)

# print(s)

def sub_numbers(a,b) :
    sum=(a+b)*(a**2-a*b+b**2)
    return (sum)

# k = sub_numbers (x,y)

# print(k)

def a3minusb3(a,b) :
    sum=(a-b)*(a**2+a*b+b**2)
    return (sum)

# o = a3minusb3 (x,y)

# print(o)

def mod_numbers(a,b) :
    sum=a**3 + 3*a**2*b + 3*a*b**2 + b**3
    return (sum)

# p = mod_numbers (x,y)

# print(p)

print('''
Enter you choice : 
    1.(a2+b2)
    2.(a+b)2
    3.(a3+b3)
    4.(a3-b3)
    5.(a-b)3

''')
x=int(input("Enter the value of x"))
y=int(input("Enter the value of y"))

choice = int(input("Enter choice : "))
if choice == 1:
    r = add_numbers (x,y)
    print(r)
elif choice == 2:
    s = mul_numbers (x,y)
    print(s)
elif choice == 3:
    k = sub_numbers (x,y)
    print(k)
elif choice == 4:
    o = a3minusb3 (x,y)
    print(o)
else:
    p = mod_numbers (x,y)
    print(p)
