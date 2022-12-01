# -*- coding: utf-8 -*-
"""
Fichier composé des classes : Document, RedditDocument et ArxivDocument
"""

#Création de la classe Document
class Document:
    def __init__(self, titre="", auteur="", date="", url="", texte=""):
        self.titre=titre
        self.auteur=auteur
        self.date=date
        self.url=url
        self.texte=texte
    
    # Fonction qui renvoie le texte à afficher lorsqu'on tape repr(classe)
    def __repr__(self):
        return f"Titre : {self.titre}\tAuteur : {self.auteur}\tDate : {self.date}\tURL : {self.url}\tTexte : {self.texte}\t"
    
    # Fonction qui renvoie le texte à afficher lorsqu'on tape str(classe)
    def __str__(self):
        return f"{self.titre}, par {self.auteur}"

#Création de la classe fille RedditDocument
class RedditDocument(Document):
    def __init__(self, titre="", auteur="", date="", url="", texte="", nbCom=""):
        super().__init__(titre="", auteur="", date="", url="", texte="")
        self.nbCome=nbCom
    def __str__(self):
        parent = super().__str__()
        return f"{parent}, {self.nbCom}"
    
#Création de la classe fille ArxivDocument
class ArxivDocument(Document):
    def __init__(self, titre="", auteur="", date="", url="", texte="", coAuteur=""):
        super().__init__(titre="", auteur="", date="", url="", texte="")
        self.coAuteur=coAuteur
    def __str__(self):
        parent = super().__str__()
        return f"{parent}, {self.coAuteur}"
