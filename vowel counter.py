# x = input("Enter the sentence: ")
# vcounter = 0
# ccounter = 0
# v = ['a','e','i','o','u']
# for i in x:
#     if i in v:
#         vcounter = vcounter+1
#     else:
#         ccounter = ccounter+1

# print(f" vowels : {vcounter}, consonants : {ccounter}")



# x = input("Enter the word : ")
# # x = []
# b = x[ : :-1]
# print(b)




# a=str(input("Enter the word: "))
# b = a[:]
# c = []
# for i in a[::-1]:

# if b == x : 
#     print("The world is palindrome ")
# else  : 
#     print("The word is not a palindrome ")





# x = input("Enter the sentence : ")
# y = x.split(" ")
# print(y)
# for i in y:
#    s = i.capitalize()
#    print(s,end=" ")




# txt = "I Love Java"
# x = txt.replace("Java", "Python")
# print(x)




# x = "abc123def"
# ncounter = 0
# g = [0,1,2,3,4,5,6,7,8,9]
# for i in x:
#     if int(i) in g:
#         ncounter = ncounter+1
# print(ncounter)




# sentence = "hi how 123are 22you"
# # counter = 0
# for x in sentence:
#     if x.isdigit():
#         # counter = counter + 1
#         print(x,end="")

# print(counter)




# sentence = "hi how 123are 22you"
# nums = ['0','1','2','3','4','5','6','7','8','9']
# for x in sentence:
#     if x in nums:
#         # counter = counter + 1
#         print(x,end="")




# x = input("Enter the sentence")
# y = x.split(" ")
# counter = []
# # print(y)
# for z in y : 
#     counter.append(len(z))
# print(counter)
# max = max(counter)
# max_index = counter.index(max)
# print(max_index)
# # print(max_index)
# print(y[max_index])




# x = input("Enter the word : ")
# y = input("Enter the character : ")
# counter = 0
# for z in x:
#     if z == y:
#         counter = counter + 1
# print(counter)




# x = input("Enter the word : ")
# y = x.replace(" ","")
# print(y)
# if x.isalpha():
#     print("True")
# else:
#     print("False")




# x = input("Enter the word : ")
# for i in x:
#     if i.islower():
#         a = i.upper()
#         print(a,end="")
#     else:
#         a = i.lower()
#         print(a,end="")




# x = "Python"
# first_character = x[0]
# last_character = x[-1]
# print(first_character)
# print(last_character)




# x = input("Enter the word : ")
# N = int(input("Enter the value of N : "))
# y = x*N
# print(y)




# x = input("Enter the word : ")
# y = len(x)
# for i in range(0,y):
#     print(f"{x[i]} : {i}") # format string




# x = input("Enter the word : ")
# y = input("Enter the specific character : ")
# if x[0] == y:
#     print("True")
# else:
#     print("False")




# sentence = "a1b2c3"
# for x in sentence:
#     if x.isalpha():
        
#         print(x,end="")



        
x = input("Enter the word : ")

for i in x : 
    print(f"{i} : {ord(i)}")

# a = [[1,2,3] , [4,5,6] ]
# for i in a:
#     for j in i:
#         print(f"{j}" , end ="\n")