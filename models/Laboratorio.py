from odoo import models, fields, api

class Laboratorio(models.Model):
    _name = 'veterinariaupo.laboratorio'
    _description = 'Modelo del laboratorio'
    #Atributos mascota
    nombre = fields.Char(String = 'nombreLab', size = 256, required = True)
    direccion = fields.Char(String = 'direccionLaboratorio', required=True)
    correo = fields.Char(String = 'correo')
    telefono = fields.Integer(int = "telefonoLab", required=True)

    
