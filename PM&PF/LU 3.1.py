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

marks = {
    "Aman": 85,
    "Riya": 92,
    "Karan": 76,
    "Simran": 88,
    "Rahul": 65
}
total=0
for student,mark  in marks.items():
    total+=mark

average=total/len(marks)
print("Average marks:", average)


