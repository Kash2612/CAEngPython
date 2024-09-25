# programming with mosh
# BASICS OF PYTHON
print("hello world")
print(2+3)
age=20
f_name="Kashish"
isValid=False
print(age)

#take input: always takes input in string
name=input("What do you do?")
print("Hello"+name)

# data type: number, string, boolean
#conversion
birth_year=input()
#age=2025-birth_year
#print(age) #causes error as birth_year is string and 2025 is int

age=2025- int(birth_year);
print(age)

# similarly we have float(), bool(), and str()
num1= input("enter number 1")
num2=input("enter number 2")
sum= float(num1)+ float(num2)
print("sum is: "+ str(sum))

# we can also take input as
first=float(input())

#inbuilt string functions
course="heyyy this is me"
course.upper()
course.find("me")
print(course.replace("me","you"))
print(course)

#IN return true or false
#division return boolean
#floor division gives floor value like java division

#logical- and, or, not

# CONTROL FLOW
# if-elif-else loops (indentation represents block of code)
temp=90
if temp>100:
    print("it's hot")
elif temp==90:
    print("it's 90")
else:
    print("cold")
print("done")

# while loops
n=5
while n>0:
    print(n)
    n-=1

#we can't concatenate strings, but we can multiply them

# lists
names=["kashish","harsh", "shivangi","akriti"]
print(names[0])
print(names[-1])
print(names[0:2])


#objects
numbers=[1,2,3,"a",True]
print(numbers)
numbers.append(7)
numbers.insert(2,10)
print(numbers)
#remove : to remove a particular one
#clear: to remove complete list

# tuple- immutable(can't be changed)/ can implement magic methods
numb=(1,2,3)
numb.count(3)


#for loop
for item in numbers:
    print(item)

for x in "apple":
    print(x)

i=0
while i< len(numbers):
    print(numbers[i])
    i+=1

for i in range(5):
    print(i)

range(0,5,2) #start,stop,steps

#ERROR HANDLING IN PYTHON
#The try block lets you test a block of code for errors.
#The except block lets you handle the error.
#The finally block lets you execute code, regardless of the result of the try- and except blocks.
q=1
print(f"heyaaa {q} is:") #formatted string literal

a=input("enter a number")
print(f"multiplication table of {a} is:")
try:
    for i in range(1,11):
        print(f"{int(a)} X {i} = {int(a)*i}")
except Exception as e:
    print(e)
finally:
    print("it will always run")
#finally for clean ups

try:
    num = int(input("Enter an integer: "))
except ValueError:
    print("Number entered is not an integer.")

#we can have multiple excepts

# the name of python program should not match the module name
# *args and **kwargs
