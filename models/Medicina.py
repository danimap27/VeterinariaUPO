from odoo import models, fields,api
from datetime import datetime

import re
class Medicina(models.Model):
    _name = 'veterinariaupo.medicina'
    _description = 'Modelo Medicina'
    _rec_name = 'nombre'
    
    codigo_nacional = fields.Float('Id Medicina',digits=(6,1),required=True, help = "Identificador de medicina" ) #Primary key
    nombre = fields.Char('Nombre medicina', size=20, required=True, help="nombre de medicina")
    precio = fields.Float('Precio',(3,2))
    caducidad = fields.Date('Caducidad',required=True, autodate = True )
    descripcion = fields.Text('Descripcion')
    prospecto = fields.Char('Prospecto',size = 20,required=True)
    numTipos = fields.Integer(compute= '_NumTiposTotal',string='Numero de tipos de medicina',store=True)
    estado = fields.Selection([('experimental','Experimental'),
                              ('probada','Probada'),
                              ('descatalogada','Descatalogada'),],
                              'Estado', default='experimental')
   #relaciones
    laboratorios_id = fields.Many2many('veterinariaupo.laboratorio',string='codigo_nacional')
    tratamiento_id = fields.Many2one('veterinariaupo.tratamiento', string='Tratamiento')
    tipos_medicina_id = fields.One2many('veterinariaupo.tipomedicina','medicinas_ids', string='Tipo de Medicinas')
    
    
    _sql_constraints = [('codigo_nacional_sqlConstr','UNIQUE (codigo_nacional)','Cada medicina tiene un codigo distinto (primary key')]


   #funcionalidades
   
    def btn_submit_to_experimental(self):
      self.write({'estado':'experimental'})
  
    #al pasar al estado de descatalogada no se permite relacionar con una cita
    def btn_submit_to_descatalogar(self):
      self.write({'estado':'descatalogada'})
      self.write({'tratamiento_id':[(3,self.tratamiento_id)]})

  
    def btn_submit_to_oficializar(self):
      self.write({'estado':'probada'})
   
    @api.depends('tipos_medicina_id')
    def _NumTiposTotal(self):
      for record in self:
        record.numTipos = len(record.tipos_medicina_id)

   #validaciones
   
   
    
    @api.onchange('caducidad')
    def checkfecha(self):
      if self.caducidad and self.caducidad < fields.Date.today():
        resultado = {
          'value':{'caducidad':fields.Date.today()},
          'warning': {
            'title':'Fecha introducida incorrecta',
            'message':'La medicina ha caducado'
          }
        }
        return resultado
        
    @api.onchange('precio')
    def checkprecio(self):
      if self.precio < 0:
        resultado = {
          'value':{'precio':10.00},
          'warning':{
              'title':'Precio incorrecto',
              'message':'El precio no puede ser menor que 0'
          }
        }
        return resultado
    
    @api.onchange('tratamiento_id')
    def validaTratamiento(self):
      if self.estado == 'descatalogada':
        return {
          'value': {self.tratamiento_id:False,},
          'warning': {
            'title': 'Error en la cita',
            'message': 'No se puede establecer una cita si la medicina está descatalogada',
          }
        }
    
  
      

      
