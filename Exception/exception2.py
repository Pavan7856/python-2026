try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    result = a / b

except ValueError:
    print("Enter valid integer values")

except ZeroDivisionError:
    print("Second number cannot be zero")

else:
    print("Division result:", result)

finally:
    print("Program execution completed")