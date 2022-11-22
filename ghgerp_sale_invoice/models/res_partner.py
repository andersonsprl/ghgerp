# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    # -------------------------------------------
    # Field Declaration
    # -------------------------------------------

    street3 = fields.Char(string='Street3')

    def _display_address(self, without_company=False):
        res = super(ResPartner, self)._display_address(without_company)
        new_address = res.split('\n')
        new_address.insert(2, self.street3 or '')
        return "\n".join(new_address)
