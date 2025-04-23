print("Enter any three numbers")
x,y,z=int(input()),int(input()),int(input())
if x>=y and x>z:
    print(x)
elif y>x and y>=z:
    print(y)
elif z>=x and z>y:
    print(z)
else:
    print(x)