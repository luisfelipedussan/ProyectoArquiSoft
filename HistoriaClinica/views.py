from django.shortcuts import render
from .forms import HistoriaClinicaForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from .logic.logic_historiaClinica import create_historiaClinica, get_historiaClinicas
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import ensure_csrf_cookie
from datetime import datetime
import logging
import os

current_directory = os.path.dirname(os.path.realpath(__file__))
print(current_directory)
logging.basicConfig(filename='app.log', level=logging.INFO)


def historiaClinica_list(request):
    historiaClinicas = get_historiaClinicas()
    context = {
        'historiaClinica_list': historiaClinicas
    }
    return render(request, 'HistoriaClinica/historiaClinicas.html', context)

@csrf_exempt
@ensure_csrf_cookie
def historiaClinica_create(request):
    if request.method == 'POST':
        form = HistoriaClinicaForm(request.POST)
        if form.is_valid():
            create_historiaClinica(form)
            messages.add_message(request, messages.SUCCESS, 'historiaClinica create successful')
            usuario = request.user if request.user.is_authenticated else None

            # Obtener la fecha y hora actual
            fecha_hora_actual = datetime.now()

            # Registrar la información en el archivo de log en una hora
            logging.info(f'Usuario: {usuario}, en Hora: {fecha_hora_actual}, creo/modificó una HistoriaClinica')
        
            return HttpResponseRedirect(reverse('historiaClinicaCreate'))
        else:
            print(form.errors)
    else:
        form = HistoriaClinicaForm()

    context = {
        'form': form,
    }

    return render(request, 'historiaClinicaCreate.html', context)


