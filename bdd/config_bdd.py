from acces_bdd import (ouvrir_connexion, executer_requete, valider_modifs, fermer_connexion)

import requetes as r


def creer_bdd(db_name):
    """
    Création de la base de données SQLite

    La connexion à la base est refermée à la fin de la fonction.
    """
    conn, cur = ouvrir_connexion(db_name)

    # Création des tables
    req = """create table if not exists Statut (statut text primary key)"""
    executer_requete(cur, req)

    req = """create table if not exists Etat (etat text primary key)"""
    executer_requete(cur, req)

    req = """create table if not exists Agence (nom text primary key)"""
    executer_requete(cur, req)

    req = """create table if not exists Client (num_client integer primary key,
                                                nom text,
                                                prenom text,
                                                date_naissance integer)"""
    executer_requete(cur, req)

    req = """create table if not exists Voiture (immatriculation text primary key,
                                                    type text,
                                                    modele text,
                                                    kilometrage integer,
                                                    annee_de_creation integer,
                                                    nb_places integer,
                                                    boite_vitesse_auto integer,
                                                    agence text,
                                                    etat text,
                                                    foreign key(agence) references Agence(nom),
                                                    foreign key(etat) references Etat(etat))"""
    executer_requete(cur, req)

    req = """create table if not exists Employe (nom text,
                                                    prenom text,
                                                    agence text,
                                                    statut text,
                                                    foreign key(agence) references Agence(nom),
                                                    foreign key(statut) references Statut(statut)
                                                    primary key(nom,prenom))"""
    executer_requete(cur, req)

    req = """create table if not exists Trajet (numero_trajet integer primary key autoincrement,
                                                    date_debut real,
                                                    date_fin real,
                                                    distance integer,
                                                    lieu_depart text,
                                                    lieu_arrivee text,
                                                    client text,
                                                    voiture text,
                                                    cout integer,
                                                    foreign key(lieu_depart) references Agence(nom),
                                                    foreign key(lieu_arrivee) references Agence(nom),
                                                    foreign key(client) references Client(num_client),
                                                    foreign key(voiture) references Voiture(immatriculation))"""
    executer_requete(cur, req)

    valider_modifs(conn)

    # Insertion des éléments
    etats = ('Disponible', 'Empruntée', 'En transfert', 'En entretien')
    for e in etats:
        r.inserer_ligne(cur, 'Etat', ('etat',), (e,))
    valider_modifs(conn)

    statuts = ('Vendeur', 'Respo', 'Siege')
    for s in statuts:
        r.inserer_ligne(cur, 'Statut', ('statut',), (s,))
    valider_modifs(conn)

    agences = ('Siege', 'Paris Nord', 'Paris Sud','Moret-sur-Loing Gros-Bois', 'Villeneuve-Saint-Georges Quartier Nord', 'Flers Saint-Michel')
    for a in agences:
        r.inserer_ligne(cur, 'Agence', ('nom',), (a,))
    valider_modifs(conn)

    voitures = (
        ('AA000AA', 'Citadine', 'Clio', 35000, 1999, 5, 0, 'Paris Nord', 'Disponible'),
        ('BB111BB', 'Citadine', '4L', 125000, 1985, 4, 0, 'Saint-Michel', 'En entretien'),
        ('CC222CC', 'Familial', 'Trafic', 90000, 2000, 9, 1, 'Quartier Nord', 'Empruntée'),
        ('DD333DD', 'Utilitaire', 'Trafic', 135000, 1999, 3, 0, 'Quartier Nord', 'En transfert'),
        ('EE444EE', 'Berline', 'A8', 10000, 2010, 5, 1, 'Quartier Nord', 'Disponible')
    )
    colonnes = ('immatriculation',
                'type',
                'modele',
                'kilometrage',
                'annee_de_creation',
                'nb_places',
                'boite_vitesse_auto',
                'agence',
                'etat')
    for v in voitures:
        r.inserer_ligne(cur, 'Voiture', colonnes, v)
    valider_modifs(conn)

    employes = (
        ('Girard', 'Alexandre', 'Saint-Michel', 'Respo'),
        ('Blettery', 'Emile', 'Quartier Nord', 'Respo'),
        ('Thill', 'Florian', 'Saint-Michel', 'Vendeur'),
        ('Bourassin', 'Emmanuel', 'Siege', 'Siege')
    )
    colonnes = ('nom', 'prenom', 'agence', 'statut')
    for e in employes:
        r.inserer_ligne(cur, 'Employe', colonnes, e)
    valider_modifs(conn)

    clients = (
        ('Delgrange', 'Clement', 14),
        ('Costes', 'Benoit', 15)
    )
    colonnes = ('nom', 'prenom', 'date_naissance')
    for c in clients:
        r.inserer_ligne(cur, 'Client', colonnes, c)
    valider_modifs(conn)

    fermer_connexion(cur, conn)

if __name__ == "__main__":
    creer_bdd('location.db')
