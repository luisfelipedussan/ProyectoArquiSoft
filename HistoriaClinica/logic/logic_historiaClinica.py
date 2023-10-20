from ..models import HistoriaClinica

def get_historiaClinicas():
    queryset = HistoriaClinica.objects.all()
    return (queryset)

def create_historiaClinica(form):
    historiaClinica = form.save()
    historiaClinica.save()
    return ()