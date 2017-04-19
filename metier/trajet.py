from agence import Agence
from client import Client
from voiture import Voiture

class Trajet(object):
    def __init__(self, date_depart, date_fin, lieu_depart, lieu_arrivee, distance, voiture, client):
        """
        Constructeur de la classe Trajet

        :param date_depart:
        :type date_depart: date
        :param date_fin:
        :type date_fin: date
        :param lieu_depart:
        :type lieu_depart: Agence
        :param lieu_arrivee:
        :type lieu_arrivee: Agence
        :param distance:
        :type distance: integer
        :param voiture:
        :type voiture: Voiture
        :param client:
        :type client: Client
        """

        self._date_depart = date_depart
        self._date_fin = date_fin
        self._lieu_depart = lieu_depart
        self._lieu_arrivee = lieu_arrivee
        self._distance = distance
        self._voiture = voiture
        self._client = client

    # On définit les accesseurs des attributs
    @property
    def date_depart(self):
        return self._date_depart

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
        return " Trajet de {} à {}, du {} au {}, en {}".format(self._lieu_depart, self._lieu_arrivee,self._date_depart,self._date_fin, self._voiture)



    def changer_lieu(self, nouveau_lieu):
        """
        Fonction qui permet de changer le lieu d'arrivée d'un trajet

        :param nouveau_lieu:
        :type nouveau_lieu: Agence
        """
        pass

    def changer_date(self, nouvelle_date):
        """
        Fonction qui permet de changer la date d'arrivée d'un trajet

        :param nouvelle_date:
        :type nouvelle_date: date
        """
        pass

