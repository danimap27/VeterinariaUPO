from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Cliente(models.Model):
    _name = 'veterinariaupo.cliente'
    _description = 'Modelo Cliente de la clinica'
    _inherit = 'veterinariaupo.persona'

    carnet_id = fields.Integer(int= 'carnet_id', size = 9, required = True, help="Identificador cliente")
    photo = fields.Binary('photo_Cliente')
    
    mascotas_ids = fields.Many2many('veterinariaupo.mascota', string='Mascota')
    
    @api.constrains('carnet_id')
    def _check_carnet_id(self):
        for record in self:
            if record.carnet_id < 0:
                raise ValidationError("El Carnet ID no puede ser un valor negativo.")

    @api.onchange('carnet_id')
    def comprobar_carnet_id(self):
      if self.carnet_id < 0:
        resultado = {
          'value':{'carnet_id':abs(self.carnet_id)},
          'warning':{
              'title':'Id incorrecto',
              'message':'El id no puede ser menor que 0'
          }
        }
        return resultado