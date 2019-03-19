x = []
i=0
while i <= 9:
    n = str(input("digite uma letra: "))
    x.append(n)
    i=i+1
i=0
cont=0
while i<=9:
    if x[i] not in 'aeiou':
        cont = cont +1
    i = i +1
print ("foram lidos %d consoantes" %cont)
