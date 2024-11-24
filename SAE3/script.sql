-- rlwrap sqlplus maubert@ora12
-- drop table nomTable;
-- select * from tab;
-- purge recyclebin;

create table ReserveBotanique (
    PRIMARY KEY IDReserveBota number(10),
    NomReserve varchar2(30),
    Ville varchar2(30),
    Pays varchar2(30),
    Telephone number(20),
    Email varchar2(40),
    NomRepresentant varchar2(30),
    TypeReserve varchar2(10)
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
    PRIMARY KEY CodeEmplacement
);

create table FamilleEpece(
    PRIMARY KEY NomFamille varchar2(20),
    DescriptionFamille varchar2(50),
    Catatéristiques varchar2(20)
);

create table Espece (
    PRIMARY KEY IDEspece number(10),
    NomScientifique varchar2(30),
    NomVulgaire varchar2(30),
    DescriptionEspeces varchar2(50)  
);

create table Plante (
    PRIMARY KEY IDPlante number(10),
    DatePlantation Date,
    Couleur varchar2(10),
    Hauteur number(5)        
);

create table FicheArrosage (
    PRIMARY KEY IDFiche number(10),
    QteEauSemaine number(10),
    ModeArrosage varchar2(20),
    AjustementsSaison varchar2(30)
);
