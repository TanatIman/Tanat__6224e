A_n=[1,2,4,62,-4,5,6,7,0,9,12,53,-23,132,-67]
x=0
for i in range(len(A_n)):
    if A_n[i]<=0:
        x=i
        break
S=0
for i in range (0,x):
    S+=A_n[i]
print (S)
    
