# integers = [500, 450, 200, 300, 250]
# integers.append(100)
# integers.extend([200,300])

# integers.insert(1,50)
# integers.pop()
# integers.sort()
# print(integers)

# times=[45, 32, 50, 28, 40]
# times.append(35)
# times.extend([25, 60])
# times.insert(2, 30)
# times.remove(50)
# times.sort()

# print(times)
# print("Length: ", len(times))
# print("Minimum: ", min(times))
# print("Maximum: ", max(times))
# print("Total: ", sum(times))
# print("Average: ", sum(times)/len(times))

# numbers=[12,5,8,3]
# numbers.append(10)
# numbers.insert(1,7)

# removed=numbers.pop(2)
# numbers.sort()

# print("Removed element:", removed)
# print("Final list:", numbers)

# scores=(75,90,65,90,80)
# print(len(scores))
# print(scores.count(90))
# print(scores.index(90))
# first, second=scores[:2]
# print(first)
# print(second)

# prices = {"apple":40, "banana":20, "mango":60}
# print("Banana price:", (prices["banana"]))
# prices["apple"] = 45
# prices["orange"] = 30
# removed_price = prices.pop("mango")
# print("Removed mango price:", removed_price)
# print("Updated Prices:", prices)

from itertools import count
from operator import index
from re import U


# numbers=[2,4,2,6,4,8]
# unique_numbers=set(numbers)
# print(len(unique_numbers))
# unique_numbers.add(10)
# unique_numbers.discard(6)
# print(unique_numbers)

# attendance=80
# marks=65
# if attendance>=75 and marks >=40:
#     print("Eligible")

# marks=35
# if marks >=80:
#     print("Distinction")
# elif 40<=marks<80:
#     print("Pass")
# else:
#     print("Fail")

# age_text=input("Enter age: ")
# if age_text.isdigit():
#     print("Adult")
# else:
#     print("Minor")

# marks=int(input())
# bonus= marks * 10/100
# final_score=marks+bonus
# print(f"{marks}", {bonus}, {final_score})

# scores=[45, 78, 62, 90, 55]

# scores.append(85)
# scores.extend([70,95])
# scores.insert(2,88)

# removed_score=scores.pop()
# scores.sort(reverse=True)

# print("Leaderboard:", scores)
# print("Removed score:", removed_score)
# print("Highest score:", max(scores))
# print("Lowest score:", min(scores))
# print("Total score:", sum(scores))
# print("Number of scores:", len(scores))

# nums= [10, 20, 30, 40]
# nums.insert(2, 25)
# print(nums)

# cart = ["milk", "eggs", "bread"]
# cart.append("butter")
# cart.extend(["juice", "apples"])
# cart.insert(1,"cheese")

# print(cart)

# scores=[10, 20, 30, 20, 40]

# last= scores.pop()
# scores.remove(20)

# print(last)
# print(scores)

# nums=[5, 2, 8, 1, 3]
# nums.sort()
# print(nums)

# nums.sort(reverse=True)
# print(nums)


# nums = [5, 2, 8, 2, 10]

# # 1. append()
# nums.append(7)

# # 2. extend()
# nums.extend([3, 6])

# # 3. insert()
# nums.insert(1, 99)

# # 4. pop()
# removed = nums.pop()

# # 5. remove()
# nums.remove(2)

# # 6. count()
# count_2 = nums.count(2)

# # 7. index()
# index_10 = nums.index(10)

# # 8. Membership
# has_99 = 99 in nums

# # 9. sorted() - creates a new sorted list
# sorted_nums = sorted(nums)

# # 10. sort() - sorts original list
# nums.sort()

# # 11. reverse()
# nums.reverse()

# # 12. Built-in functions
# print("Length:", len(nums))
# print("Minimum:", min(nums))
# print("Maximum:", max(nums))
# print("Sum:", sum(nums))

# # Print results
# print("Removed item:", removed)
# print("Count of 2:", count_2)
# print("Index of 10:", index_10)
# print("Is 99 present?", has_99)
# print("Sorted copy:", sorted_nums)
# print("Final nums:", nums)

# # 13. clear()
# temp = [1, 2, 3]
# temp.clear()
# print("After clear:", temp)



# 1. Creating tuples
point = (3, 5)
person = ("Priya", 20, "A")
empty = ()
solo = (5,)

print("Point:", point)
print("Person:", person)
print("Empty tuple:", empty)
print("Single-item tuple:", solo)
print("Type of solo:", type(solo))

# 2. Accessing items and slicing
print("First item:", person[0])
print("Last item:", person[-1])
print("Slice:", person[0:2])

# 3. Length and membership
print("Length:", len(person))
print("Is 20 present?", 20 in person)

# 4. Tuples are immutable
# point[0] = 99  # TypeError: tuple cannot be changed

# 5. Packing and unpacking
x, y = point
print("x:", x)
print("y:", y)

name, age, grade = "Priya", 20, "A"
print("Name:", name)
print("Age:", age)
print("Grade:", grade)

# 6. One-line swap
a, b = 10, 20
a, b = b, a
print("After swap:", a, b)

# 7. Tuple methods
nums = (4, 1, 4, 2, 4)
print("Count of 4:", nums.count(4))
print("Index of 2:", nums.index(2))

# 8. Built-in functions
print("Length:", len(nums))
print("Maximum:", max(nums))
print("Minimum:", min(nums))
print("Sum:", sum(nums))

# 9. Convert tuple to list to modify it
temp = list(point)
temp[0] = 99
point = tuple(temp)
print("Modified point:", point)

# 10. Returning multiple values as a tuple
def divide(a, b):
    return a // b, a % b

q, r = divide(17, 5)
print("Quotient:", q)
print("Remainder:", r)


