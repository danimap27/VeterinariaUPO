from odoo import models, fields, api

class Seguro(models.Model):
    _name = 'veterinariaupo.seguro'
    _description = 'Modelo del seguro'
    #Atributos Seguro
    numeroPoliza = fields.Integer(int="numPoliza", required = True, help = "Identificador Seguro") #Primary Key
    precio = fields.Float(float='precioSeguro', required = True)
    tipo = fields.Char(String = 'tipoSeguro', size = 256, required = True)
    condiciones = fields.Char(String = 'condicionesSeguro',autodate = True)

    idMascota = fields.One2many('veterinariaupo.mascota','microChip','Mascota')

    _sql_constraints = [('numeroPoliza sqlConstr','UNIQUE (numeroPoliza)','Cada seguro tiene un numero de poliza distinto (primary key')]

    @api.depends('idMascota')
    def _calculoNumPoliza(self): 
            self.numeroPoliza = (self.idMascota * 2)
