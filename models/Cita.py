from odoo import models, fields, api

class Cita(models.Model):
    _name = 'veterinariaupo.cita'
    _description = 'Modelo Cita'

    id_cita = fields.Integer('Id Cita', required=True, help="Identificador de cita")  # Primary key
    fecha = fields.Datetime('Fecha', required=True, autodate=True)
    duracion = fields.Integer("Duracion (minutos)", required=True)
    descripcion = fields.Text('Descripcion')

    microChip = fields.Many2one('veterinariaupo.mascota', string='Mascota')
    veterinario_id = fields.Many2one('veterinariaupo.veterinario', string='Veterinario')
    tratamientos_ids = fields.One2many('veterinariaupo.tratamiento', 'cita_id', string='Tratamientos')
    pruebas_medicas_ids = fields.One2many('veterinariaupo.pruebamedica', 'cita_id', string='Pruebas Médicas')

    @api.constrains('fecha', 'duracion', 'tratamientos_ids')
    def check_fecha_duracion(self):
        # Asegurarse de que la duración sea un valor positivo
        if self.duracion <= 0:
            raise models.ValidationError('La duración debe ser un valor positivo.')

        # Asegurarse de que la fecha no esté en el pasado
        if self.fecha < fields.Datetime.now():
            raise models.ValidationError('La fecha de la cita no puede estar en el pasado.')

        # Asegurarse de que hay al menos un tratamiento asociado a la cita
        if not self.tratamientos_ids:
            raise models.ValidationError('Debe haber al menos un tratamiento asociado a la cita.')

        # Calcular la duración total de los tratamientos en minutos
        duracion_total_tratamientos = sum(
            (tratamiento.fin_tratamiento - tratamiento.inicio_tratamiento).days * 24 * 60
            for tratamiento in self.tratamientos_ids
        )

        # Asegurarse de que la duración total de los tratamientos no exceda la duración de la cita
        if duracion_total_tratamientos > self.duracion:
            raise models.ValidationError('La duración total de los tratamientos no puede exceder la duración de la cita.')



