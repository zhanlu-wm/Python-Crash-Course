age = 23

# message = "Happy " + age + "rd Birthday!"   # TypeError: must be str, not int
# print(message)

message = "Happy " + str(age) + "rd Birthday!"
print(message)