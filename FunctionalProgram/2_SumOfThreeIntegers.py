def sumOfThreeIntegers(arr):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            for k in range(j+1,len(arr)):
                if arr[i]+arr[j]+arr[k] == 0:
                    print(f"The Three integers are {arr[i]},{arr[j]},{arr[k]}")

number = int(input("Enter the number of elements: "))
arr = map(int,input("Enter the elements: ").split())
arr=list(arr)
print(f"The Input Array is {arr}")
sumOfThreeIntegers(arr)
