from django.shortcuts import render
from .forms import HistoriaClinicaForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from .logic.logic_historiaClinica import create_historiaClinica, get_historiaClinicas

def historiaClinica_list(request):
    historiaClinicas = get_historiaClinicas()
    context = {
        'historiaClinica_list': historiaClinicas
    }
    return render(request, 'HistoriaClinica/historiaClinicas.html', context)

def historiaClinica_create(request):
    if request.method == 'POST':
        form = HistoriaClinicaForm(request.POST)
        if form.is_valid():
            create_historiaClinica(form)
            messages.add_message(request, messages.SUCCESS, 'historiaClinica create successful')
            return HttpResponseRedirect(reverse('historiaClinicaCreate'))
        else:
            print(form.errors)
    else:
        form = HistoriaClinicaForm()

    context = {
        'form': form,
    }

    return render(request, 'HistoriaClinica/historiaClinicaCreate.html', context)
