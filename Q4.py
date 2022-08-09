n=input('enter the value :')
i=n
count=0
while(i>0):
    i=i//10
    count=count+1
add=0
i=n
while(i>0):
    digit=i%10
    x=1
    pro=1
    while(x<=count):
        pro=pro*digit
        x=x+1
    add=add+pro
    i=i//10
if(add==n):
    print('the number is armstrong')
else:
    print('the number is not armstrong')
