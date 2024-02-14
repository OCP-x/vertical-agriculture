# copyright 2022 David BEAL @ Akretion

from odoo import api, fields, models


class AnimalSpecies(models.Model):
    _inherit = "animal.species"

    _parent_name = "parent_id"
    _parent_store = True
    _rec_name = "name"
    _order = "complete_name"

    product_template_id = fields.Many2one(
        comodel_name="product.template",
        # domain=,
        # index=True,
        track_visibility="onchange"
    )
    attribute_id = fields.Many2one(
        comodel_name="product.attribute", 
        # domain=
    )
    attribute_value_id = fields.Many2one(
        comodel_name="product.attribute.value", 
        # domain=
    )