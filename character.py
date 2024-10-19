string = input(" Create your own word :")
char = input(" Create your own Character : ")
i = 0
count = 0
while(i < len(string)):

    if(string[i] == char):
        count = count + 1
    i = i +1

print(" The total number of times", char," has Occurred = ", count)        