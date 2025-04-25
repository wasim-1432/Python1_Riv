x=input("Enter any number\n")
u=' '
for i in x:
    if i not in u:
        u+=i
print("Required answer is=",u)