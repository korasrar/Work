-- Q1
select VilleArrivee
from VOYAGES
where VilleDepart='Paris';
-- Q2
select *
from VOYAGES
where VilleArrivee='Amsterdam';
-- Q3
select VilleDepart,to_char(Depart,'DD-MM-YYYY-HH24:MI') as Depart
from VOYAGES 
where VilleArrivee='Amsterdam';
-- Q4
select Nom,VilleArrivee,Prix
from Clients natural join RESERVATIONS natural join VOYAGES
order by Nom,Prix;
-- Q5
select Nom,VilleDepart,Code
from Clients natural join Reservations natural join Voyages
where Ville=VilleDepart;
-- Q6
insert into Voyages values('V700', 'Paris', 'Tokyo',  to_date('01-05-2025-10:30','DD-MM-YYYY-HH24:MI'), to_date('07-05-2025-20:30','DD-MM-YYYY-HH24:MI'),600.00);
-- Q7
select VilleDepart,VilleArrivee,to_char(Depart,'DD-MM-YYYY-HH24:MI') as Depart
from Voyages
where Depart>to_date('29-1-2025-00:00','DD-MM-YYYY-HH24:MI');
-- Q8
-- Q9
select *
from Clients
where Ville!='Paris';
-- Q10
select Nom,Prenom,Ville,VilleDepart
from Clients natural join Reservations natural join Voyages
where VilleDepart='Paris' and Ville != 'Paris';
-- Q11
select Nom,Prenom
from Clients 
where ID not in (select ID from Reservations);
-- Q12
select Code
from Voyages
where code not in (select code from Reservations);
-- Q13
select Nom,Prenom
from Clients natural join RESERVATIONS natural join Voyages
where VilleDepart='Paris' and VilleArrivee='Amsterdam'
minus
select Nom,Prenom
from Clients natural join Reservations natural join Voyages
where VilleDepart='Paris' and VilleArrivee!='Amsterdam';
-- Q14
select Nom,Prenom
from Clients natural join Reservations natural join Voyages
where VilleArrivee='Amsterdam'
intersect
select Nom,Prenom
from Clients natural join Reservations natural join Voyages
where VilleArrivee='Rio De Janeiro';
-- Q15