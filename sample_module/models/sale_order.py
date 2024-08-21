from odoo import api, fields, models

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    spaceship_id = fields.Many2one(
        comodel_name='space.spaceship',
        string="Spaceship",
    )