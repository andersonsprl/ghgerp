# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, models, fields


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    # -------------------------------------------
    # Field Declaration
    # -------------------------------------------

    x_studio_customer_invoice_status = fields.Selection(
        [('Paid', 'Paid'), ('Unpaid', 'Unpaid')], compute='_compute_x_studio_customer_invoice_status')

    # -------------------------------------------
    # Method Declaration
    # -------------------------------------------

    @api.onchange('x_studio_project_main')
    def _onchange_x_studio_project_main(self):
        project_account_configuration = self.env['product.project.config'].search([('project_id.id', '=', self.x_studio_project_main.id)
                                                                                   ], limit=1)
        self.property_account_income_id = project_account_configuration.income_account_id.id
        self.property_account_expense_id = project_account_configuration.expense_account_id.id

    def _compute_x_studio_customer_invoice_status(self):    
        for record in self:
            record.x_studio_customer_invoice_status = record.x_studio_invoice_lines and all(x == 'paid' for x in record.x_studio_invoice_lines.filtered(
                lambda x: x.move_id.move_type == 'out_invoice').mapped("x_studio_payment_status")) and sum(record.x_studio_invoice_lines.filtered(
                lambda x: x.move_id.move_type == 'out_invoice').mapped('quantity')) == sum(record.x_studio_invoice_lines.filtered(
                lambda x: x.move_id.move_type == 'in_invoice').mapped('quantity'))  and 'Paid' or 'Unpaid'
