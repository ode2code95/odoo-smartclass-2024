from odoo import api, fields, models

class ResPartner(models.Model):
    _inherit = 'res.partner'

    spaceship_id = fields.Many2one(
        comodel_name='space.spaceship',
        string="Spaceship",
    )