CREATE TABLE Emplacement (
    PRIMARY KEY (Code_Emplacement),
    Code_Emplacement VARCHAR2(8) NOT NULL,
    IDreservbota     NUMBER() NOT NULL,
    UNIQUE (IDreservbota)
);

CREATE TABLE Especes (
    PRIMARY KEY (IDEspeces),
    IDEspeces        VARCHAR(42) NOT NULL,
    Nom_Scientifique VARCHAR2(255),
    Nom_Vulgaire     VARCHAR2(255),
    Description      TEXT,
    IDPlante         VARCHAR(42) NOT NULL,
    Nom_Famille      VARCHAR2(255) NOT NULL
);

CREATE TABLE Famille_Especes (
    PRIMARY KEY (Nom_Famille),
    Nom_Famille      VARCHAR2(255) NOT NULL,
    Description      TEXT,
    Caracteristiques VARCHAR(42)
);

CREATE TABLE Fiches_Arrosages (
    PRIMARY KEY (IDFiche),
    IDFiche                        VARCHAR(42) NOT NULL,
    Quantitte_Eau_Semaine          VARCHAR(42),
    Mode_Arrosage                  VARCHAR(42),
    Ajust_Saisons_Condi_CLimatique VARCHAR(42)
);

CREATE TABLE IS_A (
    PRIMARY KEY (Superficie, Nom_Orga, IDreservbota),
    Superficie   NUMBNER(10) NOT NULL,
    Nom_Orga     VARCHAR(255) NOT NULL,
    IDreservbota NUMBER() NOT NULL
);

CREATE TABLE Jardins (
    PRIMARY KEY (Nom_Orga),
    Nom_Orga VARCHAR(255) NOT NULL,
    Adresse  VARCHAR(30),
    Contact  NUMBER(10)
);

CREATE TABLE Nourri (
    PRIMARY KEY (IDEspeces, IDNutriments),
    IDEspeces    VARCHAR(42) NOT NULL,
    IDNutriments VARCHAR(42) NOT NULL
);

CREATE TABLE Nutriment (
    PRIMARY KEY (IDNutriments),
    IDNutriments      VARCHAR(42) NOT NULL,
    Nom_Nutriments    VARCHAR2(255),
    Formule_Chimique  VARCHAR(42),
    Type              VARCHAR(42),
    Taux_Remplacement VARCHAR(42)
);

CREATE TABLE Plante (
    PRIMARY KEY (IDPlante),
    IDPlante         VARCHAR(42) NOT NULL,
    Dateplantation   VARCHAR(42),
    Couleur          VARCHAR2(50),
    Hauteur          DECIMAL(10,2),
    Emplacement      VARCHAR(42),
    Code_Emplacement VARCHAR2(8) NOT NULL
);

CREATE TABLE Remplacer (
    PRIMARY KEY (IDNutriments_1, IDNutriments_2),
    IDNutriments_1 VARCHAR(42) NOT NULL,
    IDNutriments_2 VARCHAR(42) NOT NULL
);

CREATE TABLE Reserve_Botanique (
    PRIMARY KEY (IDreservbota),
    IDreservbota NUMBER() NOT NULL,
    Nomreserv    VARCHAR2(42),
    Ville        VARCHAR2(100),
    Pays         VARCHAR2(100),
    Tel          VARCHAR2(20),
    Email        VARCHAR2(255),
    Nom_Rep      VARCHAR2(255),
    Type_Reserv  VARCHAR(42)
);

CREATE TABLE Zone_Geo_Origine (
    PRIMARY KEY (Zone_Geo),
    Zone_Geo  VARCHAR(42) NOT NULL,
    IDEspeces VARCHAR(42) NOT NULL
);

ALTER TABLE Emplacement ADD FOREIGN KEY (IDreservbota) REFERENCES Reserve_Botanique (IDreservbota);

ALTER TABLE Especes ADD FOREIGN KEY (Nom_Famille) REFERENCES Famille_Especes (Nom_Famille);
ALTER TABLE Especes ADD FOREIGN KEY (IDPlante) REFERENCES Plante (IDPlante);

ALTER TABLE IS_A ADD FOREIGN KEY (IDreservbota) REFERENCES Reserve_Botanique (IDreservbota);
ALTER TABLE IS_A ADD FOREIGN KEY (Nom_Orga) REFERENCES Jardins (Nom_Orga);

ALTER TABLE Nourri ADD FOREIGN KEY (IDNutriments) REFERENCES Nutriment (IDNutriments);
ALTER TABLE Nourri ADD FOREIGN KEY (IDEspeces) REFERENCES Especes (IDEspeces);

ALTER TABLE Plante ADD FOREIGN KEY (Code_Emplacement) REFERENCES Emplacement (Code_Emplacement);

ALTER TABLE Remplacer ADD FOREIGN KEY (IDNutriments_2) REFERENCES Nutriment (IDNutriments);
ALTER TABLE Remplacer ADD FOREIGN KEY (IDNutriments_1) REFERENCES Nutriment (IDNutriments);

ALTER TABLE Zone_Geo_Origine ADD FOREIGN KEY (IDEspeces) REFERENCES Especes (IDEspeces);