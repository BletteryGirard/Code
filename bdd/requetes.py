from bdd.acces_bdd import executer_requete

def insert_into(cur, table, colonnes, valeurs):
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

    exp_col = ",".join(colonnes)
    exp_val = ",".join(len(colonnes)*['?'])
    req = "insert into {} ({}) values ({})".format(table, exp_col, exp_val)
    executer_requete(cur, req, valeurs)
