# V A R I A B L E S   COMMON   MISTAKES

1. Forgetting quotes around texY

# Wrong
name = Alice  # Python looks for a variable called Alice
# Right
name = "Alice"  # This creates text


2. Using undefined variables

# Wrong
print(score)  # Error: score doesn't exist yet
score = 10
# Right
score = 10
print(score)  # Now it works


3. Confusing = and ==

# = means "store"
age = 25
# == means "compare" (we'll learn this later)
if age == 25:
    print("Quarter century!")






# C O M M E N T S   COMMON MISTAKES

1. Outdated comments

# Bad: Says 15% but does 20%
# Calculate 15% tip
tip = bill * 0.20
# Good: Accurate
# Calculate 20% tip (standard)
tip = bill * 0.20


2. Over-commenting obvious code

# Bad: Too obvious
x = 5  # Set x to 5
y = 10  # Set y to 10
# Good: Only explain complex parts
x = 5
y = 10
position = x + y  # Convert to linear index



# N U M B E R S    COMMON MISTAKES

1. Division always returns float

# Even when dividing evenly
result = 10 / 2
print(result)       # 5.0 (not 5)
print(type(result)) # <class 'float'>
# Use // for integer result
result = 10 // 2    # 5


2. Can't use commas in numbers

# Wrong
million = 1,000,000  # Creates a tuple, not a number!
# Right
million = 1000000    # Hard to read
million = 1_000_000  # Python style



# S T R I N G S     COMMON MISTAKES

1. Mixing quotes

# Wrong - mismatched quotes
text = "Hello'
# Right - matching quotes
text = "Hello"
text = 'Hello'


2.Can't add strings and numbers

# Wrong
result = "Age: " + 25  # TypeError!
# Right - convert number first
result = "Age: " + str(25)


3. Forgetting quotes entirely

# Wrong
name = Alice  # Python looks for variable Alice
# Right  
name = "Alice"  # String literal




# B O O L E A N   COMMON MISTAKES
1. Wrong capitalization

# Wrong
is_ready = true   # NameError!
is_done = TRUE    # NameError!
# Right
is_ready = True
is_done = False


2. Using = instead of ==

# Wrong - this assigns, not compares!
if is_logged_in = True:
    print("Welcome")
# Right - but redundant
if is_logged_in == True:
    print("Welcome")
# Best - booleans are already True/False
if is_logged_in:
    print("Welcome")



# O P E R A T O R S    COMMON MISTAKES

1. Division always returns float

# Regular division
result = 10 / 2    # 5.0 (not 5)
# Integer division
result = 10 // 2   # 5


2. Order of operations

# Wrong
average = 10 + 20 + 30 / 3  # 40.0
# Right
average = (10 + 20 + 30) / 3  # 20.0


3. Confusing = and ==

# = assigns a value
age = 18
# == compares values
if age == 18:
    print("Just turned adult!")






# S T R I N G  MANIPULATION MISTAKES

1. Forgetting the f in f-strings

# Wrong
name = "Alice"
message = "Hello {name}"  # Prints: "Hello {name}"
# Right
message = f"Hello {name}"  # Prints: "Hello Alice"

2. Wrong quotes in strings

# Wrong - mismatched quotes
text = 'It's Python'
# Right - escape or use different quotes
text = "It's Python"  # Double quotes outside
text = 'It\'s Python'  # Escape the apostrophe










