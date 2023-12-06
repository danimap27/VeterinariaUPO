from odoo import models, fields, api
#Import re sirve para trabajar con expresiones regulares en python
import re

class Laboratorio(models.Model):
    _name = 'veterinariaupo.laboratorio'
    _description = 'Modelo del laboratorio'
    #Atributos Laboratorio
    nombre = fields.Char(String = 'nombreLab', size = 256, required = True)
    direccion = fields.Char(String = 'direccionLaboratorio', required=True) #La primary key
    correo = fields.Char(String = 'correo')
    telefono = fields.Integer(int = "telefonoLab", required=True)

    codigo_nacional = fields.Many2many('veterinariaupo.medicina', string='Medicina')
    atsID = fields.One2many('veterinariaupo.ats','direccion','ATS')

    _sql_constraints = [('direccionLabUnica','UNIQUE (direccion)','Solo puede haber un laboratorio por direccion (primary key')]
    @api.onchange('telefono')
    def valida_telefono(self):
        result = {}
        if self.telefono != False and not self.compruebaTelefono(self.telefono):
            result = {
                'value': {'telefono': '666666666'},
                'warning': {
                    'title': 'Error en el telefono',
                    'message': 'El telefono tiene que ser una cadena de 9 digitos numericos',
                }
            }
        return result
    
    #Mediante expresion regular comprueba que el numero de telefono tenga 9 digitos, todos numeros
    def compruebaTelefono(self,telefono):
        telefono_str = str(telefono)
        expresion_regular = re.compile(r'^\d{9}$')
        return expresion_regular.match(telefono_str)      
