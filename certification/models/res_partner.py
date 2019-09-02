from odoo import models,fields

class ResPartner(models.Model):
    _inherit='res.partner'
certification_ids=fields.One2many(comodel_name='certificaiton',inverse_name='owner_id')
is_certificaiton_body=fields.Boolean(string='It is an entity', default='True',help='Check this box if the concact is a ceritification entity')