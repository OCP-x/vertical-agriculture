# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    product_template_id = fields.Many2one(
        "product.template",
        string="Product Template",
        related="company_id.product_livestock_id",
        # domain=[
        #     ("detailed_type", "=", "product"),
        #     # ("route_ids", "in", "manufacture"),
        #     ("tracking", "=", "serial"),
        # ],
    )
