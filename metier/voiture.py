class Voiture(object):
    def __init__(self, immatriculation, modele, km, annee_creation, nb_places, boite_vit, etat = "Disponible"):
        """
        Constructeur de la classe Voiture

        :param immatriculation:
        :type immatriculation: string
        :param modele:
        :type modele: string
        :param km:
        :type km: integer / float (à voir) !!!!
        :param annee_creation:
        :type annee_creation: integer ou date à voir !!!!
        :param nb_places:
        :type nb_places: integer
        :param boite_vit:
        :type boite_vit: string
        :param etat: paramètre optionnel, par défaut une voiture est dispo, définit si une voiture est dispo, en entretien, louée, en transfert.
        :type etat: string (vérifier si truc spécial pour énumération) !!!!
        """

        self._immatriculation = immatriculation
        self._modele = modele
        self._km = km
        self._annee_creation = annee_creation
        self._nb_places = nb_places
        self._boite_vit = boite_vit
        self._etat = etat

    # On définit les accesseurs des attributs
    @property
    def immatriculation(self):
        return self._immatriculation

    @property
    def modele(self):
        return self._modele

    @property
    def km(self):
        return self.km

    @property
    def annee_creation(self):
        return self._annee_creation

    @property
    def nb_places(self):
        return self._nb_places

    @property
    def boite_vit(self):
        return self._boite_vit

    @property
    def etat(self):
        return self._etat

    def __str__(self):
        return "{}, {} places, boite de vitesse {}, {} km".format(self._modele, self._nb_places, self._boite_vit, self._km)



    def changer_etat(self,nouvel_etat):
        """
        Fonction qui permet de modifier l'état de disponibilité de la voiture

        :param nouvel_etat:
        :type nouvel_etat: string (vérifier si truc spécial pour énumération) !!!!
        """
        pass

    def changer_km(self, valeur):
        """
        Fonction qui permet de mettre à jour le kilométrage d'une voiture à la fin de chaque trajet

        :param valeur: nombres de km du trajet fait (à rajouter au kilométrage de la voiture
        :type valeur: integer / float (à voir) !!!!
        """
        pass
