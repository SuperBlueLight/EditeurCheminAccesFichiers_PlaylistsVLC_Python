# .................................................................
# NOTES : 
# 


# .................................................................
# Imports librairie standard
import os
import io

# Imports tiers

# Imports locaux

# .................................................................
# Constantes


# .................................................................
# Classes
class GestionnaireFichier():
    """Classe permettant d'intéragir simplement avec des fichiers."""

    # .................................................................
    # Constructeur & méthodes spéciales

    def __init__(self):
        pass

    # .................................................................
    # Propriétés

    # .................................................................
    # Méthodes

    def fichier_existe(self, chemin_fichier: str):
        """Permet de savoir si un fichier existe ou non sur le disque dur.

        Args:
            chemin_fichier (str): chemin d'accès complet du fichier.

        Returns:
            bool: True si le fichier existe, False sinon.
        """
        return os.path.exists(chemin_fichier)

    def obtenir_contenu_fichier_complet(self, chemin_fichier: str, obtenir_tableau=True):
        """Permet de récupérer l'intégralité du contenu d'un fichier. Aucune ligne n'est filtrée.

        Args:
            chemin_fichier (str): chemin d'accès complet du fichier.
            obtenir_tableau (bool, optional): permet de récupérer les résultats sous forme d'un tableau (True) ou non (False).

        Returns:
            si obtenir_tableau vaut True:
                str: contenu du fichier sous forme de texte.
            sinon:
                list: liste contenant chaque ligne du fichier sous forme de texte.
        """
        contenu_fichier = None
        if self.fichier_existe(chemin_fichier):
            fichier = open(chemin_fichier, "r", encoding="utf-8")
            contenu_fichier = fichier.read()
            fichier.close()

            if obtenir_tableau:
                contenu_fichier = contenu_fichier.split("\n")
        return contenu_fichier

    def ecrire_dans_fichier(self, chemin_fichier: str, contenu: list, mode_ecriture="a", tester_existence_fichier=False):
        """Ajoute une liste de textes dans un fichier.

        Args:
            chemin_fichier (str): chemin d'accès complet du fichier.
            contenu (list): liste des lignes au format texte à ajouter.
            mode_ecriture (str, optional): précise le mode d'écriture à utiliser. 
                'a': ajouter en fin de fichier ; 'w': écrire avec reset du fichier.
            tester_existence_fichier (bool, optional): indique s'il faut (True) ou non (False) tester l'existence du fichier avant d'ajouter le contenu.
        """
        ecriture_possible = True
        if tester_existence_fichier:
            ecriture_possible = self.fichier_existe(chemin_fichier)
            
        if ecriture_possible:
            fichier = open(chemin_fichier, mode_ecriture, encoding="utf-8")
            for donnees in contenu:
                fichier.write(f"{str(donnees)}\n")
            fichier.close()

    def lister_fichiers(self, repertoire: str, filtre = "*", obtenir_tableau=False):
        """Renvoie une chaîne de caractères contenant une liste 
        des fichiers contenus dans un répertoire donné. 

        Arguments:
            repertoire (str): Emplacement des fichiers dans lequel faire la liste.
            filtre (str): Permet, comme son nom l'indique, de filtrer les fichiers 
                selon une chaîne de caractères.
                Exemple: '.mp3' permet de ne récupérer que les fichiers ayant cette extension.
            obtenir_tableau (bool): Précise si la liste doit être renvoyées sous format texte (False)
                ou sous forme de tableau (True)"""
        contenu_final = None
        liste_fichiers = os.listdir(repertoire)

        if filtre != "*":
            liste_fichiers = [fichier for fichier in liste_fichiers if filtre in fichier]

        if obtenir_tableau:
            contenu_final = liste_fichiers
        else:
            constructeur_chaine = io.StringIO()
            for fichier in liste_fichiers:
                constructeur_chaine.write("{0}\n".format(fichier))
            contenu_final = constructeur_chaine.getvalue()
        return contenu_final
    




