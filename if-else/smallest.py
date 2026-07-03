a=int(input("Enter the number: "))
b=int(input("Enter the number: "))
c=int(input("Enter the number: "))
if a < b and a < c:
    print("a is smallest")
elif b < a and b < c:
    print("b is smallest")
else:
    print("c is smallest")
