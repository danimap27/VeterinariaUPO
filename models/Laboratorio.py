from odoo import models, fields, api

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
    
