for i in range(int(input("Enter starting point\n")),int(input("Enter ending point\n"))+1):
    j=2
    while j<=i:
        if i%j==0:
            break
        j+=1
    if j==i:
        print(j,end=' ')