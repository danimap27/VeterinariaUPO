from odoo import models, fields, api
import re

class Persona(models.Model):
    _name = "veterinariaupo.persona"
    _description = "Modelo de Persona"
    
    dni = fields.Char('DNI', size=9, required=True, help="Documento Nacional de Identidad")
    nombre = fields.Char('Nombre', size=100, required=True)
    apellidos = fields.Char('Apellidos', size=100, required=True)
    direccion = fields.Char('Direccion', size=100, required=True)
    telefono = fields.Char('Telefono', size=9, required=True, help="Número de teléfono")
    correo = fields.Char('Correo', size=100, help="Correo electrónico")

    @api.onchange('telefono')
    def valida_telefono(self):
        result = {}
        if not self.compruebaTelefono(self.telefono):
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
    
    @api.onchange('dni')
    def valida_dni(self):
        try:
            if not self.compruebaDni(self.dni):
                return {
                    'value': {'dni': '12345678R'},
                    'warning': {
                        'title': 'Error en el dni',
                        'message': 'El dni debe ser una cadena de 8 dígitos seguidos por una letra',
                    }
                }
        except TypeError:
            return {
                'warning': {
                    'title': 'Error en el dni',
                    'message': 'El dni debe ser una cadena de 8 dígitos seguidos por una letra',
                }
            }

    def compruebaDni(self, dni):
        if not isinstance(dni, str) or not re.match(r'^\d{8}[a-zA-Z]$', dni):
            return False
        return True