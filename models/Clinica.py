from odoo import models, fields, api

class Clinica(models.Model):
    _name = 'veterinariaupo.clinica'
    _description = 'Modelo de la Clinica'

    nombre = fields.Char(string='Nombre de la Clinica', size=256, required=True)
    direccion = fields.Char(string='Dirección de la Clinica', required=True, help="La dirección de la clínica, se utiliza como clave primaria")  # La primary key
    telefono = fields.Integer(string="Teléfono de la Clinica", required=True)

    veterinarios_ids = fields.One2many('veterinariaupo.veterinario', 'clinicas_id', string='Veterinarios')

    @api.onchange('telefono')
    def valida_telefono(self):
        result = {}
        if self.telefono != False and not self.compruebaTelefono(self.telefono):
            result = {
                'value': {'telefono': '666666666'},
                'warning': {
                    'title': 'Error en el telefono',
                    'message': 'El telefono tiene que ser una cadena de 9 dígitos numéricos',
                }
            }
        return result

    def compruebaTelefono(self, telefono):
        if telefono is None or not isinstance(telefono, str) or not re.match(r'^\d{9}$', telefono):
            return False
        return True

    @api.constrains('direccion')
    def check_direccion(self):
        # Validar que la dirección de la clínica no sea demasiado corta
        if len(self.direccion) < 5:
            raise models.ValidationError('La dirección de la clínica debe tener al menos 5 caracteres.')


    
