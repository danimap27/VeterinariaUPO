from odoo import models, fields

class Medicina(models.Model):
    _name = 'veterinariaupo.medicina'
    _description = 'Modelo Medicina'
    _inherit = 'veterinariaupo.persona'
    
    codigo_nacional = fields.Integer('Id Medicina',required=True, help = "Identificador de medicina" ) #Primary key
    nombre = fields.Char('Nombre medicina', size=20, required=True, help="nombre de medicina")
    precio = fields.Float('Precio',(3,2))
    caducidad = fields.Datetime('Caducidad',required=True, autodate = True )
    descripcion = fields.Text('Descripcion')
    prospecto = fields.Char('Prospecto',size = 20,required=True)
    
    laboratorios_id = fields.Many2many('veterinariaupo.laboratorio',string='codigo_nacional')
