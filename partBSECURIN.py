dieA = [0, 1, 2, 3, 4, 0] #allowed values in dieA
dieB = []
for i in range(2, 13): #starting from 2 because if 1 is present there is one chance of getting the output of 1 which is not valid
    if i <= 4:
        dieB.append(i)
    else:
        if i not in dieA:
            dieB.append(i)
if 8 not in dieB:
    dieB.append(8)
dieB=dieB[:5]+[8]
#checking if we get the summation output(2 to 12)
li=[2,3,4,5,6,7,8,9,10,11,12];k=0;c=0;pl=[];flag=0
for i in dieA:
    for j in dieB:
        op=i+j
        pl.append(op)
pl=list(set(pl))
if li==pl:
    #all values are present 
    flag=1 
if flag==1:    
    print("dieA :", dieA)
    print("dieB :", dieB)
