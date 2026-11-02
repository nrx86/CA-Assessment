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
    
from functools import total_ordering
from itertools import count
from os import name
from tokenize import Name
from turtle import st


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

# expenses={}
# expenses["Food"]=250
# expenses["Travel"]=150
# expenses["Shopping"]=400
# expenses["Books"]=200

# total=0

# for amount in expenses:
#     total+=expenses[amount]
# print("Total expenses:", total)

# marks={}
# marks["Rahul"]=85
# marks["Aman"]=42
# marks["Priya"]=91
# marks["Rohit"]=35
# marks["Sneha"]=67
# marks["Karan"]=28

# count=0

# for student in marks:
#     if marks[student]<50:
#         count+=1
# print("Number of students scoring less than 50:", count)

# scores= {}
# scores["Kohli"]=95
# scores["Rohit"]=72
# scores["Gill"]=88
# scores["Bumrah"]=45
# scores["SKY"]=81

# highest=0
# player=""

# for players in scores:
#     if scores[players]>highest:
#         highest=scores[players]
#         player=players

# print("Top player:", player)
# print("Highest score:", highest)

# frequency={}
# numbers = [2, 3, 2, 5, 3, 2, 5, 1, 3, 2]

# for digit in numbers:
#     frequency[digit] = frequency.get(digit,0)+1
# print("Frequency of numbers:", frequency)

# marks={}
# marks["Maths"]=85
# marks["Physics"]=72
# marks["Chemistry"]=91
# marks["English"]=78
# marks["Biology"]=64

# total=0

# for subject in marks:
#     total+=marks[subject]
# average=total/len(marks)
# print("Average marks:", average)

# temperatures={}
# temperatures["Delhi"]=32
# temperatures["Mumbai"]=29
# temperatures["Jaipur"]=35
# temperatures["Shimla"]=18
# temperatures["Chennai"]=31

# lowest = float('inf')
# city=""

# for cities in temperatures:
#     if temperatures[cities]<lowest:
#         lowest=temperatures[cities]
#         city=cities
# print("City with lowest temperature:", city)
# print("Lowest temperature:", lowest)

# data={"seven": 7, "eight": 8, "nine": 9}
# for number in data:
#     print(number)
# print("Loop completed")

# students={}
# students["Rahul"]=85
# students["Aman"]=72
# students["Priya"]=91
# students["Rohit"]=68

# for student in students:
#     print(student, students[student])

# students["Sneha"]=88
# print("Updated student marks:", students)

# marks = {"Maths": 85, "Physics": 78, "Chemistry": 92}
# print(marks.get("Physics", 0))
# print(marks.get("Biology", 0))

# counts={}
# word="banana"
# for letter in word:
#     counts = {}
# word = "banana"

# for letter in word:
#     if letter in counts:
#         counts[letter] += 1
#     else:
#         counts[letter] = 1

# smallest = float('inf')
# smallest_letter = ""

# for letter in counts:
#     if counts[letter] < smallest:
#         smallest = counts[letter]
#         smallest_letter = letter

# print("Frequency of letters:", counts)
# print("Letter with smallest frequency:", smallest_letter)
# print("Smallest frequency:", smallest)


# products = {
#     "Laptop": 55000,
#     "Mouse": 800,
#     "Keyboard": 1500,
#     "Monitor": 12000
# }
# print("Products and their prices:")
# for item in products:
#     print(item, ":", products[item])
# total=0
# highest=0

# for item in products:
#     total+=products[item]
#     if products[item] > highest:
#         highest = products[item]
#         product=item

# print("Total value of products:", total)
# print("Highest product value:", highest)
# print("Product with highest value:", product)


