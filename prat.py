list=tuple(x for x in range(1,11) if x%2!=0)
list_1=tuple(x for x in range(1,11) if x%2==0)
ne=zip(list,list_1)
print(tuple(ne))