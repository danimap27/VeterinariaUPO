from odoo import models, fields

class Veterinario(models.Model):
    _name = 'veterinariaupo.veterinario'
    _description = 'Modelo Veterinario'
    _inherit = 'veterinariaupo.persona'
    
    name = fields.Char('ID VETERINARIO', size=9, required=True, help="Identificación del Veterinario")
    especialidad = fields.Selection([('cirugia', 'Cirugía Veterinaria'),('dermatologia', 'Dermatología Veterinaria'),('oftalmologia', 'Oftalmología Veterinaria'),('cardiologia', 'Cardiología Veterinaria'),('neurologia', 'Neurología Veterinaria'),
    ('odontologia', 'Odontología Veterinaria'),
    ('medicina_interna', 'Medicina Interna Veterinaria'),
    ('emergencia', 'Medicina de Emergencia y Cuidados Críticos'),
    ('ortopedia', 'Ortopedia Veterinaria'),
    ('oncologia', 'Oncología Veterinaria'),
    ('reproduccion', 'Reproducción Veterinaria'),
    ('exoticos', 'Medicina de Animales Exóticos'),
    ('anestesiologia', 'Anestesiología Veterinaria')
    ], string='Especialidad', required=True)

    photo = fields.Binary('photo_Veterinario')
    
    clinicas_id = fields.Many2one('veterinariaupo.clinica', string='Clinica')
    cita_ids = fields.One2many('veterinariaupo.cita', 'veterinario_id', string='Citas del veterinario')

