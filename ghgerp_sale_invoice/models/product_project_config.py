# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import fields, models


class ProductProjectConfig(models.Model):
    _name = 'product.project.config'
    _rec_name = 'project_id'

    # -------------------------------------------
    # Field Declaration
    # -------------------------------------------

    project_id = fields.Many2one('project.project', string="Project")
    income_account_id = fields.Many2one('account.account', string="Income Account")
    expense_account_id = fields.Many2one('account.account', string="Expense Account")
