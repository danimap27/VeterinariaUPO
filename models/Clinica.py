from odoo import models, fields, api

class Clinica(models.Model):
    _name = 'veterinariaupo.clinica'
    _description = 'Modelo de la Clinica'
    
    nombre = fields.Char(String = 'nombreCli', size = 256, required = True)
    direccion = fields.Char(String = 'direccionClinica', required=True, help="La dirección de la clínica, se utiliza como clave primaria") #La primary key
    telefono = fields.Integer(int = "telefonoCli", required=True)

    # Relación con la clase Veterinario (1 a muchos)
    veterinarios_ids = fields.One2many('veterinariaupo.veterinario', 'clinicas_id', string='Veterinarios')
    
