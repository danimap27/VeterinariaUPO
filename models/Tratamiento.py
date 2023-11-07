from odoo import models, fields

class Tratamiento(models.Model):
    _name = 'veterinariaupo.tratamiento'
    _description = 'Modelo Tratamiento'
    
    
    id_tratamiento = fields.Char('Id tratamiento',size=10, required=True)
    descripcion = fields.Text('Descripcion tratamiento', help="descripcion de tratamiento")
    fin_tratamiento = fields.Datetime('Fin de tratamiento',required=True, autodate = True )
    inicio_tratamiento = fields.Datetime('Inicio de tratamiento',required=True, autodate = True )
