from odoo import models, fields, api

class Seguro(models.Model):
    _name = 'veterinariaupo.seguro'
    _description = 'Modelo del seguro'
    #Atributos Seguro
    numeroPoliza = fields.Integer(int="numPoliza", required = True, help = "Identificador Seguro") #Primary Key , compute='_calculoNumPoliza', store=True
    precio = fields.Float(float='precioSeguro', required = True)
    tipo = fields.Selection([('todoRiesgo','Seguro a todo riesgo'),
                                     ('seguroTerceros','Seguro a terceros'),
                                     ('seguroVida','Seguro de vida'),
                                     ], 
                                     'Tipo de Seguro', required = True)
    condiciones = fields.Char(String = 'condicionesSeguro',autodate = True)

    idMascota = fields.One2many('veterinariaupo.mascota','microChip','Mascota')

    _sql_constraints = [('numeroPoliza_sqlConstr','UNIQUE (numeroPoliza)','Cada seguro tiene un numero de poliza distinto (primary key')]
    
    def btn_submit_to_tipo(self):
        if self.tipo == 'todoRiesgo':
            self.write({'tipo': 'seguroTerceros'})
        elif self.tipo == 'seguroTerceros':
            self.write({'tipo': 'seguroVida'})
        else:
            self.write({'tipo': 'todoRiesgo'})

        
    
    ##@api.depends('idMascota')
    ##def _calculoNumPoliza(self): 
    ##        self.numeroPoliza = (self.idMascota * 2)
    ##
            
    @api.onchange('precio')
    def onchange_precio_seguro(self):
        resultado = {}
        if self.precio < 0:
            resultado = {
                'value': {'precio':0},
                'warning': {
                     'title':'Valores incorrectos',
                     'message':'No puede tener precio negativo'
                }
            }
            return resultado
