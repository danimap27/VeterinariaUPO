from odoo import models, fields, api

class PruebaMedica(models.Model):
    _name = 'veterinariaupo.pruebamedica'
    _description = 'Modelo PruebaMedica'

    id_pruebamedica = fields.Integer('Número de Prueba Médica', required=True, help="Identificador de prueba medica")  # Primary key
    tipo = fields.Char(string='Tipo de Prueba Médica', size=256, required=True)
    fecha = fields.Datetime('Fecha', required=True, autodate=True)
    descripcion = fields.Text('Descripción')

    ats_id = fields.Many2one('veterinariaupo.ats', string='ATS')
    cita_id = fields.Many2one('veterinariaupo.cita', string='Cita')

    @api.constrains('fecha')
    def check_fecha(self):
        # Validar que la fecha de la prueba médica no esté en el pasado
        if self.fecha < fields.Datetime.now():
            raise models.ValidationError('La fecha de la prueba médica no puede estar en el pasado.')

    @api.constrains('tipo')
    def check_tipo(self):
        # Validar que el tipo de prueba médica no contenga caracteres especiales
        if not self.tipo.isalnum():
            raise models.ValidationError('El tipo de prueba médica no puede contener caracteres especiales.')

    @api.constrains('descripcion')
    def check_descripcion(self):
        # Validar que la descripción no sea demasiado corta
        if len(self.descripcion) < 5:
            raise models.ValidationError('La descripción de la prueba médica debe tener al menos 5 caracteres.')
