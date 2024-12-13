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
where months_between(SYSDATE,Depart)>3;
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
where VilleArrivee='Rio de Janeiro';
-- Q15
select Nom,Prenom
from Clients natural join Reservations natural join Voyages
where VilleArrivee='Amsterdam'
union
select Nom,Prenom
from Clients natural join Reservations natural join Voyages
where VilleArrivee='Rio de Janeiro';
-- Q16
select C1.Nom,C2.Nom,C1.Ville
from Clients C1,Clients C2
where C1.Ville=C2.Ville and C1.ID<C2.ID;
-- Q17
select V1.Code,V2.Code,V1.Prix
from Voyages V1,Voyages V2
where V1.Prix=V2.Prix and V1.Code<V2.Code;
-- Q18
select R1.ID,R1.Code,R2.Code
from Reservations R1,Reservations R2, Clients C1
where R1.ID=C1.ID and R2.ID=C1.ID and R1.Code!=R2.Code and R1.Code<R2.Code;
-- Q19 
select Nom,Prenom
from Clients 
where ID in (select ID from Reservations)
minus
select C1.Nom,C1.Prenom
from Reservations R1,Reservations R2, Clients C1
where R1.ID=C1.ID and R2.ID=C1.ID and R1.Code!=R2.Code and R1.Code<R2.Code;
-- Q20


