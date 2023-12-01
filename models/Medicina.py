from odoo import models, fields,api
from datetime import datetime

import re
class Medicina(models.Model):
    _name = 'veterinariaupo.medicina'
    _description = 'Modelo Medicina'
    
    codigo_nacional = fields.Float('Id Medicina',digits=(6,1),required=True, help = "Identificador de medicina" ) #Primary key
    nombre = fields.Char('Nombre medicina', size=20, required=True, help="nombre de medicina")
    precio = fields.Float('Precio',(3,2))
    caducidad = fields.Date('Caducidad',required=True, autodate = True )
    descripcion = fields.Text('Descripcion')
    prospecto = fields.Char('Prospecto',size = 20,required=True)
   #relaciones
    laboratorios_id = fields.Many2many('veterinariaupo.laboratorio',string='codigo_nacional')
    tratamiento_id = fields.Many2one('veterinariaupo.tratamiento', string='Tratamiento')
    tipos_medicina_id = fields.One2many('veterinariaupo.tipomedicina','medicinas_ids', string='Tipo de Medicinas')
    
    _sql_constraints = [('codigo_nacional_sqlConstr','UNIQUE (codigo_nacional)','Cada medicina tiene un codigo distinto (primary key')]

   #validaciones
   
   
    
    @api.constrains('caducidad')
    def checkfecha(self):
      if not self.validaCaducidad(self.caducidad):
        raise models.ValidationError('LA fecha esta en el pasado')
        
    @api.onchange('precio')
    def checkprecio(self):
      if self.precio < 0:
        raise models.ValidationError('El precio no puede ser menor que 0')
    

   
    def validaCaducidad(self,caducidad):
      fecha_actual = fields.Date.context_today(self)
      return caducidad > fecha_actual
     
      
