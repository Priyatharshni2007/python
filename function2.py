def add_numbers (a,b,c) :
    sum = a+b+c
    return (sum)
def mul_numbers (a,b,c) :
    mul = a*b*c
    return (mul)
def sub_numbers (a,b,c) :
    sub = a-b-c
    return (sub)

print('''
Enter your choice:
      1.a+b+c
      2.a*b*c
      3.a-b-c

''')
x=int(input("Enter the value of x"))
y=int(input("Enter the value of y"))
z=int(input("Enter the value of z"))

choice = int(input("Enter choice :"))
if choice == 1:
    r=add_numbers (x,y,z)
    print(r)
elif choice == 2:
    s=mul_numbers (x,y,z)
    print(s)
else:
    p=sub_numbers (x,y,z)
    print(p)
