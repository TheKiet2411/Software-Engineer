#Print out the numbers 1 to 10, but print ‘a’ instead if the number is divisible by 2, 
# and print ‘b’ if the number is divisible by 3.
for i in range(1, 11):
    if i % 2 == 0:
        print('a')
    elif i % 3 == 0:
        print('b')
    else:
        print(i)
