print("Enter the value of a.b and c of quadratic equation")
a,b,c=int(input()),int(input()),int(input())
d=b*b-4*a*c
if d>0:
    print("Two real & distinct roots")
elif d==0:
    print("Real and equal roots")
else:
    print("Imagianry roots")