# Copyright (C) 2020 Open Source Integrators
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
from odoo import api, fields, models


class ProductionLot(models.Model):
    _inherit = "stock.production.lot"

    animal_id = fields.Many2one(
        "animal", string="Animal", index=True, tracking=True
    )

    def action_view_animal(self):
        action = self.env.ref("animal.action_animal").read()[0]
        action["views"] = [(self.env.ref("animal.view_animal_form").id, "form")]
        action["res_id"] = self.animal_id.id or False
        return action
