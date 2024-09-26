# We have seen that a function can only pass a certain number of arguments.
# The number of arguments has to be decided while defining the function, and it can not be changed while calling it.
# In simple terms, the number of arguments passed should be the same as the ones that are defined.
# If we dislike this restriction and do not want ourselves to be bound by certain limits, then we are lucky to have *args and **kwargs with us.

# Asterisk is used in python as mathematical symbol for multiplication, but in case of arguments, it refers to unpacking.The unpacking could be for a list, tuple, or a dictionary.


# args is a short form used for arguments.
# It is used to unpack an argument. In the case of *args, the argument could be a list or tuple.

def user(*args):
    result=1
    for num in args:
        result*=num
    print(result)
user(1,2,3,4,5)

# The full form of **kwargs is keyword arguments. It passes the data to the argument in the form of a dictionary
# it sends argument in the form of key and value pair.
def save_user(**user):
    print(user)
save_user(id=1, name="kashish", age=20)


# One function that sums all
# def function_name_print(a, b, c, d, e):
#     print(a, b, c, d, e)

def funargs(normal, *argsdemo, **kwargsdemo):
    print(normal)
    for item in argsdemo:
        print(item)
    print("\nNow introducing **kwargs")
    for key, value in kwargsdemo.items():
        print(f"{key} is a {value}")


# function_name_print("Harry", "Rohan", "Skillf", "Hammad", "Shivam")

har = ["Harry", "Rohan", "Skillf", "Hammad",
       "Shivam", "The programmer"]
normal = "I am a normal Argument and the students are:"
kw = {"Rohan": "Monitor", "Harry": "Fitness Instructor",
      "The Programmer": "Coordinator", "Shivam": "Cook"}
funargs(normal, *har, **kw)




