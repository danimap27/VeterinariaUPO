from odoo import models, fields

class TipoMedicina(models.Model):
    _name = 'veterinariaupo.tipomedicina'
    _description = 'Modelo Tipo Medicina'
    
    nombre = fields.Char('Nombre Tipo Medicina',size=10,required=True )
   
   
