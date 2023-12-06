from django.shortcuts import render
from ..forms import PacienteForm
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from ..logic.paciente_logic import create_paciente, get_pacientes
from django.views.decorators.csrf import ensure_csrf_cookie
from django.contrib.auth.decorators import login_required
from ProyectoArquiSoft.auth0backend import getRole

@login_required
def Paciente_list(request):

    role = getRole(request)
    if role == "Medico":
        pacientes = get_pacientes()
        context = {
            'paciente_list': pacientes
        }
        return render(request, 'Paciente/pacientes.html', context)
    else:
        return HttpResponse("Unauthorized User")

@login_required
@ensure_csrf_cookie
def Paciente_create(request):

    role = getRole(request)
    if role == "Medico":
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

    else:
        return HttpResponse("Unauthorized User")