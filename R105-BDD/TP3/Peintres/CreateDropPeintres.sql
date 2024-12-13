drop table  EXPOSITIONTABLEAUX;
drop table GALERIES;
drop table TABLEAUX;
drop table PEINTRES;
purge recyclebin;


create table PEINTRES (
nomP Varchar2(20) primary key,
dateN date,
ecole Varchar2(20));

create table TABLEAUX(
nomP Varchar2(20),
titreTab VarChar2(30) ,
valeurEstimee number (10,2),
type VarChar2(10),
constraint KTableaux primary key (nomP, titreTab),
constraint KFPeintreExisteInTableaux foreign key (nomP) references  PEINTRES (nomP) on delete cascade);


create table GALERIES
(IdSalle number(3) primary key,
nomSalle VarChar2(20),
superfice number(4),
ville VarChar2(15));

create table EXPOSITIONTABLEAUX
(IdSalle number(3),
nomP Varchar2(20),
titreTab VarChar2(30) ,
dateDebut date,
dateFin date,
constraint KEXPO primary key (IdSalle,nomP,titreTab),
constraint KFTableauxExisteInExpo foreign key (nomP,titreTab) references  TABLEAUX (nomP,titreTab) on delete cascade,
constraint KFSalleExisteInExpo foreign key (IdSalle) references GALERIES(IdSalle) on delete cascade);