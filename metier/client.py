class Client(object):
    def __init__(self, nom, prenom, date_naiss, liste_trajets = []):
        """
        Constructeur de la classe Client

        :param nom: nom du client
        :type nom: string
        :param prenom: prenom du client
        :type prenom: string
        :param date_naiss: date de naissance du client au format date
        :type date_naissance: date
        """

        self._nom = nom
        self._prenom = prenom
        self._date_naiss = date_naiss

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


    def __str__(self):
        return "{} {}, né(e) le {}".format(self._nom, self._prenom, self._date_naiss)





