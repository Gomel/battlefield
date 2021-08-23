from odoo import fields, models


class Battlefield(models.Model):
    _name = "battlefield.battle"

    date = fields.Date(string="Date start")
    arena = fields.Many2one("battlefield.arena", string="Arena")
    status = fields.Char(string="Status")
    mode = fields.Many2one("battlefield.game_mode", string="Game mode")
#    players = fields.Many2many("battlefield.player", string="Players")
    winner = fields.Many2one("battlefield.player", string="Winner")
