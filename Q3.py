firstnumber=0
print(firstnumber)
secondnumber=1
print(secondnumber)
num=input()
i=0
while i < num:
    a=firstnumber+secondnumber
    print(a)
    i=i+1
    firstnumber=secondnumber
    secondnumber=a
    
