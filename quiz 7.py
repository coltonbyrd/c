# Question 1: Use comments to write out the three components
# of a while loop. Try to use the appropriate terminology and 
# describe what it actually does in the loop.

# Part 1 of a while loop is: intializer
#x = 0
# Part 2 of a while loop is: x(a variable)
#while x < 5:
# Part 3 of a while loop is: Incrementor
#x+=1


# Question 2
# Write a while loop that continues to collect a new number
# from the user until they actually enter an even number.
InputNum = int(input("Please enter an even number: "))
while InputNum % 2 != 0:
    InputNum = int(input("That was not an even number. Please try again: "))



# Question 3
# Write a while loop that uses the boolean variable FoundaTwo
# to loop through a list until a two is found. Once a two is 
# found, the while loop should break and you should display 
# "A two was found in the list.". If a two is not found,
# the while loop should loop through the entire length of the list
# and then display that "No two was found in the list". 
x = [1,3,5,7,9,2,4,6,8,10]
y = 0
while y < 11:
    if x[y] == 2:
        print("A two was found in the list")
        y = 11
    elif x[y] != 2:
        y += 1
    else:
        print("No two was found in th list")