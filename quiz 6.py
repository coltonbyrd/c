# Number 1: Store the given data as a dictionary

"""Fruit Type 	Imperial (oz or lb.)   
Apple 	           6.8 oz 	
Apricot 	       1.2 oz 
Avocado 	       6 oz	
Banana   	       4.2 oz	
Blackberry	       0.09 oz	"""

FruitType = {"Apple":"6.8oz", "Apricot":"1.2oz", "Avocado":"6oz", "Banana":"4.2oz","Blackberry":"0.09oz"}
# Number 2: Use the dictionary you defined in number 1 to try and 
# access the average weight of an avocado in ounces. Store this as
# a float variable (Hint: you will need to ensure that you are only trying
# to convert the number to a float and not "oz")
x = FruitType[("Avocado")]
y = float(x[0])
# Number 3: Use this dictionary you defined in number one to loop
# through all items in the dictionary and print out a story including
# information about all of the fruits and their average weight. For example,
# you may print something like "An apple is 6.8 oz on average." 
# Remember that you can not hardcode this and both apple and 6.8 should be 
# accessed from your dictionary directly
for akey in FruitType.keys():
    print("An", akey,"is", FruitType[akey],"on average.")