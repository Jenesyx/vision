DROP DATABASE if EXISTS Anwesenheit ;
Create DATABASE Anwesenheit;
Use Anwesenheit;

Create TABLE Schueler(
    Schueler_ID int AUTO_INCREMENT Primary key,
    Vorname varchar(20) not null,
    Nachname varchar(20) not null,
    Klasse varchar(5) not null,
    Gesicht longtext,
    Anwesend boolean
);

CREATE TABLE Anwesenheit(
    Anwesenheit_ID int AUTO_INCREMENT Primary key,
    Ankunftszeit Timestamp,
    Gangzeit Datetime,
    Schueler_ID int,
    FOREIGN KEY (Schueler_ID) REFERENCES Schueler(Schueler_ID)
);