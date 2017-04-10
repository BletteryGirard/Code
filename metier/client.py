class Client(object):
    def __init__(self, nom, prenom, date_naiss, liste_trajets = []):
        """
        Constructeur de la classe Client

        :param nom:
        :type nom: string
        :param prenom:
        :type prenom: string
        :param date_naiss:
        :type date_naiss: date
        :param liste_trajets: liste des trajets déjà effectués par le client, si non renseigné, elle est vide, c'est un nouveau client
        :type liste_trajets: liste de Trajet
        """

        self._nom = nom
        self._prenom = prenom
        self._date_naiss = date_naiss
        self._liste_trajets = liste_trajets

    # On définit les accesseurs des attributs
    @property
    def nom(self):
        return self._nom

    @property
    def prenom(self):
        return self._prenom

    @property
    def date_naiss(self):
        return self._date_naiss

    @property
    def liste_trajets(self):
        return self._liste_trajets

    def __str__(self):
        return "{} {}, né(e) le {}".format(self._nom, self._prenom, self._date_naiss)





