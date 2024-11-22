-- rlwrap sqlplus maubert@ora12
-- drop table nomTable;
-- select * from tab;
-- purge recyclebin;
drop table contenir;
drop table expediteur;
drop table colis;
drop table commande;
drop table article;
drop table client;
drop table pointdistribution;
purge recyclebin;

create table pointdistribution (
    refpointdist number(10),
    adressepointdist varchar2(30),
    constraint clepointdist PRIMARY KEY (refpointdist)
);

create table client (
    codecl number(10),
    nomcl varchar2(30),
    prenom varchar2(30),
    adressecl varchar2(50),
    emailcl varchar2(30),
    refpointdist number(10),
    constraint cleclient primary key (codecl),
    constraint foreignkey_client_refpoindist FOREIGN KEY (refpointdist) REFERENCES pointdistribution (refpointdist) 
);

create table article(
    refarticle number(10),
    nomarticle varchar2(35),
    prixht float(8),
    tva number(4, 2),
    qtestock number(35),
    constraint cleart primary key (refarticle)
);

create table commande(
    numcom number(10),
    datecom date,
    codecl number(10),
    constraint clecom primary key (numcom)
);

create table colis(
    numcom number(10),
    numcolis number(10),
    indretrait varchar2(2),
    constraint clecolis primary key (numcolis, numcom),
    constraint foreignkey_colis_numcom FOREIGN KEY (numcom) REFERENCES commande (numcom)
);

create table expediteur(
    numcom number(10),
    numcolis number(10),
    refarticle number(10),
    qteexp number(10),
    qteacpt number(10), 
    constraint cleexpediteur primary key (numcolis, numcom, refarticle),
    constraint foreignkey_expediteur_numcolis FOREIGN KEY (numcolis,numcom) REFERENCES colis (numcolis,numcom),
    constraint foreignkey_expediteur_refarticle FOREIGN KEY (refarticle) REFERENCES article (refarticle)
);

create table contenir(
    numcom number(10),
    refarticle number(10),
    qtecom number(10), 
    constraint clecontenir primary key (refarticle, numcom),
    constraint foreignkey_contenir_numcom FOREIGN KEY (numcom) REFERENCES commande (numcom),
    constraint foreignkey_contenir_refarticle FOREIGN KEY (refarticle) REFERENCES article (refarticle)
);

insert into pointdistribution values(
    '123',
    '5 rue de la nerv'
);

insert into pointdistribution values(
    '124',
    '6 rue de la nerv'
);

insert into pointdistribution values(
    '125',
    '7 rue de la nerv'
);

insert into client values(
    12,
    'Ayanami',
    'Rei',
    '38 rue du crampte',
    'reiayanami@nerv.com',
    '123'
);

insert into client values(
    13,
    'Ikari',
    'Shinji',
    '38 rue de lapanyan',
    'shinjiiari@nerv.com',
    '124'
);

insert into article values(
    1,
    'Figurine EVA01',
    25,
    20.00,
    35
);

insert into article values(
    2,
    'Figurine EVA02',
    30,
    20.00,
    20
);

insert into article values(
    3,
    'Figurine EVA03',
    55,
    20.00,
    20
);

insert into commande values(
    1,
    24/12/2024,
    12,
)

insert into contenir values(
    1,
    1,
)