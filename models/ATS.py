from odoo import models, fields

class ATS(models.Model):
    _name = 'veterinariaupo.ats'
<<<<<<< HEAD
    _description = 'Modelo ATS'
=======
    _description = 'Modelo ATS (Técnico de Salud Animal)'
>>>>>>> 5b253f2 (Solucion error Herencia)
    _inherit = 'veterinariaupo.persona'
    
    idATS = fields.Char('ID ATS', size=9, required=True, help="Identificación del ATS")
    especialidad = fields.Char('Especialidad', size=20, required=True, help="Especialidad del ATS")
