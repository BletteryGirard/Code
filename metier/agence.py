class Agence(object):
    def __init__(self, ville, nom, liste_client = [], liste_voiture = []):
        """
        Constructeur de la classe Agence

        :param ville: nom de la ville ou se situe l'agence correpondante
        :type ville: string
        :param nom: nom de l'agence, doit être différent de ceux existants ! Même si villes différentes (cf BDD, à voir peut être)
        :type nom: string
        :param liste_client: liste des clients ayant deja fait une location dans une agence
        :type liste_client: liste de Client
        :param liste_voiture: liste des voitures appartenants aux différentes agences
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
        return "{}, {}".format(self._nom, self._ville)

