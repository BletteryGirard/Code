from agence import Agence
from voiture import Voiture
from client import Client

class Employe(object):
    def __init__(self, nom, prenom, agence, statut):
        """
        Constructeur de la classe Employé
        :param nom:
        :type nom: string
        :param prenom:
        :type prenom: string
        :param agence: agence où travaille l'employé, ça peut être le siège.
        :type agence: Agence
        :param statut: statut de l'employé : vendeur, respo d'agence ou employé du siège
        :type statut: string
        """

        self._nom = nom
        self._prenom = prenom
        self._agence = agence
        self._statut = statut

    # On définit les accesseurs des attributs
    @property
    def nom(self):
        return self._nom

    @property
    def prenom(self):
        return self._prenom

    @property
    def agence(self):
        return self._agence

    @property
    def statut(self):
        return self._statut

    def __str__(self):
        return "{} {}, {} à l'agence {}".format(self._nom, self._prenom, self._statut, self._agence.nom)



    def creer_fiche_client(self, nom_client, prenom_client, date_naiss_client):
        """
        Fonction qui crée une nouvelle fiche client (objet client de la base de donnée). Disponible qu'aux vendeurs

        :param nom_client:
        :type nom_client: string
        :param prenom_client:
        :type prenom_client: string
        :param date_naiss_client:
        :type date_naiss_client: date
        """
        pass


    def louer_voiture(self, client, voiture, trajet):
        """
        Fonction qui initie l'ensemble du processus de location. Disponible qu'aux vendeurs

        :param client:
        :type client: Client
        :param voiture:
        :type voiture: Voiture
        :param trajet:
        :type trajet: Trajet
        """
        pass


    def creer_trajet(self, date_depart, date_arrivee, lieu_depart, lieu_arrivee, voiture, client):
        """
        Fonction qui crée un nouvel objet trajet, et l'ajoute dans la BDD. Disponible qu'aux vendeurs

        :param date_depart:
        :type date_depart: date
        :param date_arrivee:
        :type date_arrivee: date
        :param lieu_depart:
        :type lieu_depart: Agence
        :param lieu_arrivee:
        :type lieu_arrivee: Agence
        :param voiture:
        :type voiture: Voiture
        :param client:
        :type client: Client
        """
        pass


    def calculer_cout(self, trajet):
        """
        Fonction qui calcule le coût de location pour un certain trajet. Disponible qu'aux vendeurs

        :param trajet:
        :type trajet: Trajet
        """
        pass


    def transferer_voiture(self, agence_depart, agence_arrivee, liste_voiture):
        """
        Fonction qui permet de transférer certaines voitures d'une agence à une autre. Disponible qu'aux employés du siège.

        :param agence_depart:
        :type agence_depart: Agence
        :param agence_arrivee:
        :type agence_arrivee: Agence
        :param liste_voiture:
        :type liste_voiture: liste de Voiture
        """
        pass


    # voir ici comment ajouter une fonction qui met les voiture dans l'Etat "en entretien" si on choisit cette solution.
