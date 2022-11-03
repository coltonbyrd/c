'''file = open(ROSTER.csv, "r")

begining_text = file.read(20)
print(begining_text)

middle_text = file.read(310)
print(middle_text)'''

file = open("ROSTER.csv", 'r')

for x in file:
    print(x)
