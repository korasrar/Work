# RENDU SAE1.03 IMAGE
## A
### A.0 Expliquez ces valeurs -
L'erreur indique que la longueur de l'image et la taille du fichier ne concorde pas. On peut corriger cette erreur
Le fichier fait 816 026 octets
Dans l'en tête du fichier bmp a l'adresser 0x02 la valeur qui est attribué a la taille total du fichier en octets est : 99 73 0C 00
Elle se convertit en 000C7399, le poit faible est la valeur le plus a gauche
Cela donne 816 025 en base 10.
**816 026 ≠ 816 025**
Il faut donc modifier la valeur en ajoutant 1 a 9 pour donner : 000C739A qui s'écrirat : 9A 73 0C 00 dans Okteta
### A.1 Avec Okteta saisir de l'hexadécimal pour créer une image bmp de type Windows 2.0 -
42 4D 9A 73 0C 00 00 00 00 00 1A 00 00 00 0C 00 00 00 80 02 A9 01 01 00 18 00