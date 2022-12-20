def add(a ,b):
    ip1=isinstance(a,int)
    ip2=isinstance(b,int)
    if ip1 and ip2:
        sum=a+b
        return sum
    else:
        return'both the inputs are not of same type'

result=add(2,2.0)
print(result)