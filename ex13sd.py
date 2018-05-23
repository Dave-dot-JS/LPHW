from sys import argv
form, age = argv

age = input("How old are you? ")

print("This form is titled: ", form)
print("You claimed that you are", age, "years old.")
true = input("Is this true? ")

if true == "No" :
    print("Why would you lie to me??")
else:
    print("Thank you for your honesty.")
