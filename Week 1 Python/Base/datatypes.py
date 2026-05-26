# DATA TYPES
'''#Numbers
#Text
#True/False'''

# String
name = "John Doe"
# Integer
age = 30
# Float
height = 5.9
# Boolean
is_student = True
# List
fruits = ["apple", "banana", "cherry"]
# Tuple
coordinates = (10.0, 20.0)
# Dictionary
person = {"name": "John", "age": 30, "city": "New York"}
# Set
unique_numbers = {1, 2, 3, 4, 5}



'''Why we need to know data types?'''
# 1. Data types help us understand what kind of data we are working with and how to manipulate'''
# Numbers can do math
total = 10 + 5  # 15

# Strings combine differently  
name = "Hello" + "World"  # "HelloWorld"

# Can't mix without converting
# age = "25" + 5  # Error!
age = int("25") + 5  # 30 (converted string to number)

'''CHECKING DATA TYPES'''
# Check different types
print(type(42))          # <class 'int'>
print(type(3.14))        # <class 'float'>
print(type("Hello"))     # <class 'str'>
print(type(True))        # <class 'bool'>

# Check variables
age = 25
name = "Waasu"
print(type(age))         # <class 'int'>
print(type(name))        # <class 'str'>