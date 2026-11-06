
Accessing & Slicing

Tuples use zero-based indexing and support standard Python slicing.

fruits = ("apple", "banana", "cherry", "date")

print(fruits[0])     # Output: apple
print(fruits[-1])    # Output: date (negative indexing)
print(fruits[1:3])   # Output: ('banana', 'cherry')

# mutable object (like a list), that nested list can still be modified

colors = ("Red", "Green", "Blue")
r, g, b = colors

print(r)  # Output: Red

# Immutability & The "Loophole"
# If you attempt to change an item, Python throws an error. However, if the tuple contains a
# mutable object (like a list), that nested list can still be modified
bad_example = (1, 2, 3)
# bad_example[0] = 99  --> Throws TypeError!

# The Loophole:
nested_tuple = (1, 2, ["apple", "banana"])
nested_tuple[2][0] = "cherry"  # This works!
print(nested_tuple)  # Output: (1, 2, ['cherry', 'banana'])



# 4. Built-in Tuple Methods

# Because tuples cannot change, they only have two built-in methods:
# • count(value): Returns the number of times a value appears.
# • index(value): Returns the first index where the value is found

numbers = (1, 3, 7, 3, 8)
print(numbers.count(3))  # Output: 2
print(numbers.index(7))  # Output: 2
