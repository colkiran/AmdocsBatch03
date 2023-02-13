
def greet():
    print("Greetings Mr.Messi, Welcome to the event......")

def greetGst(gname):
    print(f"Greetings Mr.{gname}, Welcome to the event.......")

# gname - non default argument, city  - default argument
# non default argument should not follow a default argument
def greetGstCty(gname, city = "Bacelona"):
    print(f"Greetings Mr.{gname} from {city}, Welcome to the event.........")
greet()

print("-" * 40)
greetGst("Messi")

print("-" * 40)
greetGstCty("Messi")
greetGstCty("Neymay")
greetGstCty("Ronaldo", "Turin")

print("-" * 40)
# variable length argument - list and dictionary as argument

def prodAll(*numbers):          # *num can accept more than one value into a tuple or list
    print(f"numbers :{numbers}")
    prod = 1
    for number in numbers:
        prod *= number
    return prod

print(prodAll(1, 2, 3, 4, 5))

print("-" * 40)

def extractAll(**details):          # accept data into a dictionary
    print(details)
    print("-" * 40)
    for k,v in details.items():
        print(k, "=>", v)


extractAll(pname="Lionel Messi", age=35, goals=350, club='PSG')

# Return values from a function
# return in the last line of execution in the code

print("-" * 40)
def addMe(x, y):
    return x + y

print(f"The sum of 5 and 8 is :{addMe(5, 8)}")

# find the factorial of a number and fibanocci series

# Factorial of a  number
print("-" * 40)

def fact(num):
    if num == 1 or n == 0:
        return 1
    else:
        return num * fact(num - 1)

n = 5
print(f"The factorial of {n} is :{fact(n)}")

print("-" * 40)

def fibo(n):
    if n <= 1:
        return n
    else:
        return fibo(n-1) + fibo(n-2)

iter = 8
print("Fibnocii Series :")
for i in range(iter):
    print(fibo(i), end=" ")
print()

print("-" * 40)
def arithmeticCalc(x, y):
    sum = x + y
    diff = x - y
    prod = x * y
    quot = x / y
    return sum, diff, prod, quot

res = arithmeticCalc(20, 5)
print(f"res :{res}")
