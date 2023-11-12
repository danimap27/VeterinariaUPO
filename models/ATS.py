from odoo import models, fields

class ATS(models.Model):
    _name = 'veterinariaupo.ats'
    _description = 'Modelo ATS'
    _inherit = 'veterinariaupo.persona'
    
    idATS = fields.Char('ID ATS', size=9, required=True, help="Identificación del ATS")
    especialidad = fields.Char('Especialidad', size=20, required=True, help="Especialidad del ATS")
    
    prueba_medicas = fields.One2many('veterinariaupo.pruebamedica', 'ats_id', string='Pruebas médicas')
    laboratorios_id = fields.Many2one('veterinariaupo.laboratorio', string='Laboratorio')
