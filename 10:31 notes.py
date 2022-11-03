# Warm- Up:Write code that calculates the factorial of a given number. 
# Allow the user to input the number they wish to calculate the factorial of
# Code the calculation
# Ex: 5! = 5*4*3*2*1
x = int(input("Please eneter the number you would like to calculate the fractorial of: "))
y = 1
z = x
while z > 0:
    y = y * z
    z -= 1
print("The factorial of you number," , x , "is", y)
# Exercise 1: Use recursion to write code for the calculation of a factorial
def factorial(c):
    if c > 1:
        return c*factorial(c-1)
    else:
        return 1
print(factorial(5))