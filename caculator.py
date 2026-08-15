# making calculator

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def multi(a, b):
    return a * b

def div(a, b):
    return a / b


print("1. addition")
print("2. subtraction")
print("3. multiplication")
print("4. division")

x = int(input("enter your choice :"))

a = int(input("enter your number 1 :"))
b = int(input("enter your number 2 :"))

if x == 1:
    print(add(a, b))

elif x == 2:
    print(sub(a, b))

elif x == 3:
    print(multi(a, b))

elif x == 4:
    print(div(a, b))

else:
    print("Invalid choice")