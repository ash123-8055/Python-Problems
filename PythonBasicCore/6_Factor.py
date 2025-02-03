def prime_factor(number):
    n=number**0.5
    for i in range(2,int(n)+1):
        if number%i==0:
            print(f"{i},{number//i} is a prime factor of {number}")
        else:
            continue
            #print(f"{i} is not a prime factor of {number}")


number=int(input("Enter the number to find the factors: "))
prime_factor(number)
