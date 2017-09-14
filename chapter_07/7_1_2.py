# age = input("How old are you? ")

# print(type(age))        # <class 'str'>
# print(type(int(age)))   # <class 'int'>



height = input("How tall are you, in inches? ")
height = int(height)

if height >= 36:
    print("\nYou're tall enough to ride!")
else:
    print("\nYou'll be able to ride when you're a litter older.")
