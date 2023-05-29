from django import forms
from gestion.models import Student



class FormStudent(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['nom_student','prenom_student','date_naissance','adress_rue','code_postal','ville','sexe','classe']
