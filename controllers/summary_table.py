# https://www.cybrosys.com/blog/web-controllers-in-odoo
from odoo import http
from odoo.http import request


class SummaryTable(http.Controller):
    @http.route('/summary_table', auth='public', website=True)
    def index(self, **kw):
        summary_table = request.env['battlefield.player'].sudo().search([])
        # Сортировка по убыванию
        summary_table = sorted(summary_table, key=lambda x: x.win_rate, reverse=True)
        return request.render('battlefield.summary_table', {'summary_table': summary_table})
