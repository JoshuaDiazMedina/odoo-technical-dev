from odoo import fields, models, api, _

class EstateMixin(models.Model):
    _name = "estate.mixin"
    _description = "Estate Mixin"

    name = fields.Char(required=True, string="Name")