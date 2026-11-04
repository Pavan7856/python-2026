# # Pass by Reference and Pass by Value
# # Variables refer to objects. Function behavior depends on whether the object is mutable or immutable.

# # Mutable objects like lists can be modified inside functions.
# # Immutable objects like integers and strings remain unchanged.

def myFun(x):
    x[0] = 20

b = [10, 11, 12, 13]
myFun(b)
print(b)

def myFun2(x):
    x = 20

a = 10
myFun2(a)
print(a)

