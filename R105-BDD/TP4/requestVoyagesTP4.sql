-- Q1
select ID,Nom,Prenom,Ville
from Clients
where Id not in (select ID from Reservations);
-- Q2 
select Code,VilleDepart,VilleArrivee,Depart,Retour,Prix
from Voyages
where Code not in (select Code from Reservations);
-- Q3 
select Nom
from Clients
where 