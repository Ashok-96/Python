arr=[1,6,3,6,6,1]
unique=list()
for i in range(0, len(arr)):
    for j in range(0,len(arr)):
        if arr[i]==arr[j]:
            break
    if i==j:
        unique.append(arr[i])
    else:
        print(f'{arr[i]} is repeated at {i+1} position')
res=sorted(unique,reverse=False) 
print(f'the unique numbers are:{res}')