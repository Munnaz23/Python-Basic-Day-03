# lower = int(input("Enter the lower bound: "))
# upper = int(input("Enter the upper bound: "))

# # print(f"Prime numbers between {lower} and {upper}:")
# print("Prime numbers between",lower,"and",upper)
# for num in range(lower, upper + 1):
#     if num > 1:
#         for i in range(2, num):
#             if num % i == 0:
#                 break
#         else:
#             print(num)


number=int(input("Enter the number: "))
if number==1:
    print("This is not prime number.")
if number>1:
    for i in range(2,number):
        if number%i==0:
            print("Is not a prime number.")
            break
        else:
            print("This is a prime number.")