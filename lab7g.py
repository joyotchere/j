#!/usr/bin/env python3
# Student ID: Joy Otchere

def function1():
    # This object 'a' is completely unrelated to the object 'a' in function2():
    a = 'object_function1'
    print('print() call in function1 on a:', a)

def function2():
    # This variable 'a' is completely unrelated to the variable 'a' in function1():
    a = 'function2_object'
    print('print() call in function2 on a:', a)

# Note that you cannot access the value of object 'a' created in function1() or function2() 
# with the print() functions after calling function1() and function2()

a = 'object_in_main'  # This is the 'a' in the main script
print('print() call in main on a:', a)
function1()
print('print() call in main on a:', a)
function2()
print('print() call in main on a:', a)
