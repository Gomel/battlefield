from odoo import fields, models


class Team(models.Model):
    _name = "battlefield.team"

    name = fields.Char(string="Name")
    color = fields.Integer(string="Color")
