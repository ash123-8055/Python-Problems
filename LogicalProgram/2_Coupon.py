import random

def coupon(number):
    arr=[]
    string=""
    for i in range(0,number+1):
        a=random.randint(0,9)
        if a not in arr:
            arr.append(a)
            string+=str(a)

    print(string)


number=int(input("Enter how many number do you need to generate the distinct coupon: "))
coupon(number)