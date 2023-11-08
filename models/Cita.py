from odoo import models, fields

class Cita(models.Model):
    _name = 'veterinariaupo.cita'
    _description = 'Modelo Cita'

    
    id_cita = fields.Integer('Id Cita',required=True, help = "Identificador de cita" ) #Primary key
    fecha = fields.Datetime('Fecha',required=True, autodate = True )
    duracion = fields.Integer(int = "Duracion", required=True)
    descripcion = fields.Text('Descripcion')

    # Relación con la clase Mascota (Muchos a 1)
    #microChip = fields.Many2one('veterinariaupo.mascota', string='Mascota')

    # Relación con la clase Veterinario (Muchos a 1)
    #idVeterinario = fields.Many2one('veterinariaupo.veterinario', string='Veterinario')

    # Relación con la clase Tratamiento (1 a muchos)
    #id_tratamiento = fields.One2many('veterinariaupo.tratamiento', 'id_cita', string='Tratamientos')

    # Relación con la clase PruebaMedica (1 a muchos)
    #id_pruebamedica = fields.One2many('veterinariaupo.prueba_medica', 'id_cita', string='Pruebas Médicas')
