#2. Write a Python Program to Find HCF?
def hcf(n1,n2):
    if n1>n2:
        smaller = n2
    else:
        smaller = n1
    while(True):
        if n1%smaller==0 and n2%smaller==0:
            hcf = smaller
            break
        else:
            smaller-=1
    return hcf
print(hcf(8,12))