from odoo import models, fields,api
from datetime import datetime

class Tratamiento(models.Model):
    _name = 'veterinariaupo.tratamiento'
    _description = 'Modelo Tratamiento'
    
    
    id_tratamiento = fields.Char('Id tratamiento',size=10, required=True)
    descripcion = fields.Text('Descripcion tratamiento', help="descripcion de tratamiento")
    fin_tratamiento = fields.Date('Fin de tratamiento',required=True, autodate = True )
    inicio_tratamiento = fields.Date('Inicio de tratamiento',required=True, autodate = True )

    cita_id = fields.Many2one('veterinariaupo.cita', string='Cita', required=True)
    medicinas_ids = fields.One2many('veterinariaupo.medicina', 'tratamiento_id', string='Medicinas')
    
    _sql_constraints = [('id_tratamiento_sqlConstr','UNIQUE (id_tratamiento)','Cada tratamiento tiene un id distinto (primary key')]
    #validaciones
    
    @api.constrains('inicio_tratamiento','fin_tratamiento')
    def checkFechas(self):
        if not self.verificaFechas(self.inicio_tratamiento,self.fin_tratamiento):
           raise models.ValidationError('La fecha fin no puede ser menor que la fecha inicio')
        elif not self.verificaFechaPresente(self.inicio_tratamiento,self.fin_tratamiento):
            raise models.ValidationError('Las fechas no pueden estar en el pasado')
    
    
    
    
    #funcion para verificar que las fechas tienen sentido
    def verificaFechas(self,fecha_inicio,fecha_fin):
            return fecha_fin > fecha_inicio
    
    #funcion para verificar que las fechas no estan en el pasado
    
    def verificaFechaPresente(self,fecha_inicio,fecha_fin):
        fecha_actual = fields.Date.context_today(self)
        
        return fecha_inicio >= fecha_actual and fecha_fin >= fecha_actual 
