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

# def fibonacci(n):
#     if n <= 0:
#         return "Please enter a positive number"
#     elif n == 1:
#         return 0
#     elif n == 2:
#         return 1
    
#     a,b = 0,1
#     for i in range(2,n):
#         a,b = b,a+b
#     return b
    
# n = int(input("Enter the value of n"))
# print(fibonacci(n))

# x = int(input())
# y = int(input())
# prime = True
# for i in range(x,y+1,1):
#     for j in range(2,i+1):
#         if i == 2:
#             print(f"{i} is a prime number")

#         elif i % j == 0:
#             print(f"{i} is not a prime number")
#             break
#         else:
#             print(f"{i} is a prime number")
#             break
        



# if __name__ == '__main__':
#     n = int(input())
#     for i in range(1,n+1):
#         print(i,end="")