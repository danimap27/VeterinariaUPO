from odoo import models, fields, api

class Mascota(models.Model):
    _name = 'veterinariaupo.mascota'
    _description = 'Modelo de la mascota del cliente'
    #Atributos mascota
    microChip = fields.Integer('idMascota', required = True) #Primary Key de Mascota
    nombre = fields.Char(String = 'nombreMascota', size = 256, required = True)
    fechaNacimiento = fields.Datetime('fechaNacimientoMascota',required=True, autodate = True)
    vivo = fields.Selection([('vivo','Vivo'),('muerto','Muerto')])
    sexo = fields.Selection([('macho','Macho'),('hembra','Hembra')])
    especie = fields.Selection([('dog','Perro'),
                                     ('cat','Gato'),
                                     ('bird','Pajaro'),
                                     ], 
                                     'Type of pet', required = True)
    raza = fields.Char(String="raza", size = 100)
    peso = fields.Float(float='Peso_Mascosta', required  = True)
    photo = fields.Binary('photo_Mascota')

    carnets_id = fields.Many2many('veterinariaupo.cliente',string='Duenyo de la mascota')
    seguro_id = fields.Many2one('veterinariaupo.seguro', string='Numero de Poliza')
    citas_ids = fields.One2many('veterinariaupo.cita', 'microChip', string='Citas de la mascota')

    _sql_constraints = [('microChip_sqlConstr','UNIQUE (microChip)','Cada mascota debe tener su propia primary key (primary key')]
    
    def btn_submit_to_vivo(self):
        if(self.vivo == 'Vivo'):
            self.write({'vivo':'Muerto'})
        else:
            self.write({'vivo':'Vivo'})
        
 
    @api.onchange('fechaNacimiento')
    def _onchange_fechaNacimiento(self):
            if self.fechaNacimiento and self.fechaNacimiento > fields.Date.today():
                resultado = {
                'warning': {
                     'title':'Fecha Introducida no valida',
                     'message':'No puede ser posterior a la fecha actual'
                }
            }
            return resultado
            
    @api.onchange('peso')
    def _onchange_Peso(self):
        if self.peso < 0:
            resultado = {
                'value': {'peso':0},
                'warning': {
                     'title':'Valores incorrectos',
                     'message':'No puede ser un peso negativo'
                }
            }
            return resultado
                
