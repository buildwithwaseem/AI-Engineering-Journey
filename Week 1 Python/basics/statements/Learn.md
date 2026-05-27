# c o n t r o l   flow

# Making program thinks 
 So far, your programs run top to bottom, executing every line. But real programs need to make decisions - “if this, then that”.
Control flow is what makes programs intelligent!


# R E A L   -World example

1. ATM : IF password correct , THEN  allow access
2. Apps : IF user clicks button , THEN perform action
3. Weather apps : IF temperature < 0,  THEN  show snow icon
4. Games : IF health =0, THEN game over


# P r e r e q u i s i t e s 
Before starting this section, make sure you understand:
    1.Variables and data types
    2.Operators (especially comparison operators)
    3.Boolean values (True/False)



# IF S T A T E M E N T       COMMON MISTAKES

1. Forgetting the colon

# Wrong
if x > 5
    print("Big")
# Right
if x > 5:
    print("Big")


2. Using = instead of ==

# Wrong (assignment)
if x = 5:
    print("Five")
# Right (comparison)
if x == 5:
    print("Five")


3. Wrong indentation

# Wrong
if True:
print("Hello")  # IndentationError
# Right
if True:
    print("Hello")










# L O O P S   --------------
## Repeat code multiple times

## 1. What are loops?

Loops let you repeat code without writing it multiple times. Instead of copying and pasting, you tell Python to repeat the code for you.


# COMMON MISTAKES BY Loops
1. Forgetting the colon

# Wrong - missing colon
for i in range(5)
    print(i)
# Right - colon after the loop line
for i in range(5):
    print(i)


2.Wrong indentation

# Wrong - not indented
for i in range(3):
print(i)
# Right - indented inside the loop
for i in range(3):
    print(i)


3. Off-by-one errors

# Wrong - only goes to 4
for i in range(5):
    print(f"Item {i}")  # 0, 1, 2, 3, 4
# Right - if you want 1-5
for i in range(1, 6):
    print(f"Item {i}")  # 1, 2, 3, 4, 5









    