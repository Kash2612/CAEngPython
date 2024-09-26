# we should use functions for simplicity
# def greet():
#     print("hi there")
#
# greet()

# parameter : input in function definition
# argument: actual values through which a function is called

def greet(fname, lname):
    print(f"hi there {fname} {lname}")


greet("kashish", "gupta")
print(greet("kashish", "gupta"))  # none


# types:
# 1. perform a task
# 2. return a value

def get_ans(name):
    return f"hi {name}"


print(get_ans("kashish"))


def increment(number, by):
    return number + by

# keyword argumements
result = increment(6, by=1)
print(result)

# how to make parameters optional
def decrement(number, by=1):
    return number-by

print(decrement(3))
print(decrement(7,4))

# all optional parameters should come after the required ones

#PRACTICE FIZZBUZZ QUESTION

def fizzbuzz(a):
    if a%3==0 and a%5==0:
        return "fizzbuzz"
    elif a%3==0:
        return "fizz"
    elif a%5==0:
        return "buzz"
    else:
        return a
print(fizzbuzz(7))