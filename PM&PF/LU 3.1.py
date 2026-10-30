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

sales={}
sales["Shoes"]=2500
sales["T-shirt"]=800
sales["Jeans"]=1800
sales["Jacket"]=3500
sales["Cap"]=400
total=0
count=0
for products in sales:
    total+=sales[products]
    if sales[products]>1000:
        count+=1

print("Total sales:", total)
print("Items with sales greater than 1000:", count)
    
