from django.shortcuts import render
from .forms import PacienteForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from .logic.paciente_logic import create_paciente, get_pacientes
from django.views.decorators.csrf import ensure_csrf_cookie

def Paciente_list(request):
    pacientes = get_pacientes()
    context = {
        'paciente_list': pacientes
    }
    return render(request, 'Paciente/pacientes.html', context)

@ensure_csrf_cookie
def Paciente_create(request):

    if request.method == 'POST':
        form = PacienteForm(request.POST)
        if form.is_valid():
            create_paciente(form)
            messages.add_message(request, messages.SUCCESS, 'Paciente create successful')
            return HttpResponseRedirect(reverse('pacienteCreate'))
        else:
            print(form.errors)
    else:
        form = PacienteForm()

    context = {
        'form': form,
    }

    return render(request, 'Paciente/pacienteCreate.html', context)