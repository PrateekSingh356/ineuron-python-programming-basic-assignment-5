#5. Write a Python Program to Make a Simple Calculator with 4 basic mathematical operations?
def calc(op,x,y):
    if op=='add':
        return x+y
    elif op=='sub':
        return x-y
    elif op=='mul':
        return x*y
    elif op=='divide' and y>0:
        return x/y
print({"add":'addition',
       'sub':'subtract',
       'mul':'multiply',
       'divide':'divide'})
operation = input("enter the operation : ")
print(calc(operation,4,5))