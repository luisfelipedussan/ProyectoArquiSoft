from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    path('Paciente/', csrf_exempt(views.Paciente_list)),
    path('pacientecreate/', csrf_exempt(views.Paciente_create), name='PacienteCreate'),
]