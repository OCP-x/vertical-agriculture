# copyright 2022 David BEAL @ Akretion

from odoo import api, fields, models


class Herd(models.Model):
    _name = "herd"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = "Herd Inventory"
    _rec_name = "display_name"

    product_template_id = fields.Many2one(
        comodel_name="product.template",
        # domain=,
        index=True,
        tracking=True
    )