n=int(input("Enter any number\n"))
s=' '
while n:
    r=n%8
    n=n//8
    s=str(r)+s
print("Octal number is=",s)