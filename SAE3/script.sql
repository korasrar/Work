-- rlwrap sqlplus maubert@ora12
-- drop table nomTable;
-- select * from tab;
-- purge recyclebin;

drop table REMPLACER;
drop table NOURRIR;
drop table STOCKER;
drop table Nutriment;
drop table Plante;
drop table Espece;
drop table FicheArrosage;
drop table FamilleEspece;
drop table Emplacement;
drop table Jardins;
drop table Forets;
drop table ReserveBotanique;
purge recyclebin;

create table ReserveBotanique (
    IDReserveBota number(10) PRIMARY KEY,
    NomReserve varchar2(30),
    Ville varchar2(30),
    Pays varchar2(30),
    Telephone number(20),
    Email varchar2(40),
    NomRepresentant varchar2(30),
    TypeReserve varchar2(10),
    CHECK (TypeReserve IN ('Forets', 'Jardins'))
);

create table Forets (
    IDReserveBota number(10) NOT NULL,
    Superficie number(20),
    constraint foreignkey_Forets_IDReserveBota FOREIGN KEY (IDReserveBota) REFERENCES ReserveBotanique (IDReserveBota)
);

create table Jardins (
    IDReserveBota number(10) NOT NULL,
    NomOrganisation varchar2(30),
    AdresseContact varchar2(50),
    InformationContact varchar2(80),
    constraint foreignkey_Jardins_IDReserveBota FOREIGN KEY (IDReserveBota) REFERENCES ReserveBotanique (IDReserveBota)
);

create table Emplacement (
    CodeEmplacement number(10) PRIMARY KEY,
    IDReserveBota number(10) NOT NULL,
    SituationEmplacement varchar2(10),
    constraint foreignkey_Emplacement_IDReserveBota FOREIGN KEY (IDReserveBota) REFERENCES ReserveBotanique (IDReserveBota)
);

create table FamilleEspece(
    NomFamille varchar2(20) PRIMARY KEY,
    DescriptionFamille varchar2(50),
    Catateristiques varchar2(20)
);

create table FicheArrosage (
    IDFicheArrosage number(10) PRIMARY KEY,
    QteEauSemaine number(10),
    ModeArrosage varchar2(20),
    AjustementsSaison varchar2(30)
);

create table Espece (
    IDEspece number(10) PRIMARY KEY,
    NomScientifique varchar2(30),
    NomVulgaire varchar2(30),
    DescriptionEspeces varchar2(50),
    NomFamille varchar2(20) NOT NULL,
    IDFicheArrosage number(10) NOT NULL,
    constraint foreignkey_Espece_NomFamille FOREIGN KEY (NomFamille) REFERENCES FamilleEspece (NomFamille),
    constraint foreignkey_Espece_IDFicheArrosage FOREIGN KEY (IDFicheArrosage) REFERENCES FicheArrosage (IDFicheArrosage)
);

create table Plante (
    IDPlante number(10) PRIMARY KEY,
    DatePlantation date,
    Couleur varchar2(10),
    Hauteur number(5),
    IDEspece number(10) NOT NULL,
    CodeEmplacement number(10) NOT NULL,
    constraint foreignkey_Plante_IDEspece FOREIGN KEY (IDEspece) REFERENCES Espece (IDEspece),
    constraint foreignkey_Plante_CodeEmplacement FOREIGN KEY (CodeEmplacement) REFERENCES Emplacement (CodeEmplacement)
);

create table Nutriment (
    IDNutriment number(10) PRIMARY KEY,
    NomNutriment varchar2(50),
    FormuleChimique varchar2(50),
    TypeNutriment varchar2(50)
);

create table STOCKER (
    IDNutriment number(10),
    IDReserveBota number(10),
    QteNutriment number(10),
    PRIMARY KEY (IDReserveBota, IDNutriment),
    constraint foreignkey_STOCKER_IDNutriment FOREIGN KEY (IDNutriment) REFERENCES Nutriment (IDNutriment),
    constraint foreignkey_STOCKER_IDReserveBota FOREIGN KEY (IDReserveBota) REFERENCES ReserveBotanique (IDReserveBota)
);

create table NOURRIR (
    IDEspece number(10) NOT NULL,
    IDNutriment number(10) NOT NULL,
    QteParJour number(10,5),
    PRIMARY KEY (IDEspece, IDNutriment),
    constraint foreignkey_NOURRIR_IDEspece FOREIGN KEY (IDEspece) REFERENCES Espece (IDEspece),
    constraint foreignkey_NOURRIR_IDNutriment FOREIGN KEY (IDNutriment) REFERENCES Nutriment (IDNutriment)
);

create table REMPLACER (
    IDNutrimentPrincipal number(10) NOT NULL,
    IDNutrimentSubstitut number(10) NOT NULL,
    TauxRemplacement number(4,2),
    PRIMARY KEY (IDNutrimentPrincipal, IDNutrimentSubstitut),
    constraint foreignkey_REMPLACER_IDNutrimentPrincipal FOREIGN KEY (IDNutrimentPrincipal) REFERENCES Nutriment (IDNutriment),
    constraint foreignkey_REMPLACER_IDNutrimentSubstitut FOREIGN KEY (IDNutrimentSubstitut) REFERENCES Nutriment (IDNutriment)
);

