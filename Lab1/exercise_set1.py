"""Exercise Set 1: Python Basics"""
from tokenize import endpats

import numpy as np
import matplotlib as plt

# Please, remove all the pass in the exercises and substitute them with the expected methods for your functions


# ex1
def return_val():
    a = int(input("Insert the first number:"))
    print("The first chosen value is:",a)
    b = int(input("Insert the second number:"))
    print("The second chosen value is:",b)

    if a*b < 1000:
        product = a*b
        print(product)
        return product
    else:
        summ = a+b
        print(summ)
        return summ

# ex2
def exercise2():
    print("aaaa")
    pass


# ex3
def exercise3():
    pass


# ex4
def div_by_5():
    list_ = [ 1 , 2, 3 ,5, 10,7,25,49,90]

    for i in list_:
        if i % 5 == 0:
            print(i)






# ex5
def check_name():
    string_ = "Emma is a good developer. Emma is also a writer"
    Emma_time = string_.count("Emma")

    print("The word emma is repeated:",Emma_time)

# ex6
def exercise6():
    pass


# ex7
def exercise7():
    pass


# ex8
def exercise8():
    pass


# ex9
def exercise9():
    pass


# ex10
def exercise10():
    pass


# ex11
def exercise11():
    pass


# ex12
def exercise12():
    pass


if __name__ == "__main__":
    print("EXERCISE SET 1")
    print("EX1")
    return_val()
    print("EX2")
    exercise2()
    print("EX3")
    exercise3()
    print("EX4")
    div_by_5()
    print("EX5")
    check_name()
    print("EX6")
    exercise6()
    print("EX7")
    exercise7()
    print("EX8")
    exercise8()
    print("EX9")
    exercise9()
    print("EX10")
    exercise10()
    print("EX11")
    exercise11()
    print("EX12")
    exercise12()
