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
from Clients natural join Reservations
where ID not in (select R1.Id 
                from Reservations R1, Reservations R2 
                where R1.Code!=R2.Code and R1.Id=R2.Id);
-- Q4
select Code
from Voyages
where Prix>=ALL(select prix from Voyages);

select Code
from Voyages
where prix=(select MAX(prix) from Voyages);
-- Q5 
select Code
from Voyages
where Prix<=ALL(select prix from Voyages);
-- Q6 
select v1.Code,v1.VilleDepart,v1.VilleArrivee,v1.Prix
from Voyages v1, Voyages v2
where v1.VilleArrivee=v2.VilleArrivee and v1.VilleDepart=v2.VilleDepart and v1.Code!=v2.Code;

select v1.Code,v1.VilleDepart,v1.VilleArrivee,v1.Prix
from Voyages v1
where exists (select * from Voyages v2 where v1.VilleArrivee=v2.VilleArrivee and v1.VilleDepart=v2.VilleDepart and v1.Code!=v2.Code);
-- Q7
select v1.Code,v1.VilleDepart,v1.VilleArrivee,v1.Prix
from Voyages v1
where not exists (select * from Voyages v2 where v1.VilleArrivee=v2.VilleArrivee and v1.VilleDepart=v2.VilleDepart and v1.Code!=v2.Code);
-- Q8
select Nom
from Clients
where not exists (select code from Voyages where VilleArrivee='Amsterdam'
                minus 
                select code from Reservations where Reservations.id=Clients.id);
-- Q9
select Code
from Voyages
where exists (select Id from Clients natural join Reservations where ville='Paris');

select
