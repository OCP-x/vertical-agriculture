# Copyright (C) 2020 Open Source Integrators
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
from odoo import fields, models


class Animal(models.Model):
    _inherit = "animal"

    product_template_id = fields.Many2one(related="herd_id.product_template_id", readonly=True)
    brand_id = fields.Many2one(
        # "product.brand",
        related="herd_id.brand_id",
        readonly=True,
        help="Livestock brand. The value is retrieved from product template.",
    )
    counterbrand_id = fields.Many2one(
        "product.brand",
        # related="product_template_id.brand_id",
        # domain=,
        # states=,
        help="Livestock brand. The value is retrieved from product template.",
    )
    hotbrand = fields.Integer(
        string="Hot Brand",
        # "product.brand",
        # related="product_template_id.brand_id",
        # domain=,
        # states=,
        # help="Livestock brand. The value is retrieved from product template.",
    )
    lot_id = fields.Many2one(
        comodel_name="stock.production.lot",
        # domain=,
        # states=,
    )
    product_id = fields.Many2one(
        # comodel_name="product.product",
        related="lot_id.product_id",
        # domain=,
        readonly=True
    )
    
    # brand_ranch_id = 
    # brand_year_id = 

    # production_id = fields.Many2one()
    # production_lot = 
    # production_component_ids =
    
    # @api.onchange("lot_id")
