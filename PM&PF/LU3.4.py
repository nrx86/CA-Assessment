# nums = [4, 9, 2, 7, 8, 1]
# count=0
# for num in nums:
#     if num > 5:
#         count+=1
# print("Numbers  greater than 5: ", count)

# nums = [3, 6, 9, 12, 15, 18]
# evens=[]
# for num in nums:
#     if num%2==0:
#         evens.append(num)
# print(evens)

# word="education"
# count=0
# for ch in word:
#     if ch in "aeiou":
#         count+=1
        
# print("Number of vowels:", count)

# nums = [12, 5, 8, 20, 3, 17]
# filtered=[]
# for num in nums:
#     if num >= 5 and num <=15:
#         filtered.append(num)
# print("Filtered numbers:", filtered)
# print("Total numbers:", len(filtered))

# text = "Rs 1,299 only"
# result=""
# for ch in text:
#     if ch.isdigit():
#         result+=ch
# print(result)

nums = [3, 11, 7, 2, 15, 6]
short_count=0
long_count=0
for num in nums:
    if num<8:
        short_count+=1

    elif num>=8:
        long_count+=1

print("Short numbers:", short_count)
print("Long numbers:", long_count)
