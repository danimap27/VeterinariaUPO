from odoo import models, fields

class PruebaMedica(models.Model):
    _name = 'veterinariaupo.pruebamedica'
    _description = 'Modelo PruebaMedica'

    
    id_pruebamedica = fields.Integer('numPruebaMedica',required=True, help = "Identificador de prueba medica" ) #Primary key
    tipo = fields.Char(String = 'tipoPruebaMedica', size = 256, required = True)
    fecha = fields.Datetime('Fecha',required=True, autodate = True ) 
    descripcion = fields.Text('Descripcion')

    # Relación con la clase ATS (Muchos a 1)
    #idATS = fields.Many2one('veterinariaupo.ats', string='ATS')

    # Relación con la clase Cita (Muchos a 1)
    #cita_id = fields.Many2one('veterinariaupo.cita', string='Cita')
