name = input("Please enter your name:")
# age = input ("What about your age:")
# age = input("Hi %s, what about your age:"% (name))
age = input("Hi {}, what about your age".format(name))

# print("Hello World, my name is", name, "and I am", age, "years old.")
# print("Hello world, my name is %s and I am %s years old." %(name, age))
print("Helo World, my name is {} and \n"
"I am {} years old".format(name, age))