import re

v = int(input("Enter number for check:"))

if v <= 1:
    print(v, "Enter number for check:")
   
   
if (v == v/1 or v == v/v or v < 2):
    print("number is simple")
   
    
else:
    print("no simple")
    
    
    

num = int(input("Enter number for check:"))

if num <= 1:
    print(num, "no simple")
else:

    is_prime = True
    for i in range(2, int(num/2)+1):
        if (num % i) == 0:
            is_prime = False
            break
    if is_prime:
        print(num, "number is simple")
    else:
        print(num, "no simple")