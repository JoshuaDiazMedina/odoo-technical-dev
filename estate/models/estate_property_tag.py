from odoo import fields,models

class EstatePropertyTag(models.Model):
    _name = "estate.property.tag"
    _inherit = "estate.mixin"
    _description = "Estate Property Tag"

    #_sql_constraints = [
    #    ("unique_tag_name", "UNIQUE(name)", "The tag name must be unique."),
    #]
    _order = "name desc"

    