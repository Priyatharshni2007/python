x = [12,13,14,67,89]
print(x[ 0: 3])
y = int(input())
y = str(y)
sum = 0
for i in y:
    sum = sum+int(i)**3
    

y = int(y)

if y == sum:
    print("Amstrong number")
else:
    print("Not Amstrong number")
print(sum)

n = int(input())
for i in range(0,n):
    x = i**2
    print(x)
