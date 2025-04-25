x=input("Enter any string\n")
Vowels="AEIOUaeiou"
for i in x:
    for j in Vowels:
        if i==j:
            print(i)