# copyright 2022 David BEAL @ Akretion

from odoo import api, fields, models


class Herd(models.Model):
    _inherit = "herd"

    product_template_id = fields.Many2one(
        comodel_name="product.template",
        # domain=,
        # index=True,
        track_visibility="onchange",
    )
    brand_id = fields.Many2one(
        "product.brand",
        string="Brand",
        related="product_template_id.product_brand_id",
        help="Livestock brand. The value is retrieved from product template.",
    )
    attribute_id = fields.Many2one(
        comodel_name="product.attribute",
        # domain=
    )
    attribute_value_id = fields.Many2one(
        comodel_name="product.attribute.value",
        # domain=
    )
