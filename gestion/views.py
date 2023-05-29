from msilib.schema import Class
from multiprocessing import context
from pydoc import classname
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from gestion.models import Classe, Niveau, Student, Sexe
from gestion.forms import FormStudent

from django.http import Http404


# Create your views here.


def index(request):
    return render(request, 'index.html',context={})


@login_required
def dashboard(request):
    niveau = Niveau.objects.filter()

    nb_classe = Classe.objects.filter().count()

    classe_nombre_term = Classe.objects.filter(niveau="1").count()
    classe_term = Classe.objects.filter(niveau="1")
    
    list_classe_term = []
    for i in range(classe_nombre_term):
        var = {}
        var['nom'] = classe_term[i]
        var['nombre'] = Student.objects.filter(classe=classe_term[i]).count()
        list_classe_term.append(var)

    classe_nombre_prem = Classe.objects.filter(niveau="2").count()
    classe_prem = Classe.objects.filter(niveau="2")
    list_classe_prem = []
    for i in range(classe_nombre_prem):
        var = {}
        var['nom'] = classe_prem[i]
        var['nombre'] = Student.objects.filter(classe=classe_prem[i]).count()
        list_classe_prem.append(var)

    classe_nombre_sec = Classe.objects.filter(niveau="3").count()
    classe_sec = Classe.objects.filter(niveau="3")
    list_classe_sec = []
    for i in range(classe_nombre_sec):
        var = {}
        var['nom'] = classe_sec[i]
        var['nombre'] = Student.objects.filter(classe=classe_sec[i]).count()
        list_classe_sec.append(var)


    nb_etudiant = Student.objects.filter().count()

    student = Student.objects.filter()

    classe = Classe.objects.filter()

    

    context = {
        'niveau' : niveau,
        'classe_term' : list_classe_term,
        'classe_prem' : list_classe_prem,
        'classe_sec' : list_classe_sec,
        'nb_classe' : nb_classe,
        'nb_etudiant' : nb_etudiant,
        'student' : student,
        'classe' : classe,
    }
    return render(request,'login/dashboard.html',context=context)

def CreateStudent (request):
    classe = Classe.objects.filter()

    form = FormStudent()

    if request.method == 'POST':
        form = FormStudent(request.POST)
        if form.is_valid():
            student = form.save(commit=False)
            sexe = Sexe.objects.get(id=request.POST.get("sexe"))
            classe_student = Classe.objects.get(id=request.POST.get("classe"))
            student.sexe = sexe
            student.classe = classe_student
            student.save()
            student = Student.objects.all().count()
            redirect('detail-student',pk=student)


    return render(request, 'login/createstudent.html', context={
        'classe' : classe,
        'form' : form
    })



def ListeStudent(request):
    classe = Classe.objects.filter()

    student = Student.objects.filter()


    return render(request, 'login/listestudent.html', context={
        'classe' : classe,
        'student' : student
    })



def DetailClasse(request,pk):
    student = Student.objects.filter(classe=pk).order_by('nom_student')
    classe_student = Classe.objects.get(id=pk)
    classe = Classe.objects.filter()

    return render(request, 'login/detailclasse.html',context={
        'student' : student,
        'classe' : classe,
        'classe_student' : classe_student,
    })

def DetailStudent(request,pk):
    student = Student.objects.get(id=pk)

    classe = Classe.objects.filter()

    return render(request, 'login/detailstudent.html', context={
        'student' : student,
        'classe' : classe
    })

def UpdateStudent(request,pk):
    classe = Classe.objects.filter()
    try:
        student = Student.objects.get(id=pk)
        
        if request.method == 'POST':
            form = FormStudent(request.POST,request.FILES, instance=student)
            if form.is_valid():
                print(request.FILES)
                student = form.save(commit=False)
                sexe = Sexe.objects.get(pk=request.POST.get('sexe'))
                classe = Classe.objects.get(pk=request.POST.get('classe'))
                student.sexe = sexe
                student.classe = classe
                student.save()
                return redirect('detail-student', pk=pk)
        else:
            form = FormStudent(instance=student)

    except Student.DoesNotExist:
        raise Http404("L'élève n'existe pas")
    
    return render(request, 'login/updatestudent.html', context={
        'classe' : classe,
        'form':form,
        'student':student,
    })