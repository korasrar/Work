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
Done 
### A.2 Modification d'image -
Done 
### A.3 Un Fichier BMP d'un type plus récent -
#### 1. Combien y-a-t-il de bits par pixel ?
Il y a 24 bits par pixels (18)16 = (24)10
#### 2. Quelle est la taille des données pixels ?
Elle est de 48 octets (30)16 = (48)10 
#### 3. Y a-t-il une compression utilisé ?
Nan il n'y a pas de compression utilisé (Type compression -> 00 00)
#### 4. Le codage des pixels a-t-il changé ? 
Non c'est tojours du RGB avec un octets par couleur
### A.4 Un Fichier BMP avec index de couleurs -
#### 1. Combien y-a-t-il de bits par pixel?
Il y a 1 bit par pixel (01)16 = (01)10
#### 2. Quelle est la taille des données pixels?
Elle est de 16 octets (10)16 = (16)10
#### 3. Y a-t-il une compression utilisée?
Non il n'y a pas de compression utilisé (Type compression -> 00 00)
#### 4. Comment sont codées les couleurs de la palette?
Les couleurs de la palette sont codées en 2^n, n est le nombre de bit par pixel donc le résultats est 2 car on a que 1 bit par pixel -> 2¹
#### 5. Quel est le nombre de couleurs dans la palette?
Les couleurs de la palette sont codées avec 02, en décimal cela donne 2 donc ma palette est constitué de 2 couleurs (adresse : 0x2E) 00 00 FF 00 | FF FF FF 00
#### 6. Le codage des pixels a-t-il changé?
Oui
#### 7. Changez la couleur rouge des pixels en bleu pour obtenir l'image ci-dessous que vous nommerez ImageBleue.bmp.
FF 00 00 00 | FF FF FF 00
#### 8. Inversez le damier : les blancs à la place des bleus et les bleus à la place des blancs, pour obtenir l'image ci-dessous.
#### 9. Modifiez le fichier  en mode index de couleurs avec okteta de façon à obtenir ceci. Enregistrez cette image sous ce nom Image3.bmp:
#### 10. Passez le fichier de l'ancien logo du Département d'Informatique en mode index de couleurs:
#### 11. A quelle adresse peut-on trouver le nombre de couleurs qu'il y a dans la palette?
#### 12. A quelle adresse dans la palette peut-on trouver la couleur à dominante "Blanc" utilisée par cette image?
#### 13. Où commence le tableau de pixel?
#### 14. En modifiant l'Hex,  placez quelques pixels bleus tout en bas de l'image.
#### 15. Que se passe-t-il si l'on diminue le nombre de couleurs dans la palette? Que se passe t-il d'un point de vue visuel? Et dans l'hexa?
### A.5 Utilisation des négatifs -