from HistoriaClinica.models import HistoriaClinica
from ..models import Alarm

def get_alarms():
    queryset = Alarm.objects.all()
    return (queryset)

def get_HistoriaClinicas_by_Paciente(Paciente):
    queryset = HistoriaClinica.objects.filter(Paciente=Paciente)
    return (queryset)

def create_alarm(Paciente, HistoriaClinica, limitExceeded):
    alarm = Alarm()
    alarm.Paciente = Paciente
    alarm.HistoriaClinica = HistoriaClinica
    alarm.value = HistoriaClinica.value
    alarm.limitExceeded = limitExceeded
    alarm.save()
    return alarm