from django import forms
from .models import HistoriaClinica

class HistoriaClinicaForm(forms.ModelForm):
    class Meta:
        model = HistoriaClinica
        fields = [
            'paciente',
            'documentoProfesionalConsulta',
            'nombreProfesionalConsulta',
            'fechaHoraAtencionConsulta',
            'servicioConsulta',
            'motivoConsulta',
            'enfermedadPaciente',
            'diagnosticoPaciente',
            'antecedentesPersonalesPaciente',
            'antecedentesFamiliaresPaciente',
            'antecedentesFarmacologicosPaciente',
            'alergiasPaciente',
            'vacunasPaciente',
            'examenFisicoPaciente',
            'signosVitalesPaciente',
            'ordenesMedicasPaciente',
            'incapacidadMedicaPaciente',
            'notaSeguimientoPaciente',
            'motivoAtencionFallidaPaciente',
            'condicionEgresoPaciente'

        ]

        labels = {
           'paciente': 'Paciente',
    'documentoProfesionalConsulta': 'DocumentoProfesionalConsulta',
    'nombreProfesionalConsulta': 'NombreProfesionalConsulta',
    'fechaHoraAtencionConsulta': 'FechaHoraAtencionConsulta',
    'servicioConsulta': 'ServicioConsulta',
    'motivoConsulta': 'MotivoConsulta',
    'enfermedadPaciente': 'EnfermedadPaciente',
    'diagnosticoPaciente': 'DiagnosticoPaciente',
    'antecedentesPersonalesPaciente': 'AntecedentesPersonalesPaciente',
    'antecedentesFamiliaresPaciente': 'AntecedentesFamiliaresPaciente',
    'antecedentesFarmacologicosPaciente': 'AntecedentesFarmacologicosPaciente',
    'alergiasPaciente': 'AlergiasPaciente',
    'vacunasPaciente': 'VacunasPaciente', 
    'examenFisicoPaciente': 'ExamenFisicoPaciente',
    'signosVitalesPaciente': 'SignosVitalesPaciente',
    'ordenesMedicasPaciente': 'OrdenesMedicasPaciente',
    'incapacidadMedicaPaciente': 'IncapacidadMedicaPaciente',
    'notaSeguimientoPaciente': 'NotaSeguimientoPaciente',
    'motivoAtencionFallidaPaciente': 'MotivoAtencionFallidaPaciente',
    'condicionEgresoPaciente': 'CondicionEgresoPaciente'
        }