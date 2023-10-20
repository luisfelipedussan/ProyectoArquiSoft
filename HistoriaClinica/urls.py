from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    path('HistoriaClinica/', csrf_exempt(views.historiaClinica_list)),
    path('historiaClinicacreate/', csrf_exempt(views.historiaClinica_create), name='historiaClinicaCreate'),
]