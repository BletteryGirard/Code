from acces_bdd import (ouvrir_connexion, executer_requete, valider_modifs, fermer_connexion)

def creer_bdd(db_name):
    """
    Création de la base de données SQLite

    La base, correspondant à une partie, est initialisée avec des attaques, défenses, pokémons...
    La connexion à la base est refermée à la fin de la fonction.
    """
    conn, cur = ouvrir_connexion(db_name)

    # Création des tables
    req = """create table Voiture (immatriculation text primary key,
                                    modele integer,
                                    kilometrage integer,
                                    annee_de_creation integer,
                                    boite_vitesse_auto integer
                                    etat text)"""
    executer_requete(cur, req)
    req = """create table Trajet (date_debut text
                                    date-fin"""