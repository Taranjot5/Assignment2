def add(x,y):
    print(x+y)
def sub(x,y):
    print(x-y)
def div(x,y):
    print(x/y)
def mul(x,y):
    print(x*y)
print('a=add,b=subtract,c=divide,d=multiply')
choice=input()
x=int(input('enter the first value'))
y=int(input('enter the second value'))
if(choice=='a'):
    add(x,y)
elif(choice=='b'):
    sub(x,y)
elif(choice=='c'):
    div(x,y)
else:
    mul(x,y)
