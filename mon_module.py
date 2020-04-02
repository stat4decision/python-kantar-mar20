# -*- coding: utf-8 -*-
"""
Ceci est un module pour traiter des donnénes avec python issu de la formation python
"""

def recup_fichiers(rep, extension):
    # 1. on récupère la liste des fichiers
    import os
    liste_fichiers=os.listdir(rep)
    # 2. on sélectionne uniquement les fichiers avec l'extension (on peut faire une boucle et une condition)
    liste_fichiers = [fichier for fichier in liste_fichiers if extension in fichier]
    return liste_fichiers

def ma_moyenne(liste1, liste2):
    moyenne = sum(liste1+liste2)/len(liste1+liste2)
    return moyenne