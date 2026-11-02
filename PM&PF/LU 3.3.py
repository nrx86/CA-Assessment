#Write a Python program that repeatedly asks the user to enter their age until they enter digits only.
# while True:
#     age=input("Age bata be: ")
#     if age.isdigit():
#         print("Tu itne saal se dharti pr hai:", age)
#         break
#     print("Angrezi kyu likh ra hai bhaiii! Sirf number daal be!")

#Write a Python program that repeatedly asks the user to enter their age until they enter a valid age between 18 and 120 (inclusive).
# while True:
#     age=input("Enter your age (18 to 120):")
#     if age.isdigit():
#         age=int(age)
#         if 18 <=age<=120:
#             print("Accepted. Age:", age)
#             break
#         else:
#             print("Age must be between 18 and 120.")
#     else:
#         print("Age must be a number.")

#Write a Python program that repeatedly asks the user: continue? (yes/no):
# while True:
#     response=input("Continue? (yes/no): ")
#     if response.lower()=="yes" or response.lower()=="no":
#         print("You chose:", response)
#         break
#     else:
#         print("Please type yes or no.")

#Write a Python program that repeatedly asks the user to enter their name.
while True:
    name=input("Enter your name:")
    if name.isalnum():
        print("Hello", name)
        break
    else:
        print("Name cannot be empty.")
