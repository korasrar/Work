select NomEquipe
from COUREURS;

select DirecteurSportif
from EQUIPES;

select NomCoureur, PrenomCoureur
from COUREURS;

select NomEquipe
from COUREURS
where NomCoureur='ULLRICH';

select NomCoureur
from COUREURS
where NomEquipe='COFIDIS';

select NomCoureur, PrenomCoureur
from COUREURS natural join PAYS
where NPays='FRANCE';

select to_char(TempsRealise,'hh24:mi:ss') TempsRealise
from TEMPS natural join COUREURS
where NomCoureur='JALABERT' and NumEtape=3;

select NomCoureur
from COUREURS natural join EQUIPES
where DirecteurSportif='Manolo SAIZ';

select to_char(TempsRealise,'hh24:mi:ss') TempsRealise
from TEMPS natural join COUREURS natural join EQUIPES natural join ETAPES
where DirecteurSportif='Manolo SAIZ' and VilleDepart='Rouen';

select NPays 
from PAYS natural join COUREURS natural join ETAPES
where VilleArrivee='Plumelec';

select