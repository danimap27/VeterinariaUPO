from odoo import models, fields, api

class Seguro(models.Model):
    _name = 'veterinariaupo.seguro'
    _description = 'Modelo del seguro'
    #Atributos Seguro
    numeroPolica = fields.Integer(int="numPoliza", required = True, help = "Identificador Seguro") #Primary Key
    precio = fields.Float(float='precioSeguro', required = True)
    tipo = fields.Char(String = 'tipoSeguro', size = 256, required = True)
    condiciones = fields.Char(String = 'condicionesSeguro',autodate = True)
