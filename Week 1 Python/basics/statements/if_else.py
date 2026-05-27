'''control flow'''
'''if-else statements'''
'''if condition:    # code to execute if condition is true
else:           # code to execute if condition is false'''
# example

age = 18
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")

# example with user input
age = int(input("Enter your age: "))
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")



''' M u l t i p l e     conditions with and , or , not '''
'''age = 25
has_license = True

# Both must be True
if age >= 18 and has_license:
    print("You can drive!")

# At least one must be True
if weekend or holiday:
    print("No work today!")

# Reverse the condition
if not raining:
    print("Let's go outside!")'''



'''N E S T E D   IF-STATEMENTS'''
has_ticket = True
age = 15

if has_ticket:
    if age >= 18:
        print("Enjoy the movie!")
    else:
        print("Need adult supervision")
else:
    print("Buy a ticket first")





