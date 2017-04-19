import sqlite3
import ihm.console as ihm


def ouvrir_connexion(db_name):
    """
    Connexion à une base de données
    """
    conn = sqlite3.connect(db_name)
    # création d'un curseur pour accéder à cette base
    cur = conn.cursor()
    return conn, cur


def executer_requete(cur, req, variables=()):
    """
    Requête à la base de données
    """
    try:
        res = cur.execute(req, variables)
    except sqlite3.ProgrammingError:
        # nombre d'arguments incorrects
        ihm.afficher("ERREUR : nombre d'arguments passés à la requête incorrects : {}".format(req))
    except sqlite3.OperationalError:
        # erreur liée à une opération dans la bdd
        ihm.afficher("ERREUR : requête non conforme {}".format(req))
    except sqlite3.DataError:
        # format inséré inadéquat
        ihm.afficher("ERREUR : données insérées dans la BDD au mauvais format : {}".format(req))
    except sqlite3.IntegrityError:
        # violation d'une contrainte du schéma de la bdd
        ihm.afficher("ERREUR : requête viole contrainte d'intégrité de la BDD : {}".format(req))
    else:
        return res


def valider_modifs(conn):
    """
    Valider la transaction
    """
    conn.commit()


def fermer_connexion(cur, conn):
    """
    Fermeture de la connexion
    """
    cur.close()
    conn.close()


if __name__ == '__main__':
    pass

