from odoo import models, fields, api
from odoo.exceptions import ValidationError

class ATS(models.Model):
    _name = 'veterinariaupo.ats'
    _description = 'Modelo ATS'
    _inherit = 'veterinariaupo.persona'
    
    idATS = fields.Char('ID ATS', size=9, required=True, help="Identificación del ATS")
    especialidad = fields.Char('Especialidad', size=20, required=True, help="Especialidad del ATS")
    
    prueba_medicas = fields.One2many('veterinariaupo.pruebamedica', 'ats_id', string='Pruebas médicas')
    laboratorios_id = fields.Many2one('veterinariaupo.laboratorio', string='Laboratorio')

    _sql_constraints = [
    ('unique_idATS', 'unique(idATS)', 'El ID ATS debe ser único. No se puede agregar dos ATS con el mismo ID.'),
    ]
    
    @api.constrains('idATS')
    def _check_idATS(self):
        for record in self:
            if int(record.idATS) < 0:
                raise ValidationError("El ID ATS no puede ser un valor negativo.")

    @api.onchange('especialidad')
    def _onchange_especialidad(self):
        if self.especialidad:
            self.especialidad = self.especialidad.upper()

    @api.onchange('idATS')
    def comprobar_idATS(self):
      if int(self.idATS) < 0:
        resultado = {
          'value':{'idATS':str(abs(int(self.idATS)))},
          'warning':{
              'title':'Id incorrecto',
              'message':'El id no puede ser menor que 0'
          }
        }
        return resultado