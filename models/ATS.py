from odoo import models, fields, api

class ATS(models.Model):
    _name = 'veterinariaupo.ats'
    _description = 'Modelo ATS'
    _inherit = 'veterinariaupo.persona'
    
    idATS = fields.Char('ID ATS', size=9, required=True, help="Identificación del ATS")
    especialidad = fields.Char('Especialidad', size=20, required=True, help="Especialidad del ATS")
    
    prueba_medicas = fields.One2many('veterinariaupo.pruebamedica', 'ats_id', string='Pruebas médicas')
    laboratorios_id = fields.Many2one('veterinariaupo.laboratorio', string='Laboratorio')

    _sql_constraints = [
        ('unique_idATS', 'unique(idATS)', 'El ID ATS debe ser único.'),
    ]
    
    @api.onchange('especialidad')
    def _onchange_especialidad(self):
        if self.especialidad:
            self.especialidad = self.especialidad.upper()

    @api.onchange('prueba_medicas')
    def _onchange_prueba_medicas(self):
        if self.prueba_medicas:
            total_cost = sum(prueba.costo for prueba in self.prueba_medicas)
            self.total_costo_pruebas = total_cost

    @api.onchange('laboratorios_id')
    def _onchange_laboratorios_id(self):
        if self.laboratorios_id:
            self.direccion_laboratorio = self.laboratorios_id.direccion