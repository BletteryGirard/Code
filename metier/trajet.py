from agence import Agence
from client import Client
from voiture import Voiture

class Trajet(object):
    def __init__(self, date_debut, date_fin, lieu_depart, lieu_arrivee, distance, voiture, client, cout):
        """
        Constructeur de la classe Trajet

        :param date_debut: date de debut de la location
        :type date_debut: date
        :param date_fin: date de fin de la location
        :type date_fin: date
        :param lieu_depart: lieu de depart de la location correspondant a une agence
        :type lieu_depart: Agence
        :param lieu_arrivee: lieu d'arrivee de la location correspondant a une agence
        :type lieu_arrivee: Agence
        :param distance: distance du trajet effectue par le client
        :type distance: integer
        :param voiture: voiture choisie par le client
        :type voiture: Voiture
        :param client: client qui effectue une location
        :type client: Client
        :param
        """

        self._date_debut = date_debut
        self._date_fin = date_fin
        self._lieu_depart = lieu_depart
        self._lieu_arrivee = lieu_arrivee
        self._distance = distance
        self._voiture = voiture
        self._client = client

    # On définit les accesseurs des attributs
    @property
    def date_debut(self):
        return self._date_debut

    @property
    def date_fin(self):
        return self._date_fin

    @property
    def lieu_depart(self):
        return self._lieu_depart

    @property
    def lieu_arrivee(self):
        return self._lieu_arrivee

    @property
    def distance(self):
        return self._distance

    @property
    def voiture(self):
        return self._voiture

    @property
    def client(self):
        return self._client

    def __str__(self):
        return " Trajet de {} à {}, du {} au {}, en {}".format(self._lieu_depart, self._lieu_arrivee,self._date_debut,self._date_fin, self._voiture)



    def changer_lieu_arrivee(self, nouveau_lieu):
        """
        Fonction qui permet de changer le lieu d'arrivée d'un trajet

        :param nouveau_lieu: nouveau lieu d'arrivee de la location correspondant à une agence
        :type nouveau_lieu: Agence
        """
        self.lieu_arrivee = nouveau_lieu

    def changer_date_fin(self, nouvelle_date):
        """
        Fonction qui permet de changer la date d'arrivée d'un trajet

        :param nouvelle_date: nouvelle date de rendu de la location
        :type nouvelle_date: date
        """
        self.date_fin = nouvelle_date

