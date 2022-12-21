#
# Example file for working with functions
#


# TODO: define a basic function
def func1():
      print("I am a function one.")

# func1()
# print(func1())
# print(func1)


# TODO: function that takes arguments
def func2(arg1, arg2):
      print(arg1, "", arg2)

# func2(3,5)

# TODO: function that returns a value
def func3(x):
      return x*x*x

# print(func3(9))

# TODO: function with default value for an argument
def power(num, x=1):
      result = 1;
      for i in range(x):
            result = result * num;
      return result;

# print(power(2))
# print(power(2, 2))

# TODO: function with variable number of arguments
def multiple_add(*args):
      result = 0;
      for item in args:
            result+=item
      return result

print(multiple_add(4,5,10,4, 10))