arr=list(map(int,input("enter elements:").split()))
target=int(input("enter target:"))
n=len(arr)
for i in range(0,n):
    for j in range(n-1):
        if i>target:
            j--
        else:
            i++
print(i)
print(j)
