''' L O O P S '''

#without loops, we would have to repeat code multiple times to achieve the same result
print("Hello")
print("Hello")
print("Hello")
print("Hello")
print("Hello")
print("Hello")
print("Hello")
print("Hello")



#with loops, we can repeat code as many times as we want without having to write it multiple times
for i in range(8):
    print("Hello")

#both do the same thing, but the second one is more efficient and easier to read.



'''F O R   L O O P S'''
#for loops are used to iterate over a sequence (like a list, tuple, string, etc.) or other iterable objects.

# Print numbers 0 through 4
for i in range(5):
    print(i)

# Output:
# 0
# 1
# 2
# 3
# 4

# c o u n t i n g  ------
#count from 1 to 5
for i in range(1, 6):
    print(i)    
# Output: 1, 2, 3, 4, 5

#count by 2s from 0 to 10
for i in range(0, 11, 2):
    print(i)
# Output: 0, 2, 4, 6, 8, 10



'''Loop through text'''
#You can loop through each character in a string:
name = "Python"
for letter in name:
    print(letter)

# Output:
# P
# y
# t
# h
# o
# n

# Through a list:
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(f'i love {fruit}')

# Output:
# i love apple
# i love banana
# i love cherry





''' W H I L E    L O O P S'''
#while loops are used to execute a block of code as long as a specified condition is true.

count = 0
while count < 5:
    print(f"Count is {count}")
    count = count + 1  # Increase count by 1

# Output:
# Count is 0
# Count is 1
# Count is 2
# Count is 3
# Count is 4





