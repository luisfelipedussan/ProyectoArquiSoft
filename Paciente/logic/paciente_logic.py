from ..models import Paciente

def get_variables():
    queryset = Paciente.objects.all()
    return (queryset)

def create_variable(form):
    paciente= form.save()
    paciente.save()
    return ()