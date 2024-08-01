#2. Print out the numbers 1 to 10, but print ‘a’ instead if the number is divisible by 2.
for i in range(1, 11):
    if i % 2 == 0:
        print('a')
    else:
        print(i)
