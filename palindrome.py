a=str(input("Enter the value of a: "))
b = a[:]
c = []
for i in a[::-1]:
    c.append(i)

if b == c : 
    print("The world is palindrome ")
else  : 
    print("The word is not a palindrome ")
