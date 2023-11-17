from django.shortcuts import render
from .forms import HistoriaClinicaForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from .logic.logic_historiaClinica import create_historiaClinica, get_historiaClinicas
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import ensure_csrf_cookie
import logging
import os

current_directory = os.path.dirname(os.path.realpath(__file__))
log_file_path = os.path.join(current_directory, 'app.log')
logging.basicConfig(filename=log_file_path, level=logging.INFO)


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
            logging.info(f'La historiaClinica fue modificada: {request.url}')
  