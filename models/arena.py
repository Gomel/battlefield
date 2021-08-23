from odoo import fields, models


class Arena(models.Model):
    _name = "battlefield.arena"

    name = fields.Char(string="Name")
    # available_modes = fields.Char(string="Game modes available")
    available_modes = fields.Many2many("battlefield.game_mode", string="Game modes available")
