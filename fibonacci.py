a = 0
b = 1

number = int(input("Enter the value: "))

if number==1:
    print(a)
else:
    print(a)
    print(b)
    for i in range(2,number):
        c = a+b
        a=b
        b=c
        print(c)
