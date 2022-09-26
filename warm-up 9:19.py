def ave_fun(x, y ,z):
    """
    This Fuction takes 3 floats as perametrs and returns the average
    """
    return((x + y + z)/3)

fl1 = float(input("Please enter your first number:"))
fl2 = float(input("please enter your second number:"))
fl3 = float(input("Please enter your third number:"))

w = ave_fun(fl1, fl2, fl3)
print("The average of the numbers is...", w)
