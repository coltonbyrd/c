# Create a text file through Visual Studio Code that is 
# called practice.txt

# Open your text file with write abilities
import readline


filey = open("newfile.txt", "w")
# Write yourself a message in this text file. 
filey.write("Hello \n")
# Loop through the provided list and write each item in the list,
# separated by a comma
People = ["Arthur", "Calvin", "Atlas", "Brione"] 
for x in People:
    filey.write( x + ",")

# Loop through the provided dictionary and write each key and value
# in a statement, such as "An apple is 6.8 ounces on average." 
# Be sure to include a new line between each statement.
FruitWeights = {"Apple": 6.8, "Apricot":1.2, "Avocado":6, 
"Banana":4.2 , "Blackberry":0.09}
for (k,v) in FruitWeights.items():
    filey.write("\nAn " + k + " is " + str(v) + " ounces on average.")


# Read in all the lines from ROSTER.csv and write them to
# your practice.txt file 
file2 = open("ROSTER.csv", "r")
for lines in file2:
    filey.write(lines)