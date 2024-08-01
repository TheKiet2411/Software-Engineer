#4. Print out the numbers 1 to 10, but print ‘a’ instead if the number is divisible by 2, print ‘b’ if the number is divisible by 3, 
# and print ‘ab’ if the number is divisible by both 2 and 3.
for i in range(1, 11):
    if i % 2 == 0 and i % 3 == 0:
        print('ab')
    elif i % 2 == 0:
        print('a')
    elif i % 3 == 0:
        print('b')
    else:
        print(i)
