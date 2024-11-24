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
    PRIMARY KEY IDReserveBota number(10),
    NomReserve varchar2(30),
    Ville varchar2(30),
    Pays varchar2(30),
    Telephone number(20),
    Email varchar2(40),
    NomRepresentant varchar2(30),
    TypeReserve varchar2(10) (TypeReserve IN ('Forets', 'Jardins'))
);

create table Forets (
    IDReserveBota number(10),
    Superficie number(20),
    constraint foreignkey_Forets_IDReserveBota FOREIGN KEY (IDReserveBota) REFERENCES ReserveBotanique (IDReserveBota)
);

create table Jardins (
    IDReserveBota number(10),
    NomOrganisation varchar2(30),
    AdresseContact varchar2(50),
    InformationContact varchar2(80),
    constraint foreignkey_Jardins_IDReserveBota FOREIGN KEY (IDReserveBota) REFERENCES ReserveBotanique (IDReserveBota)
);

create table Emplacement (
    PRIMARY KEY CodeEmplacement number(10),
    IDReserveBota number(10),
    SituationEmplacement varchar2(10),
    constraint foreignkey_Emplacement_IDReserveBota FOREIGN KEY (IDReserveBota) REFERENCES ReserveBotanique (IDReserveBota)
);

create table FamilleEspece(
    PRIMARY KEY NomFamille varchar2(20),
    DescriptionFamille varchar2(50),
    Catatéristiques varchar2(20)
);

create table FicheArrosage (
    PRIMARY KEY IDFicheArrosage number(10),
    QteEauSemaine number(10),
    ModeArrosage varchar2(20),
    AjustementsSaison varchar2(30)
);

create table Espece (
    PRIMARY KEY IDEspece number(10),
    NomScientifique varchar2(30),
    NomVulgaire varchar2(30),
    DescriptionEspeces varchar2(50)
    NomFamille varchar2(20),
    IDFicheArrosage number(10),
    constraint foreignkey_Espece_NomFamille FOREIGN KEY (NomFamille) REFERENCES FamilleEspece (NomFamille),
    constraint foreignkey_Espece_IDFicheArrosage FOREIGN KEY (IDFicheArrosage) REFERENCES FicheArrosage (IDFicheArrosage)
);

create table Plante (
    PRIMARY KEY IDPlante number(10),
    DatePlantation DATE,
    Couleur varchar2(10),
    Hauteur number(5)
    IDEspece number(10),
    CodeEmplacement number(10),
    constraint foreignkey_Plante_IDEspece FOREIGN KEY (IDEspece) REFERENCES Espece (IDEspece),
    constraint foreignkey_Plante_CodeEmplacement FOREIGN KEY (CodeEmplacement) REFERENCES Emplacement (CodeEmplacement)
);

create table Nutriment (
    PRIMARY KEY IDNutriment number(10);
    NomNutriment varchar2(50),
    FormuleChimique varchar2(50),
    TypeNutriment varchar2(50),
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
    IDEspece number(10),
    IDNutriment number(10),
    QteParJour number(10,5),
    PRIMARY KEY (IDEspece, IDReserveBota),
    constraint foreignkey_NOURRIR_IDEspece FOREIGN KEY (IDEspece) REFERENCES Espece (IDEspece),
    constraint foreignkey_NOURRIR_IDNutriment FOREIGN KEY (IDNutriment) REFERENCES Nutriment (IDNutriment)
);

create table REMPLACER (
    IDNutrimentPrincipal number(10),
    IDNutrimentSubstitut number(10),
    TauxRemplacement number(4,2),
    PRIMARY KEY (IDNutrimentPrincipal, IDNutrimentSubstitut),
    constraint foreignkey_REMPLACER_IDNutriment FOREIGN KEY (IDNutriment) REFERENCES Nutriment (IDNutriment),
    constraint foreignkey_REMPLACER_IDNutriment FOREIGN KEY (IDNutriment) REFERENCES Nutriment (IDNutriment)
);
