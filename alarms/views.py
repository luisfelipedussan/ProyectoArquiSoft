from django.http import JsonResponse
from django.shortcuts import render

from Paciente.logic.paciente_logic import get_pacientes
from HistoriaClinica.logic.logic_historiaClinica import get_historiaClinicas

def alarm_list(request):
    alarms = get_alarms()
    context = list(alarms.values())
    return JsonResponse(context, safe=False)

def generate_alarm(request, variable_id):
    historiasClinicas = get_historiaClinicas()
    createAlarm = False
    upperHistoriaClinica = None
    for HistoriaClinica in historiasClinicas:
        if HistoriaClinica.paciente.DoesNotExist:
            createAlarm = True
            upperHistoriaClinica = HistoriaClinica
    if createAlarm:
        alarm = create_alarm(variable, upperHistoriaClinica, 30)
        return JsonResponse(alarm.toJson(), safe=False)
    else:
        return JsonResponse({'message': 'No alarm created'}, status=200)