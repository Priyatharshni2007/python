# import random as rm
# choice = True
# while choice:
#     x = rm.randint(1,6)
#     print(x)
#     choice = input("Do you want to roll again? (yes/no): ")

# a = {"Tea" : "12" , "samosa" : "10" , "juice" : "35" , "lunch" : "400" }
# print(a)

# a["breakfast"] = "40"
# print(a) 
# print(a ["Tea"])

choice = True
expense_tracker = {"expences" : "amount"}
while choice:
    a = input("Add Expence : ")
    b = int(input("Add Amount : "))
    expense_tracker[a] = b
    choice = input("Do you want to add more expence? ")
# print(expense_tracker)
for i,j in expense_tracker.items():
    print(f"{i} : {j}")

