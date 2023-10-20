from ..models import HistoriaClinica

def get_historiaClinicas():
    queryset = HistoriaClinica.objects.all().order_by('-dateTime')[:10]
    return (queryset)

def create_historiaClinica(form):
    historiaClinica = form.save()
    historiaClinica.save()
    return ()