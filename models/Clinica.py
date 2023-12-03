from odoo import models, fields, api

class Clinica(models.Model):
    _name = 'veterinariaupo.clinica'
    _description = 'Modelo de la Clinica'

    nombre = fields.Char(string='Nombre de la Clinica', size=256, required=True)
    direccion = fields.Char(string='Dirección de la Clinica', required=True, help="La dirección de la clínica, se utiliza como clave primaria")  # La primary key
    telefono = fields.Integer(string="Teléfono de la Clinica", required=True)

    veterinarios_ids = fields.One2many('veterinariaupo.veterinario', 'clinicas_id', string='Veterinarios')

    @api.constrains('telefono')
    def check_telefono(self):
        # Validar que el número de teléfono tenga al menos 7 dígitos
        if len(str(self.telefono)) < 7:
            raise models.ValidationError('El número de teléfono debe tener al menos 7 dígitos.')

    @api.constrains('nombre')
    def check_nombre(self):
        # Validar que el nombre de la clínica no contenga caracteres especiales
        if any(char.isalnum() or char.isspace() for char in self.nombre):
            raise models.ValidationError('El nombre de la clínica no puede contener caracteres especiales.')

    @api.constrains('direccion')
    def check_direccion(self):
        # Validar que la dirección de la clínica no sea demasiado corta
        if len(self.direccion) < 5:
            raise models.ValidationError('La dirección de la clínica debe tener al menos 5 caracteres.')


    
