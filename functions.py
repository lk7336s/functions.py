def division (number1, number2):
    x=number1/number2
    print(f"number1={number1}, number2={number2}, division={x}")

division(2,3)
division(5,6)
division(9,8)                                                                                                                                                                  output                                                                                                                                                                                 number1=2, number2=3, division=0.6666666666666666
number1=5, number2=6, division=0.8333333333333334
number1=9, number2=8, division=1.125

def create_name(first_name, last_name):
    first_name = first_name.capitalize()
    last_name =last_name.capitalize()
    return first_name + " " + last_name

full_name = create_name("lokesh","kilaru")

def addition (x,y):
    z=x+y
    return z

def substraction (x,y):
    z=x-y
    return z

def multiplication (x,y):
    z=x*y
    return z

print(addition(2,3))
print(substraction(3,4))
print(multiplication(4,5)) 

def happy_birthday(name , age):
    print(f"Happy Birthday {name}")
    print(f" u r fucking {age}")
    print()

happy_birthday("srivastava",30,)
happy_birthday(" madhu ",40)

def happy_birthday(name):
    print(f"Happy Birthday {name}")
    print(" fuck u ")
    print()

happy_birthday("srivastava")
happy_birthday(" madhu ")
