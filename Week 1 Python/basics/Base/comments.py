#comments
#This is a comment, it is ignored by the computer
#Comments are for humans to read, they explain what the code does


'''Single line comments'''
#start with a hash symbol (#) and continue to the end of the line.'''
# This is a comment
print("Hello")  # This is also a comment

# You can have multiple lines
# of comments by starting
# each line with a hash

age = 25  # Store user's age
print(age)  # Print the user's age


'''Multi-line comments'''
# You can also use triple quotes (''' or """) to create multi-line comments. This is often used for longer explanations or documentation.'''

"""
This is a multi-line comment.
It can span several lines.
Great for longer explanations.
"""

def calculate_tip(bill):
    """
    Calculate 20% tip for a restaurant bill.
    Takes the bill amount and returns the tip.
    """
    return bill * 0.20



'''When to use comments?'''
#1. Good comments explain why something is done, not what is done. The code itself should be clear enough to show what it does.
#2. Use comments to explain the purpose of a block of code, especially if it's not

# Good: Explains why
# Using 1.0625 because sales tax in CA is 6.25%
total = subtotal * 1.0625

# Bad: States the obvious
# Multiply subtotal by 1.0625
total = subtotal * 1.0625



'''Temporary comments'''
print("Starting process...")

#print("This is a debug message")  # This line is commented out temporarily
new_method()  # Call the new method instead
#old method()  # Old method for reference, but not used anymore




