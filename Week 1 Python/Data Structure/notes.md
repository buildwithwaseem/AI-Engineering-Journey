# Data Structure
stores multiple values together 

## Beyond single values

So far, you’ve stored one value per variable. But what if you need to store multiple values? That’s where data structures come in.

## Think of data structures as containers:
1. Lists: Like a shopping list (ordered items)
2. Dictionaries: Like a phone book (name > number)
3. Tuples: Like coordinates (fixed values)
4. Sets: Like a bag of unique items


# which one to use??
-  List: when order matters and you need to change items
-  Dictionaries : when you need to look up values by name
-  Tuples : when data shouldn't change (like coordinates)
-  Sets: when you only care about unique values


# NOTES- ----
Python counts from 0, not 1! The first item in any collection is at position 0, the second at position 1, and so on. This is called “zero-based indexing” and you’ll see it throughout Python.





# let's learn about    L I S T 
- it works with ordered collections

# What are Lists??
Lists are Python’s most versatile data structure. They’re like containers that can hold multiple items in a specific order.
## Think of a list like:
1. A shopping list (milk, eggs, bread)
2. A to-do list (tasks in order)
3. A playlist (songs in sequence)


# L I S T    COMMON MISTAKES 

# 1. Index out of range

### Wrong
fruits = ["apple", "banana"]
print(fruits[2])  # IndexError!
### Right - check length first
if len(fruits) > 2:
    print(fruits[2])


# 2.Modifying while looping

## Wrong - changes list size during loop
numbers = [1, 2, 3, 4]
for num in numbers:
    if num == 2:
        numbers.remove(num)  # Dangerous!
## Right - use list comprehension
numbers = [num for num in numbers if num != 2]



# 3. Shallow copy issues

## Wrong - both variables point to same list
list1 = [1, 2, 3]
list2 = list1
list2.append(4)
print(list1)  # [1, 2, 3, 4] - changed!
## Right - make a copy
list1 = [1, 2, 3]
list2 = list1.copy()
list2.append(4)
print(list1)  # [1, 2, 3] - unchanged



----------------------------------------------------------------------------------------------------------------------------

# LETS LEARN ABOUT           <br/> D I C T I O N A R I E S
-  stores data with key-value pairs

# What are Dictionaries ?
Dictionaries store data in key-value pairs. Think of them like a real dictionary where you look up a word (key) to find its definition (value).

## Real-world examples:
- Phone book: name > phone number
- Menu: dish > price
- User profile: username > user info

## NOTES
Dictionaries use curly braces {} with key-value pairs separated by colons. Keys must be unique!

# COMMON MISTAKES

# 1. KeyError when key doesn't exist

## Wrong
person = {"name": "Alice"}
print(person["age"])  # KeyError!
## Right - use get()
print(person.get("age", 0))  # Returns 0 if missing


# 2. Using mutable keys

## Wrong - lists can't be keys
bad_dict = {[1, 2]: "value"}  # TypeError!
## Right - use immutable types
good_dict = {(1, 2): "value"}  # Tuple is OK
good_dict = {"1,2": "value"}   # String is OK

--------------------------------------------------------------------------------------------------------------


# let's learn about TUPLES
-----------------------------------------------------------------------------------------------
- Work with immutable sequences

## What are tuples?
Tuples are like lists, but they can’t be changed once created. They’re immutable (unchangeable) sequences.

## Use tuples for data that shouldn’t change:
1. Coordinates (x, y)
2. RGB colors (255, 0, 0)
3. Database records
4. Function return values

**A single-item tuple needs a comma: (42,) not (42). Without the comma, Python thinks it’s just parentheses around a number!**


# COMMON MISTAKES IN TUPLES
# 1.Forgetting comma in single tuple

## Wrong - not a tuple
single = (42)
print(type(single))  # <class 'int'>
## Right - include comma
single = (42,)
print(type(single))  # <class 'tuple'>

# 2.Trying to modify tuples

## Wrong - tuples are immutable
point = (3, 5)
point[0] = 4  # TypeError!
## Right - create a new tuple
point = (4, point[1])
## Or convert to list, modify, convert back
temp = list(point)
temp[0] = 4
point = tuple(temp)


