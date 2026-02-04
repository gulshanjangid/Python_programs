# a = int(input("Enter a number: "))
# if a == 1:
#     print("1 is not a prime number.")
# elif a >1 :
#     for i in range(2, int(a/2)+1):
#         if (a % i) == 0:
#             print(a, "is not a prime number.")
#             break
#     else:
#         print(a, "is a prime number.")
# else:
#     print("Please enter a valid positive integer.")
    
    
lower = int(input("Enter lower range: "))
upper = int(input("Enter upper range: "))
print("Prime numbers between", lower, "and", upper, "are:")
for num in range(lower, upper + 1):
    if num > 1:
        for i in range(2, int(num / 2) + 1):
            if (num % i) == 0:
                break
        else:
            print(num)
            
            
            
    