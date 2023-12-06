from django.db import models
from Paciente.models import Paciente

class HistoriaClinica(models.Model):
    
    paciente = models.OneToOneField(Paciente,on_delete=models.CASCADE,primary_key=True)
    documentoProfesionalConsulta = models.PositiveIntegerField()
    nombreProfesionalConsulta = models.CharField(max_length=100)
    fechaHoraAtencionConsulta = models.DateTimeField()
    servicioConsulta = models.CharField(max_length=100)
    motivoConsulta = models.TextField()
    enfermedadPaciente = models.TextField()
    diagnosticoPaciente = models.TextField()
    antecedentesPersonalesPaciente = models.TextField()
    antecedentesFamiliaresPaciente = models.TextField()
    antecedentesFarmacologicosPaciente = models.TextField()
    alergiasPaciente = models.TextField()
    vacunasPaciente = models.TextField()
    examenFisicoPaciente = models.TextField()
    signosVitalesPaciente = models.TextField()
    ordenesMedicasPaciente = models.TextField()
    incapacidadMedicaPaciente = models.TextField()
    notaSeguimientoPaciente = models.TextField()
    motivoAtencionFallidaPaciente = models.TextField()
    condicionEgresoPaciente = models.CharField(max_length=100)
  

    
    def __str__(self):
        return '{}'.format(self.paciente.name)
