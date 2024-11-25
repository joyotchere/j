#!/usr/bin/env python3
# Student ID: Joy Otchere

def function1():
    global schoolName  # This line ensures the modification affects the global variable
    schoolName = 'SICT'  # Modifies the global schoolName
    print('print() in function1 on schoolName:', schoolName)

def function2():
    global schoolName
    schoolName = 'SSDO'  # Modifies the global schoolName
    print('print() in function2 on schoolName:', schoolName)

schoolName = 'Seneca'
print('print() in main on schoolName:', schoolName)
function1()
print('print() in main on schoolName:', schoolName)
function2()
print('print() in main on schoolName:', schoolName)
