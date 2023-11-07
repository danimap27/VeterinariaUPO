from odoo import models, fields, api

class Mascota(models.Model):
    _name = 'veterinariaupo.mascota'
    _description = 'Modelo de la mascota del cliente'
    #Atributos mascota
    id = fields.Integer(int='idMascota', required = True)
    nombre = fields.Char(String = 'nombreMascota', size = 256, required = True)
    fechaNacimiento = fields.Datetime('fechaNacimientoMascota',required=True, autodate = True)
    vivo = fields.Binary('Sigue_Vivo')
    sexo = fields.Binary("SexoMascota")
    especie = fields.Char(String="especieMascota", size = 100, required = True)
    raza = fields.Char(String="raza", size = 100)
    peso = fields.Float(float='Peso_Mascosta', required  = True)
    photo = fields.Binary('photo_Mascota')

 
