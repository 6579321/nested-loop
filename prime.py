lower = int(input("enter an upper range : "))
upper = int (input("enter an lower range : "))
print(" Prime number between ", lower , "and", upper, "are:")
for num in range( lower, upper + 1):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)