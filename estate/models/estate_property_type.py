from odoo import fields, models, api, _

class EstatePropertyType(models.Model):
    _name = "estate.property.type"
    _inherit = "estate.mixin"
    _table = 'real_estate_type'
    _description = "type of property"
    _order = "sequence desc"
    
    sequence = fields.Integer(default=1)

    property_ids = fields.One2many("estate.property", "property_type_id", string="Properties")

    property_count = fields.Integer(compute="_compute_property_count")

    @api.model_create_multi
    def create(self, vals_list):
        res = super().create(vals_list)
        for vals in vals_list:
            self.env["estate.property.tag"].create({"name": vals.get("name")})
        return res        

    def unlink(self):
        self.property_ids.state = "canceled"
        return super().unlink()            

    @api.depends("property_ids")
    def _compute_property_count(self):
        for record in self:
            record.property_count = len(record.property_ids)


    def action_open_property_ids(self):
        return{
            "name" : _("Related properties"),
            "type" : "ir.actions.act_window",
            "view_mode" : "list,form",
            "res_model" : "estate.property",
            "target" : "current",
            "domain" : [("property_type_id","=",self.id)],
            "context": {"default_property_type_id": self.id}
        }