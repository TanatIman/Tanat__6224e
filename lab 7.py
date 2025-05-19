lst=[]
newlist=[]
product=1
positivelist=[]
n=int(input('n : ' ))
for i in range (n):
    number=int(input("number:" ))
    lst.append(number)
file=open("list.txt", 'w')
for i in lst:
    file.write (str(i) +'\n')
file.close()
selectedNumbers=[]
file2=open("list.txt" , 'r')
for line in file2:
    number=int(line.strip())
    newlist.append(number)
file2.close()
for i in newlist:
    if(i<0):
        break
    product*=i
    positivelist.append(i)

file3=open("positive.txt" ,'w')
for i in positivelist:
    file3.write(str(i) + "\n")
file3.close()

print (product)




