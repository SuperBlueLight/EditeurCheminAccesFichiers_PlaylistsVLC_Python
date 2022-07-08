
# .................................................................
# NOTES : 
# 

# .................................................................
# Imports librairie standard

# Imports tiers

# Imports locaux
import gestionnaire_fichier as gf

# .................................................................
# Constantes
REPERTOIRE_COURANT = "C:\\Users\\Flo\\Documents\\400_Musiques\\_Playlists_vlc"
ELEMENT_A_REMPLACER_PAR_DEFAUT = "D:/400-Musiques"
ELEMENT_A_AJOUTER_PAR_DEFAUT = "C:/Users/Flo/Documents/400_Musiques" 

# .................................................................
# Classes
class Programme():
    """TODO"""

    # .................................................................
    # Constructeur & méthodes spéciales

    def __init__(self):
        self.gestionnaire_fichier = gf.GestionnaireFichier()

    # .................................................................
    # Méthodes

    def main(self):
        print("Récupération de la liste des fichiers...")
        liste_fichiers = self.gestionnaire_fichier.lister_fichiers(REPERTOIRE_COURANT, ".xspf", True)
        print(f"Nombre de fichiers: {len(liste_fichiers)}")

        for i in range(0, len(liste_fichiers), 1):
            print(f"\nFichier: {liste_fichiers[i]}")
            print("Obtention de toutes les lignes...")
            liste_lignes = self.gestionnaire_fichier.obtenir_contenu_fichier_complet(f"{REPERTOIRE_COURANT}\\{liste_fichiers[i]}")
            liste_lignes_triee = [ligne for ligne in liste_lignes if "<location>" in ligne]
            print("Affichage d'une ligne type à modifier:")
            ligne_test = liste_lignes_triee[0]
            print(ligne_test)

            print("\nModifier? (y/n)")
            yes_no = input()
            if yes_no == "y":
                print("\nQuel élément à remplacer?")
                element_a_remplacer = input()
                if (element_a_remplacer == "" or element_a_remplacer == "\n"):
                    element_a_remplacer = ELEMENT_A_REMPLACER_PAR_DEFAUT
                print("\nQuel élément à ajouter?")
                element_a_ajouter = input()
                if (element_a_ajouter == "" or element_a_ajouter == "\n"):
                    element_a_ajouter = ELEMENT_A_AJOUTER_PAR_DEFAUT

                print("\nRésultat:")
                print(ligne_test.replace(element_a_remplacer, element_a_ajouter))

                print("\nValider:")
                yes_no = input()
                if yes_no == "y":
                    print("\nRemplacement des lignes...")
                    for j in range(0, len(liste_lignes), 1): 
                        ligne = liste_lignes[j]
                        if element_a_remplacer in ligne:
                            ligne = ligne.replace(element_a_remplacer, element_a_ajouter)
                            liste_lignes[j] = ligne
                    print("Terminé.")

                    print("Ecriture du fichier...")
                    self.gestionnaire_fichier.ecrire_dans_fichier(f"{REPERTOIRE_COURANT}\\{liste_fichiers[i]}", liste_lignes, "w")
                    print("Terminé.")

# .....................................................................
# Lancement programme 

def main():
    programme = Programme()
    programme.main()

main()