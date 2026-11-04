# two types 
# 1.Arbitray arg use single *name like tuple 
# 2.keyword Arbitray arge use two **name like dist

# Program 1.Arbitray arg use single *name like tuple 
# def print_names(*names):
#     print("Tuple received:", names)
#     for name in names:
#         print("Hello", name)
# # You can pass any number of values:
# print_names("Pavan", "Sachin", "Rahul")

def avg(*num):
    total = 0
    for i in num:
        total += i
    print("ave is", total / len(num))

avg(10, 40, 24)

# 2.keyword Arbitray arge use two **name like dist

def name(**name):
    print("Hello:", name["Fname"], name["Mname"], name["Lname"])
name(Fname="pavan", Mname="Tolaram", Lname="Rathod")

# both in one 
def myFun(*args, **kwargs):
    print("Non-Keyword Arguments (*args):")
    for arg in args:
        print(arg)

    print("Keyword Arguments (**kwargs):")
    for key, value in kwargs.items():
        print(f"{key} == {value}")

myFun('Hey', 'Welcome', first='Geeks', mid='for', last='Geeks')