from bdd.acces_bdd import executer_requete


def select_vendeur(cur, colonnes, param):
    '''
    fonction qui recupere dans la BDD les caracteristiques d'un venduer en fonction de
    son nom et prenom

    :param colonnes: colonnes dont on souhaite recuperer la valeur
    :type colonnes: liste de string
    :param param: nom et prenom du vendeur
    :type param: liste de string
    :return: caracteristique du vendeur
    :returntype: liste de string
    '''
    req = "select {} from Employe where nom = ? and prenom = ?".format(",".join(colonnes))
    results = executer_requete(cur, req, (param,))
    if len(results.fetchall()) > 0:
        return results.fetchall()
    else:
        print("Vendeur non trouvé, vérifiez l'orthographe !")



def select_voiture(cur, colonnes, param):
    '''
    fonction qui recupere dans la BDD une voiture disponible en fonction de son type,
    son modele, son nombre de places et sa boite de vitesse

    :param colonnes: colonnes dont on souhaite recuperer la valeur
    :type colonnes: liste de string
    :param param: type, modele, nombre de place et ou boite de vitesse
    :type param: liste de string
    :return: voitures dont on a choisi les caracteristiques
    :returntype: liste de string
    '''
    req = "select {} from Voiture where etat = Disponible"
    if len(colonnes) == len(param):
        for c in colonnes:
            req += " and {} = ?".format(c)
    results = executer_requete(cur, req, (param,))
    return results.fetchall()



def select_client(cur, colonnes, param):
    '''
    fonction qui recupere le client dans la BDD en fonction de son nom, prenom et
    date de naissance si il existe

    :param colonnes: colonnes dont on souhaite recuperer la valeur
    :type colonnes:
    :param param:
    :type param:
    :return:
    :returntype:
    '''
    req = "select {} from Client where nom = ? and prenom = ? and date_naissance = ?".format(",".join(colonnes))
    results = executer_requete(cur, req, (param,))
    if len(results.fetchall()) > 0:
        return results.fetchall()
    else:
        print("Client non trouvé, vérifiez l'orthographe ou créez une nouvelle fiche client!")

def creer_client():
    pass

def creer_agence():
    pass

def creer_employe():
    pass

def nouvelle_voiture():
    pass





def inserer_ligne(cur, table, colonnes, valeurs):
    """
    Ajout d'une ligne dans une table

    :param cur: curseur sur la base de données
    :param table: table dans laquelle on écrit
    :param colonnes: liste des noms des colonnes à écrire
    :param valeurs: liste des valeurs pour chacune des colonnes
    """
    if len(colonnes) != len(valeurs):
        msg = "Nombre de champs et de valeurs différents : {} - {}".format(colonnes, valeurs)
        raise ValueError(msg)

    col = ",".join(colonnes)
    val = ",".join(len(colonnes)*['?'])
    req = "insert or ignore into {} ({}) values ({})".format(table, col, val)
    executer_requete(cur, req, valeurs)
