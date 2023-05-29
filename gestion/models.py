from pyexpat import model
from django.db import models

# Create your models here.

class Student(models.Model):
    """ Model représentant les étudiants """
    nom_student = models.CharField(max_length=100)
    prenom_student = models.CharField(max_length=100)
    date_naissance = models.DateField()
    adress_rue = models.CharField(max_length=100)
    code_postal = models.CharField(max_length=100)
    ville = models.CharField(max_length=100)
    sexe = models.ForeignKey('Sexe', on_delete=models.SET_NULL, null=True)
    classe = models.ForeignKey('Classe',on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return f'{self.nom_student} {self.prenom_student}'

class Sexe(models.Model):
    """ Model représentant le sexe de l'étudiants """
    nom_sexe = models.CharField(max_length=10)

    def __str__(self):
        return self.nom_sexe


class Niveau(models.Model):
    """ Model représentant le niveau de l'étudiant """
    nom_niveau = models.CharField(max_length=100)

    def __str__(self):
        return self.nom_niveau


class Classe(models.Model):
    """ Model représentant la classe de l'étudiant """
    niveau = models.ForeignKey('Niveau',on_delete=models.SET_NULL,null=True)
    numero = models.ForeignKey('NumeroClasse', on_delete=models.SET_NULL,null=True)
    

    def __str__(self):
        return f'{self.niveau} {self.numero}'


class NumeroClasse(models.Model):
    """ Model représentant le numéro d'une classe"""
    numero = models.CharField(max_length=10)

    def __str__(self):
        return self.numero