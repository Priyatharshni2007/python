# x = [13,23,34,56,78,89,90,67,46,50]
# sum = 0
# for i in range(0,9,2):
#     sum = sum+x[i]
# print(sum)
# for i in range(1,10,2):
    # sum = sum+x[i]
# print(sum)
# x = [1,1,2,3,4,2,3,3,3,7,6,8,9,5,5,0,9,1,4,0]
# x.append(6)
# print(x)
# x.pop()
# print(x)
# x.remove(7)
# print(x)
# x.insert(6,6)
# print(x)

def fibonacci(n):
    if n <= 0:
        return "Please enter a positive number"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    
    a,b = 0,1
    for i in range(2,n):
        a,b = b,a+b
    return b
    
n = int(input("Enter the value of n"))
print(fibonacci(n))