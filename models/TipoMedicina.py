from odoo import models, fields,api
import re
class TipoMedicina(models.Model):
    _name = 'veterinariaupo.tipomedicina'
    _description = 'Modelo Tipo Medicina'
    
    nombre = fields.Char('Nombre Tipo Medicina',size=10,required=True)
    #relaciones
    medicinas_ids = fields.Many2one('veterinariaupo.medicina', string='Medicinas')
    
    _sql_constraints = [('nombre_sqlConstr','UNIQUE (nombre)','Cada tipo de medicina tiene un nombre distinto (primary key')]

    @api.onchange('nombre')
    def valida_nombre(self):
        result = {}
        if not self.compruebaNombre(self.nombre):
            result = {
                'value': {'nombre': 'Prototipo'},
                'warning': {
                    'title': 'Error en el nombre',
                    'message': 'El nombre tiene que ser una cadena de caracteres',
                }
            }
        return result
    
    #funcion que comprueba que el nombre sea de tipo string
    def compruebaNombre(self,nombre):
        nombre_str = str(nombre)
        expresion_regular = re.compile(r'^[a-zA-Z]+$')
        return expresion_regular.match(nombre_str)        
        
       
