from odoo import models, fields, api

class Cliente(models.Model):
    _name = 'veterinariaupo.cliente'
    _description = 'Modelo Cliente de la clinica'
    _inherit = 'veterinariaupo.persona'

    carnet_id = fields.Integer(int= 'carnet_id', size = 9, required = True, help="Identificador cliente")
    direccion = fields.Char(String = 'direccion', size = 20, required = True, help="Direccion del cliente")
    photo = fields.Binary('photo_Mascota')
    
   mascotas_ids = fields.Many2many('veterinariaupo.mascota', string='Mascota')

