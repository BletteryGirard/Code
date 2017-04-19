from agence import Agence
from voiture import Voiture
from client import Client


class Employe(object):
    def __init__(self, nom, prenom, agence):
        """
        Constructeur de la classe Employe

        :param nom:
        :type nom: string
        :param prenom:
        :type prenom: string
        :param agence:
        :type agence: Agence
        """

        self._nom = nom
        self._prenom = prenom
        self._agence = agence

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


class Vendeur(Employe):
    """
    Premier type d'Employe, le vendeur, qui peut faire les trajets, créer une fiche client, louer les voitures et calculer le coût d'une location.
    """

    def __str__(self):
        return "{} {}, vendeur de l'agence {}".format(self._nom, self._prenom, self._agence.nom)


    def louer_voiture(self, client, voiture, trajet):
        """
        Fonction qui initie l'ensemble du processus de location

        :param client:
        :type client: Client
        :param voiture:
        :type voiture: Voiture
        :param trajet:
        :type trajet: Trajet
        """
        pass

    def recuperer_voiture(self, client, voiture):
        """
        Fonction qui crée un nouvel objet trajet, et l'ajoute dans la BDD.

        :param client:
        :type client: Client
        :param voiture:
        :type voiture: Voiture
        """
        pass

    def creer_fiche_client(self, nom_client, prenom_client, date_naiss_client):
        """
        Fonction qui crée une nouvelle fiche client (objet client de la base de donnée)

        :param nom_client:
        :type nom_client: string
        :param prenom_client:
        :type prenom_client: string
        :param date_naiss_client:
        :type date_naiss_client: date
        """
        pass

    def calculer_cout(self, trajet):
        """
        Fonction qui calcule le coût de location pour un certain trajet

        :param trajet:
        :type trajet: Trajet
        """
        pass


class Responsable(Vendeur):
    """
    Second type d'Employé, le responsable d'agence, qui peut déterminer si une voiture doit être immobilisée pour entretien
    """

    def __str__(self):
        return "{} {}, responsable de l'agence {}".format(self._nom, self._prenom, self._agence.nom)

    def entretenir_voiture(self,voiture):
        """
        Méthode qui lance la mise à l'entretien d'une voiture

        :param voiture:
        :type voiture: Voiture
        """
        pass


class Employe_siege(Employe):
    """
    Troisième et dernier type d'employé, celui du siège, qui peut décider de transferts de voitures entre Agence
    """

    def transferer_voiture(self, agence_depart, agence_arrivee, liste_voiture):
        """
        Fonction qui permet de transférer certaines voitures d'une agence à une autre

        :param agence_depart:
        :type agence_depart: Agence
        :param agence_arrivee:
        :type agence_arrivee: Agence
        :param liste_voiture:
        :type liste_voiture: liste de Voiture
        """
        pass

    def calculer_stats(self,agence):
        """
        Fonction qui retourne les statistiques propres à une agence.

        :param agence:
        :type agence: Agence
        :return:
        """
        pass
