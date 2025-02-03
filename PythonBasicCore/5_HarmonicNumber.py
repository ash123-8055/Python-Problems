def harmonicNumber(n):
    if n==0:
        return 0
    else:
        return 1/n + harmonicNumber(n-1)

n=int(input("Enter the number to find the harmonic number: "))
print(f"The {n}'th Harmonic number is {harmonicNumber(n)}")