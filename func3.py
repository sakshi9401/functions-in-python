a = 8
b = 2
c = sum((a,b))#built in function
print(c)

def func():
   print("hello u r in a function")

func()

#docstring
def func2(a ,b):
   """this function is for average of two numbers"""
   average = (a+b)/2
   return (average)

v = func2(12 ,8)
print(v)
print(func2.__doc__)