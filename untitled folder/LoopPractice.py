# These exercises are designed to help you further understand for loops and while loops
# I would like you to code individually, but feel free to work with a partner for support

# Exercise 1: Rewrite the following code as a loop

"""import turtle
bob = turtle.Turtle()
for i in range(4):
    bob.forward(50)
    bob.left(90)"""

# Exercise 2: Rewrite the following code as a loop

"""for i in range(6):
    input("Please input a number: ")"""


# Exercise 3: Write both a for loop and a while loop that execute 
# 4 times each and prints 0,1,2,3, each on their separate lines

"""or i in range(4):
    print(i)

counter = 0

while counter < 4:
    print(counter)
    counter = counter + 1"""""

    

# Exercise 4: Write both a for loop and a while loop that use the loop 
# variable IOU where IOU starts at a value of 3, stops at a value of 19 
# and iterates by a value of 3 each time the loop executes.
# Print the value of IOU in the loop each time it executes. 

"""for iou in range(3, 20, 3):
    print(iou)

iou = 3
while iou < 20:
    print(iou)
    iou = iou + 3"""


# Exercise 5: Write three separate loops that function in different ways, 
# but that all collect a number from the user 4 different times and prints the average
"""x = 0

for i in range(4):
    x = x + int(input("Please input a number"))

print(x/4)"""

"""x = 0

for i in range(4):
    x = x + float(input())

print(x/4)"""

"""counter = 0
x = 0

while counter < 4:
    x = x + int(input("NUMBER"))
    counter = counter + 1


print(x/4)"""
"""counter = 0
x = 0
while counter < 4:
    x = x + float(input("Please give me number:"))
    counter = counter + 1
print(x/4)"""

# Exercise 6: Reads in a string variable that iterates through every character 
# in the provided string. Print out each character individually on a new line.

"""string = "hello"
for x in string:
    print(x)"""

# Exercise 7: Input from a user how many times they want to run a loop and 
# create a loop that executes the number of times specified by the user and 
# prints out "hi" every time the loop executes

times = (input(str("How many times:")))

for x in times:
    str(print("hi"))

# Exercise 8: Input from a user how many times they want to run a loop and 
# create a loop that executes the number of times specified by the user. For 
# every time the loop executes, collect a new number from the user. Once outside 
# of the loop, print the sum of the numbers

# Extra Exercise: 
# Have the user input a string and then use the length of the string to determine
# how many times the loop will execute. Create a new string variable that you will be
# constructing: for every character in the inputted string, add an 'f' character to your new string.
# Outside of the loop, print both the new string and the length of the new string 



# Extra Exercises: 
# Input a string from the user. For every letter in the string, 
# check to see if the character is upper case and print out
# a statement that says "The claim that the (3rd) letter in the string is 
# uppercase is (False)." for every character