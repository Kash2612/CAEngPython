# IMPORTANT TERMS

## Iterators

[//]: # (https://www.datacamp.com/tutorial/python-iterators-generators-tutorial)
Iterators are objects that can be iterated upon.

* Iterable :
A Python object which can be looped over or iterated over in a loop. Examples of iterables include lists, sets, tuples, dictionaries, strings, etc. 

* Iterator
An iterator is an object that can be iterated upon. Thus, iterators contain a countable number of values. 

```python
# instantiate a list object
list_instance = [1, 2, 3, 4]

# convert the list to an iterator
iterator = iter(list_instance)

# return items one at a time
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
```

```
1
2
3
4
```
Python automatically produces an iterator object whenever you attempt to loop through an iterable object.
```python
# instantiate a list object
list_instance = [1, 2, 3, 4]

# loop through the list
for iterator in list_instance:
  print(iterator)
"""
1
2
3
4
"""
```

### The lazy nature of iterators
It is possible to define multiple iterators based on the same iterable object. Each iterator will maintain its own state of progress. Thus, by defining multiple iterator instances of an iterable object, it is possible to iterate to the end of one instance while the other instance remains at the beginning.
```python
list_instance = [1, 2, 3, 4]
iterator_a = iter(list_instance)
iterator_b = iter(list_instance)
print(f"A: {next(iterator_a)}")
print(f"A: {next(iterator_a)}")
print(f"A: {next(iterator_a)}")
print(f"A: {next(iterator_a)}")
print(f"B: {next(iterator_b)}")
"""
A: 1
A: 2
A: 3
A: 4
B: 1
"""
```

## Generators
Generators are a special type of function that use the yield keyword to return an iterator that may be iterated over, one value at a time.<br/>

Generators do not store their contents in memory as you would expect a typical iterable to do.

```python
def factors(n):
  factor_list = []
  for val in range(1, n+1):
      if n % val == 0:
          factor_list.append(val)
  return factor_list

print(factors(20))
"""
[1, 2, 4, 5, 10, 20]
"""
```
The code above returns the entire list of factors. However, notice the difference when a generator is used instead of a traditional Python function:

```python
def factors(n):
  for val in range(1, n+1):
      if n % val == 0:
          yield val
print(factors(20))

"""
<generator object factors at 0x7fd938271350>
"""
```

Since we used the yield keyword instead of return, the function is not exited after the run. In essence, we told Python to create a generator object instead of a traditional function, which enables the state of the generator object to be tracked. 

Consequently, it is possible to call the next() function on the lazy iterator to show the elements of the series one at a time.

* YIELD KEYWORD
The yield keyword controls the flow of a generator function. Instead of exiting the function as seen when return is used, the yield keyword returns the function but remembers the state of its local variables.

The generator returned from the yield call can be assigned to a variable and iterated upon with the next() keyword – this will execute the function up to the first yield keyword it encounters. Once the yield keyword is hit, the execution of the function is suspended. When this occurs, the function's state is saved. Thus, it is possible for us to resume the function execution at our own will.


## LIST COMPREHENSION
concise way of creating lists
```python
squares=[]
for x in range(10):
    squares.append(x**2)
```
```python
[0,1,4,9,16,25,36,49,64,]
```
```python
squares = list(map(lambda x: x**2, range(10)))
```

```python
squares = [x**2 for x in range(10)]
```

```python
[(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
```

## LAMBDA FUNCTION
A lambda function is a small anonymous function.

A lambda function can take any number of arguments, but can only have one expression.
<br/>
lambda arguments : expression

```python
x = lambda a, b : a * b
print(x(5, 6))
```

## DECORATORS

[//]: # (https://www.datacamp.com/tutorial/decorators-python)
A decorator is a design pattern in Python that allows a user to add new functionality to an existing object without modifying its structure. Decorators are typically applied to functions, and they play a crucial role in enhancing or modifying the behavior of functions.
```python
def plus_one(number):
    def add_one(number):
        return number + 1


    result = add_one(number)
    return result
plus_one(4)

```

```python
def plus_one(number):
    return number + 1

def function_call(function):
    number_to_add = 5
    return function(number_to_add)

function_call(plus_one)

```

```python
def hello_function():
    def say_hi():
        return "Hi"
    return say_hi
hello = hello_function()
hello()

```