# prices = {
#     "apple": 30,
#     "banana": 10,
#     "cherry": 50,
#     "mango": 40
# }
# for fruit in prices:
#     print(fruit, prices[fruit])

# marks = {
#     "Aman": 85,
#     "Riya": 92,
#     "Karan": 76,
#     "Simran": 88,
#     "Rahul": 65
# }

# for name in marks:
#     if marks[name]>80:
#         print(name)

# prices = {
#     "apple": 30,
#     "banana": 10,
#     "cherry": 50,
#     "mango": 40
# }

# total = 0

# for fruit,prices  in prices.items():
#     total = total + prices
# print(total)

# marks = {
#     "Aman": 85,
#     "Riya": 92,
#     "Karan": 76,
#     "Simran": 88,
#     "Rahul": 65
# }
# total=0
# for student,mark  in marks.items():
#     total+=mark

# average=total/len(marks)
# print("Average marks:", average)

# scores = {
#     "Aman": 85,
#     "Riya": 92,
#     "Karan": 76,
#     "Simran": 88,
#     "Rahul": 65
# }
# highest=0
# topper=""
# for student in scores:
#     if scores[student] > highest:
#         highest = scores[student]
#         topper=student
# print("Highest marks:", highest)
# print("Topper:", topper)

# inventory = {
#     "apple": 12,
#     "banana": 5,
#     "cherry": 20,
#     "mango": 8,
#     "orange": 3
# }
# count=0
# for fruits in inventory:
#     if inventory[fruits]>7:
#         count+=1

# print("Number of fruits:", count)

# prices={}
# prices["Laptop"]=55000
# prices["Mouse"]=800
# prices["Keyboard"]=1500
# prices["Monitor"]=12000
# for product in prices:
#     if prices[product]>2000:
#         print(product)
    
# marks={}
# marks["Rahul"]=85
# marks["Aman"]=67
# marks["Priya"]=92
# marks["Rohan"]=74
# marks["Sneha"]=38
# count=0
# for student in marks:
#     if marks[student]>=60:
#         count+=1
#         print(student)
        

# print("Total students passed:", count)

# sales={}
# sales["Shoes"]=2500
# sales["T-shirt"]=800
# sales["Jeans"]=1800
# sales["Jacket"]=3500
# sales["Cap"]=400
# total=0
# count=0
# for products in sales:
#     total+=sales[products]
#     if sales[products]>1000:
#         count+=1

# print("Total sales:", total)
# print("Items with sales greater than 1000:", count)
    
from os import name
from tokenize import Name


# scores={}
# scores["Rahul"]=78
# scores["Aman"]=91
# scores["Priya"]=85
# scores["Rohan"]=96
# scores["Sneha"]=88

# highest=0
# topper=""
# for students in scores:
#     if scores[students] > highest:
#         highest=scores[students]
#         topper=students
# print("Topper:", topper)
# print("Highest marks:", highest)

# fruits = ["apple", "banana", "apple", "orange", "banana", "apple", "mango", "orange"]
# frequency={}
# for fruit in fruits:
#     frequency[fruit] = frequency.get(fruit,0)+1
# print(frequency)

# marks={}
# n=int(input("How many students? "))
# for i in range(n):
#     student_name=input("Enter student name: ")
#     student_marks=int(input("Enter marks: "))
#     marks[student_name]= student_marks

# print("Student marks:", marks)

# marks={}
# n=int(input("How many students?"))
# count=0
# for i in range(n):
#     student_name=input("Enter student name: ")
#     student_marks=int(input("Enter marks: "))
#     marks[student_name]=student_marks

# print("Students scoring 80 or more:")
# for student in marks:
#     if marks[student]>=80:
#         print(student)
#         count+=1
# print("Total students:", count)

# student={}
# student["Name"]= "Rahul"
# student["Age"]=18
# student["Marks"]=85
# print(student)
# print(student["Name"])

# marks={}
# marks["Maths"]=90
# marks["Physics"]=78
# marks["Chemistry"]=85
# marks["English"]=92

# for subject in marks:
#     print(subject)

# prices={}
# prices["Laptop"]=55000
# prices["Mouse"]=800
# prices["Keyboard"]=1500
# prices["Monitor"]=12000

# for product in prices:
#     print(product, prices[product])

# scores={}
# scores["Rahul"]=85
# scores["Aman"]=90
# scores["Priya"]=78

# for student in scores.keys():
#     print(student)

# inventory={}
# inventory["Pen"]=20
# inventory["Notebook"]=35
# inventory["Pencil"]=15
# inventory["Eraser"]=10

# for item in inventory.values():
#     print(item)

# players={}
# players["Virat"]=85
# players["Rohit"]=62
# players["Dhoni"]=45
# players["SKY"]=70

# for player,score in players.items():
#     print(player, score)

expenses={}
expenses["Food"]=250
expenses["Travel"]=150
expenses["Shopping"]=400
expenses["Books"]=200

total=0

for amount in expenses:
    total+=expenses[amount]
print("Total expenses:", total)