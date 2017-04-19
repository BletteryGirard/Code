from agence import Agence
from voiture import Voiture
from client import Client


class Employe(object):
    def __init__(self, nom, prenom, agence):
        """
        Constructeur de la classe Employe

        :param nom: nom de l'employe
        :type nom: string
        :param prenom: prenom de l'employe
        :type prenom: string
        :param agence: nom de l'agence
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

        :param client: client qui effectue une location
        :type client: Client
        :param voiture: voiture louée par un client
        :type voiture: Voiture
        :param trajet: trajet choisi par un client d'une agence à une autre
        :type trajet: Trajet
        """
        pass

    def recuperer_voiture(self, client, voiture):
        """
        Fonction qui crée un nouvel objet trajet, et l'ajoute dans la BDD.

        :param client: client qui effectue une location
        :type client: Client
        :param voiture: voiture louée par le client
        :type voiture: Voiture
        """
        pass

    def creer_fiche_client(self, nom_client, prenom_client, date_naiss_client):
        """
        Fonction qui crée une nouvelle fiche client (objet client de la base de donnée)

        :param nom_client: nom du nouveau client
        :type nom_client: string
        :param prenom_client: prenom du nouveau client
        :type prenom_client: string
        :param date_naiss_client: date de naissance du client au format date
        :type date_naiss_client: date
        """
        pass

    def calculer_cout(self, trajet):
        """
        Fonction qui calcule le coût de location pour un certain trajet

        :param trajet: trajet d'un client partant d'une agence et arrivant à cette même agence ou une autre
        :type trajet: Trajet
        """
        pass


    def creer_trajet(self, date_debut, date_fin, lieu_debut, lieu_arrivee, distance):
        """
        Fonction qui crée le trajet effectué par le client.

        :param date_debut: date de debut du trajet choisi par le client
        :type date_debut: date
        :param date_fin: date de fin du trajet choisi par le client
        :type date_fin: date
        :param lieu_debut: lieu de depart choisi par le client correspondant a une agence
        :type lieu_debut: Agence
        :param lieu_arrivee: lieu d'arrivee choisi par le client correspondant a une agence
        :type lieu_arrivee: Agence
        :param distance: distance parcourue par le client lors de la location
        :type distance: integer
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

        :param voiture: voiture choisi par le responsable necessitant un entretien
        :type voiture: Voiture
        """
        pass



    #def recruter_vendeur(self):



class Employe_siege(Employe):
    """
    Troisième et dernier type d'employé, celui du siège, qui peut décider de transferts de voitures entre Agence ou bien
    calculer les statistiques propre à une agence.
    """

    def transferer_voiture(self, agence_depart, agence_arrivee):
        """
        Fonction qui permet de transférer certaines voitures d'une agence à une autre

        :param agence_depart: agence de depart de la location
        :type agence_depart: Agence
        :param agence_arrivee: agence d'arrivee de la location
        :type agence_arrivee: Agence
        """
        pass

    def calculer_stats(self,agence):
        """
        Fonction qui retourne les statistiques propres à une agence.

        :param agence: correspond à l'agence dont on veut les statistiques
        :type agence: Agence
        :return:
        """
        pass
