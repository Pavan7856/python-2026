# a=[10,20,30,40,50,55,70,80]
# print(a)
# print("after updating :")
# a[5]=60

# print(a)


# a=[10,20,30,40,50,55,70,80]

# print(a)
# print("after change the ite")
# a[2:5]=[2,6]
# print(a)

# 

# o/p [10, 20, 30, 40, 50, 60, 70, 80]
# [10, 2, 5, 60, 70, 80]

# a = [10, 20, 30, 40, 50]

# # Replace items at indices 1 and 2
# a[1:3] = [21, 31]  
# print(a)

# a = [10, 20, 30, 40, 50]
# a[1:3] = [100, 200]
# print(a)
# # o/p
# # [10, 100, 200, 40, 50]


# a = [10, 20, 30, 40, 50]
# a[1:4] = [99]
# print(a)
# # o/p
# [10, 99, 50]

# a = [10, 20, 30, 40, 50]
# a[1:2] = [100, 200, 300]
# print(a)
# # o/p 

# # Using List Comprehension
# a = [10, 15, 20, 25]

# # Doubling even numbers
# a = [x * 2 if x % 2 == 0 else x for x in a]
# print(a)

a = [10, 15, 20, 25]

#Adding 5 to odd numbers
for i, x in enumerate(a):
    if x % 2 != 0:
        a[i] += 5
print(a)

# Explanation:
# Using a for loop with enumerate, we iterate through each index and value in the list. For each element: If the element is odd (x % 2 != 0), we add 5 to its value (a[i] += 5).
# After the loop completes, the updated list a becomes [10, 20, 20, 30].