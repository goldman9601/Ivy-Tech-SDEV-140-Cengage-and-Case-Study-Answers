import random

afile = open("Random.txt", "w" )

for i in range(int(input('How many random numbers?: '))):
    line = str(random.randint(1, 100))
    afile.write(line)
    print(line)

afile.close()