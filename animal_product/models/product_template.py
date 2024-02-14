# Copyright (C) 2020 Open Source Integrators
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
from odoo import api, fields, models


class ProductProduct(models.Model):
    _inherit = "product.product"

    @api.depends("animal_ids")
    def _compute_animal_count(self):
        for rec in self:
            rec.animal_count = len(rec.animal_ids)

    animal_ids = fields.One2many("animal", "product_template_id", string="Animals")
    animal_count = fields.Integer(
        compute=_compute_animal_count, string="Number of Animals", store=True
    )

    def action_view_animals(self):
        action = self.env.ref("animal.action_animal").read()[0]
        if self.animal_count > 1:
            action["domain"] = [("id", "in", self.animal_ids.ids)]
        else:
            action["views"] = [(self.env.ref("animal.view_animal_form").id, "form")]
            action["res_id"] = self.animal_ids and self.animal_ids.ids[0] or False
        return action

    # def action_view_animals(self):
    #     action = self.env.ref("animal.action_animal").read()[0]
    #     if self.animal_count > 1:
    #         action["domain"] = [("id", "in", self.animal_ids.ids)]
    #     else:
    #         action["views"] = [(self.env.ref("animal.view_animal_form").id, "form")]
    #         action["res_id"] = self.animal_ids and self.animal_ids.ids[0] or False
    #     return action
    
    # def action_view_revaluation_origin_lines(self):
    #     self.ensure_one()
    #     action = self.env["ir.actions.act_window"]._for_xml_id(
    #         "account.action_account_moves_all"
    #     )
    #     action["context"] = {}
    #     if len(self.revaluation_origin_line_ids) > 1:
    #         action["domain"] = [("id", "in", self.revaluation_origin_line_ids.ids)]
    #     elif self.revaluation_origin_line_ids:
    #         form_view = [(self.env.ref("account.view_move_line_form").id, "form")]
    #         if "views" in action:
    #             action["views"] = form_view + [
    #                 (state, view) for state, view in action["views"] if view != "form"
    #             ]
    #         else:
    #             action["views"] = form_view
    #         action["res_id"] = self.revaluation_origin_line_ids.id
    #     else:
    #         action = {"type": "ir.actions.act_window_close"}
    #     return action
