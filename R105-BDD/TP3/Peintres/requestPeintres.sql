-- Q1
select nomP,dateN,ecole
from PEINTRES 
where nomP not in (select nomP 
                    from TABLEAUX);
-- Q2
select nomP,titreTab,valeurEstimee,type
from TABLEAUX
where nomP='Monet' or nomP='Renoir';
-- Q3
select ville
from Galeries natural join EXPOSITIONTABLEAUX natural join TABLEAUX
where nomP ='Picasso'
Intersect
select ville
from Galeries natural join EXPOSITIONTABLEAUX natural join TABLEAUX
where nomP ='Monet';
-- Q4
select ville
from Galeries natural join EXPOSITIONTABLEAUX natural join TABLEAUX
where nomP ='Picasso' or nomP='Monet';
-- Q5
select ville
from Galeries natural join EXPOSITIONTABLEAUX natural join TABLEAUX
where nomP ='Picasso'
minus
select ville
from Galeries natural join EXPOSITIONTABLEAUX natural join TABLEAUX
where nomP ='Monet';
-- Q6
select ville
from Galeries natural join EXPOSITIONTABLEAUX natural join TABLEAUX
where nomP='Toulouse-Lautrec'
minus
select ville
from Galeries natural join EXPOSITIONTABLEAUX natural join TABLEAUX
where nomP!='Toulouse-Lautrec';
-- Q7
select ville 
from Galeries
minus
select ville
from Galeries natural join EXPOSITIONTABLEAUX
where nomP='Picasso';
-- Q8
select IdSalle,nomSalle,superfice,ville
from Galeries
minus
select IdSalle,nomSalle,superfice,ville
from Galeries natural join EXPOSITIONTABLEAUX;
-- Q9
select G1.ville
from Galeries G1, Galeries G2
where G1.ville=G2.ville and G1.IdSalle<G2.IdSalle;
-- Q10
select ville
from Galeries
minus 
select G1.ville
from Galeries G1, Galeries G2
where G1.ville=G2.ville and G1.IdSalle<G2.IdSalle;