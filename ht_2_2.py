a = input("str: ")
print(a)
print(a[:3])
print(a[3:])

if (a[:3] == a[3:]):
    print("The entered string is symmetrical")
    
else:
    print("The entered string is not symmetrical")