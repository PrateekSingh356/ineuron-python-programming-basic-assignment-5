#1. Write a Python Program to Find LCM?
def lcm(n1,n2):
    if n1>n2:
        greater = n1
    else:
        greater = n2
    while(True):
        if greater%n1==0 and greater%n2==0:
            lcm = greater
            break
        else:
            greater+=1
    return lcm
print(lcm(2,3))