# Creating a List
# 1. Using Square Brackets: Square brackets [] are used to create a list directly.

# a = [1, 2, 3]
# print(a)

# b = ['apple', 'banana']
# print(b)

# 2. Using list() Constructor: 

# a = list((1, 2, 3, 'apple', 4.5))  
# print(a)

# b = list("GFG")
# print(b)

# c = ["pavan"]
# print(c)

# d=list("PAVAN")
# print(d)

# a = [1, 2, 2, "Python"]
# print(a[0])   
# print(a)

# a = [10, 20, 30,"Pavan"]
# print(a[0])
# print(a[-1])

# a[1]="Jay"
# print(a)

# a[3:2]="Amit"
# print()

# # Adding Elements
# a = [1, 2]
# a.append(3)
# print(a)

# a = [1, 3]
# a.insert(1, 2)
# print(a)

# a = [1, 2]
# a.extend([3, 4])
# print(a)

# a = [1, 2]
# a.append([3,4])
# print(a)

# Updating Elements

# a = [10, 20, 30, 40, 50]
# a[1] = 25 
# print(a)


# Removing Elements
# remove(): Removes the first occurrence of an element.

# a = [1, 2, 3]
# a.remove(3)
# print(a)

# pop(): Removes the element at a specific index or the last element if no index is specified.
# a = [1, 2, 3]
# a.pop(1)
# print(a)

# #  del statement: Deletes an element at a specified index.
# a = [1, 2, 3]
# del a[1]
# print(a)

# # clear(): removes all items.
# a = [1, 2, 3]
# a.clear()
# print(a)

# Iterating Over Lists
# a = ['apple', 'banana', 'cherry']
# for item in a:
#     print(item)

# Nested Lists
a = [[1, 2], [3, 4]]
print(a[0])
print(a[1][0])
