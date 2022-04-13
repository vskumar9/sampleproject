def task(a,b,c):
    if a==b or b==c or c==a:
        print('0')
    else:
        print('The sum of the three numbers : ',a+b+c)
a=int(input('Enter the 1st number : '))
b=int(input('Enter the 2st number : '))
c=int(input('Enter the 3st number : '))
task(a,b,c)

