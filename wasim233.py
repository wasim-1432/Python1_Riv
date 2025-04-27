n=int(input("Enter any number\n"))
sum=0
while n:
    sum=sum+n%10
    n=n//10
print("Sum of digit is=",sum)