name = input('enter your name:')
age = int(input('enter your age:'))

print("hello my name is " + name + "and my age is " + str(age) + "years old")
print("hello my name is", name, "and i am", age, "years old")
print("hello my name is %s and i am %d years old" % (name, age))
print("hello my name is {} and i am {} year old".format(name, age))