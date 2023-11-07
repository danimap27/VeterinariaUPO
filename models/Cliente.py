from odoo import models, fields, api

class Cliente(models.Model):
    _name = 'veterinariaupo.cliente'
    _description = 'Modelo Cliente de la clinica'
    _inherit = 'veterinariaupo.persona'

    idCarnet = fields.Integer(int= 'idCarnet', size = 9, required = True)
    direccion = fields.Char(String = 'direccion', size = 20, required = True)
 
