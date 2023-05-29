from django.contrib import admin
from .models import Student, Sexe, Niveau, Classe, NumeroClasse
# Register your models here.


admin.site.register(Student)
admin.site.register(Sexe)
admin.site.register(Niveau)
admin.site.register(Classe)
admin.site.register(NumeroClasse)
