# --------------------------------------
# EXERCICE N°7
# -------------------------------------- 

def nun(n):
    listebool = [False,False]
    for i in range (2, n+1) :
        listebool.append(True)
    return listebool
print(nun(5))


def nun2(listebool,x):
    for i in range (len(listebool)) :
        if i%x == 0 and i != x:
            listebool[i] = False
    return listebool
print(nun2(nun(6),2))

def nun3(n):
    listeprem = []
    nun(n)
    for i in range(len(listebool)) :
        if i==2 :
            
            listebool[i] = False
    for i in range(len(listebool))  :
        if listebool[i] == True :
            listeprem.append([i])
    return listeprem
print(nun3(6))