-- rlwrapsqlplus maubert@ora12
-- drop table nomTable;
-- select * from tab;
-- purge recyclebin;

create table CLIENT (
    codecl number(10),
    nomcl varchar2(30),
    prenom varchar2(30),
    adressecl varchar2(50),
    emailcl varchar2(30)
)

create table ATICLE(
    refarticle number(10),
    nomarticle varchar2(35),
    prixht float(8),
    tva number(2),
    qtestock number(35)
);


insert into client values(12,'Ayanami','Rei','38 rue du crampté','reiayanami@nerv.com')