insert into ReserveBotanique values (1, 'Neo-Tokyo Forest Reserve', 'Neo-Tokyo', 'Japon', 0312345678, 'contact@neo-tokyo.jp', 'Gendo Ikari', 'Forets');
insert into ReserveBotanique values (2, 'Jardin de la NERV', 'Hakone', 'Japan', 0312345076, 'contact@nerv-garden.jp', 'Misato Katsuragi', 'Jardins');
insert into ReserveBotanique values (3, 'LCL Reserve Amazonienne', 'Manaus', 'Brasil', 5647382910, 'contact@lcl-reserve.br', 'Ryoji Kaji', 'Forets');
insert into ReserveBotanique values (4, 'Geofront Jardin Botanique', 'Tokyo-3', 'Japon', 0312345698, 'contact@geofront.jp', 'Ritsuko Akagi', 'Jardins');

insert into Forets values (1, 50000);
insert into Forets values (3, 150000);
-- Ne fonctionne pas car les identifiants (IDReserveBota) n'existe pas dans la table ReserveBotanique
insert into Forets values (5, 100000);
insert into Forets values (6, 75000);

insert into Jardins values (2, 'NERV HQ', 'GeoFront Level 3', 'contact@nerv-hq.jp');
insert into Jardins values (4, 'SEELE Organization', 'Hakone District', 'info@seele.org');
-- Ne fonctionne pas car les identifiants (IDReserveBota) n'existe pas dans la table ReserveBotanique
insert into Jardins values (7, 'Shinji Community', 'GeoFront South Wing', 'shinji@community.jp');
insert into Jardins values (8, 'Tokyo-3 Residents', 'Sector A4', 'tokyo3@gardens.jp');

insert into Emplacement values (101, 1, 'North Zone');
insert into Emplacement values (102, 1, 'East Wing');
insert into Emplacement values (103, 1, 'Main Greenhouse');
insert into Emplacement values (101, 2, 'North Zone');
insert into Emplacement values (102, 2, 'East Wing');
insert into Emplacement values (103, 2, 'South Forest');
insert into Emplacement values (101, 3, 'North Zone');
insert into Emplacement values (102, 3, 'East Wing');
insert into Emplacement values (103, 3, 'South Forest');
insert into Emplacement values (101, 4, 'North Zone');
insert into Emplacement values (102, 4, 'East Wing');
insert into Emplacement values (103, 4, 'Main Greenhouse');
-- Je peut mettre les mêmes codes d'emplacement tant que l'IDReserveBota est différent

insert into FamilleEspece values ('Asteracées', 'Chez les Astéracées, la “fleur” est en réalité composée d’un ensemble de petites fleurs réunies sur un réceptacle (le fond d’artichaut). L’ensemble est appelé un capitule.', 'Artichaut');
insert into FamilleEspece values ('Brassicacées', 'Les Brassicacées ou Crucifères possèdent toujours des fleurs à quatre sépales et à quatre pétales, bien séparés et disposés en croix.', 'Croix');

insert into FicheArrosage values (1, 10, 'Basse pression', 'Augmenter en été');
insert into FicheArrosage values (2, 20, 'Manuel', 'Réduire en hiver');
insert into FicheArrosage values (3, 15, 'Enterré', 'Constant toute année');
insert into FicheArrosage values (4, 5, 'Brume', 'Augmenter en période sèche');

insert into Espece values (1, 'Ficus elastica', 'Arbre à caoutchouc', 'Grandes feuilles vertes', 'Brassicacées', 1);
insert into Espece values (2, 'Pinus sylvestris', 'Pin sylvestre', 'Aiguilles persistantes', 'Brassicacées', 2); 
insert into Espece values (3, 'Pteridium aquilinum', 'Fougère aigle', 'Frondes délicates', 'Asteracées', 3);
insert into Espece values (4, 'Sphagnum', 'Sphaigne', 'Retient lhumidité', 'Asteracées', 4); 
-- L'insertion ne vas pas fonctionner car la famille n'est pas répertorier dans la table FamilleEspece
insert into Espece values (1, 'Ficus elastica', 'Rubber Tree', 'Large green leaves', 'Angiosperms', 1);

insert into Plante values (1001, TO_DATE('2024-04-01', 'YYYY-MM-DD'), 'Vert', 300, 1, 101);
insert into Plante values (1002, TO_DATE('2024-05-15', 'YYYY-MM-DD'), 'Vert foncée', 400, 2, 102);
insert into Plante values (1003, TO_DATE('2024-06-20', 'YYYY-MM-DD'), 'Vert clair', 50, 3, 103);
insert into Plante values (1004, TO_DATE('2024-03-30', 'YYYY-MM-DD'), 'Vert brillant', 20, 4, 104);

insert into Nutriment values (1, 'Azote', 'N2', 'Macronutriment');
insert into Nutriment values (2, 'Phosphore', 'P', 'Macronutriment'); 
insert into Nutriment values (3, 'Potassium', 'K', 'Macronutrient');
insert into Nutriment values (4, 'Calcium', 'Ca', 'Micronutrient');

insert into STOCKER values (1, 1, 500);
insert into STOCKER values (2, 2, 300);
insert into STOCKER values (3, 3, 700);
insert into STOCKER values (4, 4, 200);

insert into NOURRIR values (1, 1, 0.05);
insert into NOURRIR values (2, 2, 0.03);
insert into NOURRIR values (3, 3, 0.04);
insert into NOURRIR values (4, 4, 0.02);

insert into REMPLACER values (1, 2, 0.90);
insert into REMPLACER values (2, 3, 0.85);
insert into REMPLACER values (3, 4, 0.80);
insert into REMPLACER values (4, 1, 0.95);
