# --------------------------------------
# EXERCICE N°7
# -------------------------------------- 

def nun(n):
    listebool = [False,False]
    for i in range (2, n+1) :
        listebool.append(True)
    return listebool


def nun2(listebool,x):
    for i in range (len(listebool)) :
        if i%x == 0 and i != x:
            listebool[i] = False
    return listebool

def crible(n):
    listeprem = []
    listebool = nun(n)
    for i in range(2,len(listebool)) :
            nun2(listebool,i)
    for i in range(len(listebool)) :
        if listebool[i] == True :
            listeprem.append(i)
    return listeprem
print(crible(120))