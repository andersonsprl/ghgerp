# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import models, fields


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    attachments_count = fields.Integer(compute='_compute_attachments_count')

    def _compute_attachments_count(self):
        Attachment = self.env['ir.attachment']
        attachment_ids = []
        for record in self.order_line:
            attachment_ids.append(record.product_id.product_tmpl_id.id)
            attachment_ids.append(record.product_id.id)
        for product in self:
            product.attachments_count = Attachment.search_count(
                [('res_id', '=', attachment_ids)])

    def action_view_attachment(self):
        attachments = []
        for record in self.order_line:
            attachments.append(record.product_id.product_tmpl_id.id)
            attachments.append(record.product_id.id)
        action = self.env["ir.actions.actions"]._for_xml_id("base.action_attachment")
        action['domain'] = [('res_id', 'in', attachments)]
        return action
