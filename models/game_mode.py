from odoo import fields, models


class GameMode(models.Model):
    _name = "battlefield.game_mode"

    name = fields.Char(string="Name")
    rounds_count = fields.Integer(string="Round count")
    round_time = fields.Integer(string="Round time (min)")
    point_to_win = fields.Integer(string="Points to win")
    friendly_fire = fields.Boolean(string="Friendly fire", default=False)
    bases_capture = fields.Boolean(string="Bases capture", default=False)
