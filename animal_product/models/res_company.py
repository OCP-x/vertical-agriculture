# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, models, _


class ResCompany(models.Model):
    _inherit = "res.company"

    
    product_livestock_id = fields.Many2one(
        "product.template",
        string="Livestock Product",
        domain=[
            ("detailed_type", "=", "product"),
            # ("route_ids", "in", "manufacture"),
            ("tracking", "=", "serial"),
        ],
    )