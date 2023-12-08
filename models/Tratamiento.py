from odoo import models, fields,api
from datetime import datetime

class Tratamiento(models.Model):
    _name = 'veterinariaupo.tratamiento'
    _description = 'Modelo Tratamiento'
    _rec_name = 'id_tratamiento'
    
    id_tratamiento = fields.Char('Id tratamiento',size=10, required=True)
    descripcion = fields.Text('Descripcion tratamiento', help="descripcion de tratamiento")
    fin_tratamiento = fields.Date('Fin de tratamiento',required=True, autodate = True )
    inicio_tratamiento = fields.Date('Inicio de tratamiento',required=True, autodate = True )
    estado = fields.Selection([('disponible','Disponible'),
                                ('cancelado','Cancelado'),],
                                 'Estado', default='disponible')
    
    cita_id = fields.Many2one('veterinariaupo.cita', string='Cita')
    medicinas_ids = fields.One2many('veterinariaupo.medicina', 'tratamiento_id', string='Medicinas')
    
    _sql_constraints = [('id_tratamiento_sqlConstr','UNIQUE (id_tratamiento)','Cada tratamiento tiene un id distinto (primary key')]

    #funcionalidades    
    def btn_submit_to_disponible(self):
        self.write({'estado':'disponible'})
    
    #Si el tratamiento es cancelado se elimina la cita relacionado a el
    def btn_submit_to_cancelado(self):
        self.write({'estado':'cancelado'})
        
        self.write({'cita_id':[(3,self.cita_id)]})
        
    #validaciones
    @api.onchange('inicio_tratamiento','fin_tratamiento')
    def checkFechas(self):
        resultado = {}
        if self.inicio_tratamiento and self.fin_tratamiento and self.inicio_tratamiento > self.fin_tratamiento:
            resultado = {
                'value':{'inicio_tratamiento':fields.Date.today(),'fin_tratamiento':fields.Date.today()},
                'warning':{
                    'title':'Fecha introducida incorrecta',
                    'message':'La fecha inicio no puede ser mayor que la fecha fin'
                }
            }
        elif self.inicio_tratamiento and self.fin_tratamiento:
            if self.inicio_tratamiento < fields.Date.today() or self.fin_tratamiento < fields.Date.today():
                resultado = {
                    'value':{'inicio_tratamiento':fields.Date.today(),'fin_tratamiento':fields.Date.today()},
                    'warning':{
                        'title':'Fecha introducida incorrecta',
                        'message':'Ninguna de las fechas pueden estar en el pasado'
                }
            }
        return resultado
        
    @api.onchange('cita_id')
    def validaTratamientoCancel(self):
        resultado = {}
        if self.estado == 'cancelado':
            resultado = {
                'warning':{
                    'title':'Estado no compatible con cita',
                    'message':'No se puede establecer relacionar una cita si el estado es cancelado'
            }
        }
        return resultado
   
