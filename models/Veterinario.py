from odoo import models, fields

class Veterinario(models.Model):
    _name = 'veterinariaupo.veterinario'
    _description = 'Modelo Veterinario'
    _inherit = 'veterinariaupo.persona'
    
    idVeterinario = fields.Char('ID VETERINARIO', size=9, required=True, help="Identificación del Veterinario")
    #Cambiar por un selection
    especialidad = fields.Char('Especialidad', size=20, required=True, help="Especialidad del Veterinario")
    
    #Esperar a que el modelo este creado
    #clinicas_id = fields.Many2one('veterinariaupo.clinica', string='Clinica')
    #Esperar a que el modelo este creado
    #citas_ids = fields.One2many('veterinariaupo.cita', string = 'Citas del veterinario')