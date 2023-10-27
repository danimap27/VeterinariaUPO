from odoo import models, fields

class Persona(models.Model):
    _name = "veterinariaupo.persona"
    _description = "Modelo de Persona"
    
    dni = fields.Char('DNI', size=9, required=True, help="Documento Nacional de Identidad")
    nombre = fields.Char('Nombre', size=100, required=True)
    apellidos = fields.Char('Apellidos', size=100, required=True)
    direccion = fields.Char('Direccion', size=100, required=True)
    telefono = fields.Char('Telefono', size=9, required=True, help="Número de teléfono")
    correo = fields.Char('Correo', size=100, required=True, help="Correo electrónico")
