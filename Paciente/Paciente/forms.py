from django import forms
from .models import Paciente

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = [
            'name',
'tipoDocumentoPaciente',
'numeroPaciente',
'fechaExpedicionDocumentoPaciente',
'lugarExpedicionDocumentoPaciente',
'fechaNacimientoPaciente',
'lugarNacimientoPaciente',
'edadPaciente',
'tipoEdadPaciente',
'primerNombrePaciente',
'segundoNombrePaciente',
'primerApellidoPaciente',
'segundoApellidoPaciente',
'seudonimoPaciente',
'estadoCivilPaciente',
'sexoPaciente',
'grupoSanguineoPaciente',
'celularPaciente',
'whatsappPaciente',
'celularAdicionalPaciente',
'telefonoFijoPaciente',
'correoElectronicoPaciente',
'lugarResidenciaPaciente',
'localidadPaciente',
'areaUbicacionPaciente',
'paisPaciente',
'departamentoPaciente',
'ciudadPaciente',
'nivelEducativoPaciente',
'ocupacionPaciente',
'tipoVinculacionPaciente',
'codigoPertenenciaEtinicaPaciente',
'poblacionClavePaciente',
'tipoAtencionPaciente',
'epsPaciente',
'tipoAfilicacionPaciente',
'ipsPrimariaPaciente',
'contratoObjetoPaciente',
'estadoPaciente'

        ]
        labels = {
            'name': 'Name',
'tipoDocumentoPaciente': 'TipoDocumentoPaciente',
'numeroPaciente': 'NumeroPaciente',
'fechaExpedicionDocumentoPaciente': 'FechaExpedicionDocumentoPaciente',
'lugarExpedicionDocumentoPaciente': 'LugarExpedicionDocumentoPaciente',
'fechaNacimientoPaciente': 'FechaNacimientoPaciente',
'lugarNacimientoPaciente': 'LugarNacimientoPaciente',
'edadPaciente': 'EdadPaciente',
'tipoEdadPaciente': 'TipoEdadPaciente',
'primerNombrePaciente': 'PrimerNombrePaciente',
'segundoNombrePaciente': 'SegundoNombrePaciente',
'primerApellidoPaciente': 'PrimerApellidoPaciente',
'segundoApellidoPaciente': 'SegundoApellidoPaciente',
'seudonimoPaciente': 'SeudonimoPaciente',
'estadoCivilPaciente': 'EstadoCivilPaciente',
'sexoPaciente': 'SexoPaciente',
'grupoSanguineoPaciente': 'GrupoSanguineoPaciente',
'celularPaciente': 'CelularPaciente',
'whatsappPaciente': 'WhatsappPaciente',
'celularAdicionalPaciente': 'CelularAdicionalPaciente',
'telefonoFijoPaciente': 'TelefonoFijoPaciente',
'correoElectronicoPaciente': 'CorreoElectronicoPaciente',
'lugarResidenciaPaciente': 'LugarResidenciaPaciente',
'localidadPaciente': 'LocalidadPaciente',
'areaUbicacionPaciente': 'AreaUbicacionPaciente',
'paisPaciente': 'PaisPaciente',
'departamentoPaciente': 'DepartamentoPaciente',
'ciudadPaciente': 'CiudadPaciente',
'nivelEducativoPaciente': 'NivelEducativoPaciente',
'ocupacionPaciente': 'OcupacionPaciente',
'tipoVinculacionPaciente': 'TipoVinculacionPaciente',
'codigoPertenenciaEtinicaPaciente': 'CodigoPertenenciaEtinicaPaciente',
'poblacionClavePaciente': 'PoblacionClavePaciente',
'tipoAtencionPaciente': 'TipoAtencionPaciente',
'epsPaciente': 'EpsPaciente',
'tipoAfilicacionPaciente': 'TipoAfilicacionPaciente',
'ipsPrimariaPaciente': 'IpsPrimariaPaciente',
'contratoObjetoPaciente': 'ContratoObjetoPaciente',
'estadoPaciente': 'EstadoPaciente'

        }