drop table BdHabitantVoiture;

create table BdHabitantVoiture(
    Prenom Varchar2(20),
    Nom Varchar2(20),
    Sexe Varchar2(1),
    Rue Varchar2(20),
    Num Number(2),
    Ville Varchar2(10),
    MarqueV Varchar2(15),
    NomV Varchar2(10),
    AnneeV Number(5),
    CouleurV Varchar2(15),
    TypeMoteurV Varchar2(10),
    ImmV Varchar2(10)
);

insert into BdHabitantVoiture values ('Arlette', 'Fort', 'F', 'des Allouettes', 15,
 'Olivet', 'Renault', 'Zoe', 2016, 'blanche', 'electrique', 'AD-123-EF');
insert into BdHabitantVoiture values ('Jean', 'Duprack', 'M', 'des Allouettes', 12,
 'Olivet', 'Pegeot', '2008', 2015, 'noire', 'essence', 'AD-234-EF');
insert into BdHabitantVoiture values ('Arlette','Fort','F','Alesia',4,
'Paris','Renault','Clio',2017,'blanche','essence','AB-333-CC');
insert into BdHabitantVoiture values ('Arlette','Fort','F','des Allouettes',15,
'Olivet','Renault','Clio',2017,'rouge','essence','AD-567-EF');
insert into BdHabitantVoiture values ('Jean','Dubois','M','des Rivoli',12,
'Paris','Pegeot','2008',2015,'noire','essence','AD-333-EF');
insert into BdHabitantVoiture values ('Jean','Dubois','M','des Rivoli',12,
'Paris','Renault','Clio',2017,'noire','essence','AD-444-EF');
insert into BdHabitantVoiture values ('Jean','Dubois','M','des Rivoli',12,
'Paris','Toyota','Verso',2015,'bleu','diesel','AA-333-BB');
insert into BdHabitantVoiture values ('Jean','Dubois','M','des Rivoli',12,
'Paris','Toyota','Yaris',2017,'rouge','hybride','AA-333-BB');
