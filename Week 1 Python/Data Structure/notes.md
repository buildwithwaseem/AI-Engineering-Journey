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

# LETS LEARN ABOUT   D I C T I O N A R I E S
-  stores data with key-value pairs
