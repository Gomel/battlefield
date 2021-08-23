from odoo import fields, models


class Battlefield(models.Model):
    _name = "battlefield.profile"

    uid = fields.Char(string="uid")
    user = fields.Char(string="User")
    name = fields.Char(string="Name")
