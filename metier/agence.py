class Agence(object):
    def __init__(self, ville, nom, liste_client, liste_voiture):
        """
        Constructeur de la classe Agence

        :param ville:
        :type ville: string
        :param nom:
        :type nom: string
        :param liste_client:
        :type liste_client: liste de Client
        :param liste_voiture:
        :type liste_voiture: liste de Voiture
        """

        self._ville = ville
        self._nom = nom
        self._liste_client = liste_client
        self._liste_voiture = liste_voiture

    # On définit les accesseurs des attributs
    @property
    def ville(self):
        return self._ville

    @property
    def nom(self):
        return self._nom

    @property
    def liste_client(self):
        return self._liste_client

    @property
    def liste_voiture(self):
        return self._liste_voiture

    def __str__(self):
        return self._nom



    def calc_stats(self):
        """
        Fonction qui permet d'effectuer les calculs statistiques sur une Agence

        :return:
        """
        pass