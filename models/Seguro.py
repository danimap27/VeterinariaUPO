from odoo import models, fields, api

class Seguro(models.Model):
    _name = 'veterinariaupo.seguro'
    _description = 'Modelo del seguro'
    #Atributos Seguro
    precio = fields.Float(float='precioSeguro', required = True)
    tipo = fields.Char(String = 'tipoSeguro', size = 256, required = True)
    condiciones = fields.Char(String = 'condicionesSeguro',autodate = True)
