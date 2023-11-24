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

    _sql_constraints = [('microChip sqlConstr','UNIQUE (microChip)','Cada mascota debe tener su propia primary key (primary key')]
 
