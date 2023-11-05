from odoo import models, fields

class Veterinario(models.Model):
    _name = 'veterinariaupo.veterinario'
    _description = 'Modelo Veterinario'
    _inherit = 'veterinariaupo.persona'
    
    idATS = fields.Char('ID ATS', size=9, required=True, help="Identificación del Veterinario")
    especialidad = fields.Char('Especialidad', size=20, required=True, help="Especialidad del Veterinario")
