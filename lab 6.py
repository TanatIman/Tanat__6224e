n=int (input ("n: "))
matris=[]
listForSumOfElements=[]
S=0
#matrisi tərtib etmək üçün dövr
for i in range (0,n):
    row= list(map(int,input().split()))
    matris.append(row)

#matrisin hər sətrində 3 ə bölünən elementlərin cəmini tapıb listə əlavə etmək üçün dövr
for i in range (0,n):
    for j in range (0,n):
        if matris[i][j]%3==0:
            S+=matris[i][j]
    listForSumOfElements.append(S)
    S=0
#baş dioqanal elementlərini dəyişmə
for i in range (n):
    for j in range (n):
        if (i==j):
            matris[i][j]=listForSumOfElements[i]
#matrisin çapı
print ("The new matris is : ")
for i in range (n):
    for j in range (n):
        print (matris[i][j],end=' ')
    print ('\n' ,  end='')
    
