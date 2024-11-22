select nomcl, prenom
from client;

select refarticle
from article
where prixht > 50;

select adressepointdist
from pointdistribution natural join client
where nomcl='Ayanami' and prenom='Rei';

select refarticle, prixht, 