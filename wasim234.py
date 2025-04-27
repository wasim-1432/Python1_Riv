n=int(input("Enter any number\n"))
s=' '
while n:
    r=n%2
    n=n//2
    s=str(r)+s
print("Binary number is=",s)