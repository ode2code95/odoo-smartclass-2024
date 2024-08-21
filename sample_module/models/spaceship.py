from odoo import api, fields, models


class Spaceship(models.Model):
    """Model used to store information about spaceships"""
    _name = 'space.spaceship'
    _description = 'Spaceship'

    name = fields.Char(string="name")
    manufacture_date = fields.Date(string="Date")
    number = fields.Integer(string="Number")

    cost_per_gallon = fields.Float(string="Cost Per Gallon")
    gallons_per_tank = fields.Integer(string="Gallons Per Tank")

    length = fields.Integer(string="Ship Length")
    width = fields.Integer(string="Ship Width")
    height = fields.Integer(string="Ship Height")

    sale_order_ids = fields.One2many(
        comodel_name='sale.order',
        inverse_name='spaceship_id',
        string="Sale Orders",
    )

    pilot_ids = fields.One2many(
        comodel_name='res.partner',
        inverse_name='spaceship_id',
        string="Pilots",
    )

    cost_per_tank = fields.Float(string="Cost To Fill Tank", compute="_compute_cost_per_tank")
    ship_volume = fields.Float(string="Ship Volume", compute="_compute_ship_volume")

    @api.depends('cost_per_gallon', 'gallons_per_tank')
    def _compute_cost_per_tank(self):
        for spaceship in self:
            spaceship.cost_per_tank = spaceship.cost_per_gallon * spaceship.gallons_per_tank

    @api.depends('length', 'width', 'height')
    def _compute_ship_volume(self):
        for spaceship in self:
            spaceship.ship_volume = spaceship.length * spaceship.width * spaceship.height
