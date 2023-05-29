from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard/',views.dashboard, name='dashboard'),
    path('create-student/',views.CreateStudent, name='create-student'),
    path('liste-student/',views.ListeStudent, name='liste-student'),
    path('detail-classe/<int:pk>', views.DetailClasse, name='detail-classe'),
    path('detail-student/<int:pk>', views.DetailStudent, name='detail-student'),
    path('update-student/<int:pk>', views.UpdateStudent, name='update-student'),
]