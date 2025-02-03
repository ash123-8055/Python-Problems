def create(array_2d):
    rows = int(input("Enter the number of rows: "))
    col = int(input("Enter the number of columns: "))
    arr1 = []
    for i in range(rows):
        a=[]
        for j in range(col):
            a.append(int(input(f"Enter the element at {i},{j}: ")))
        arr1.append(a)
    return arr1
array_2d=[]
print(f"The 2D Array is {create(array_2d)}")