# Copyright (C) 2020 Open Source Integrators
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
from odoo import fields, models


class Animal(models.Model):
    _inherit = "animal"

    lot_id = fields.Many2one(
        comodel_name="stock.production.lot",
        # domain=,
        readonly=True
    )
    product_id = fields.Many2one(related="lot_id.product_id", readonly=True)
    product_template_id = fields.Many2one(related="product_id.product_tmpl_id", readonly=True)
    # brand_ranch_id = 
    # brand_year_id = 

    # production_id = fields.Many2one()
    # production_lot = 
    # production_component_ids =
    
    # @api.onchange("lot_id")
