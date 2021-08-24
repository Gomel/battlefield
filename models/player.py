from odoo import fields, models, api


class Player(models.Model):
    _name = "battlefield.player"

    name = fields.Char(string="Name")
    country = fields.Many2one('res.country', string="Country")
    team = fields.Many2one('battlefield.team', string="Team")
    win = fields.Integer(string="Win")
    losing = fields.Integer(string="Lose")
    win_rate = fields.Float(compute='_compute_win_rate', string="Win rate", digits=(5, 2))
    color = fields.Integer(related='team.color', string="Team color", readonly=True)

    @api.onchange('win', 'losing')
    def _compute_win_rate(self):
        for record in self:
            if record.win > 0 or record.losing > 0:
                record.win_rate = round(record.win / (record.win + record.losing) * 100, 2)
            else:
                record.win_rate = 0
