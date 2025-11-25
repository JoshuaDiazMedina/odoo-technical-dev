from odoo import fields,models, api, _

from datetime import timedelta
from odoo.exceptions import UserError, ValidationError


class EstateProperty(models.Model):
    _name = "estate.property"
    _table = 'real_estate'
    _description = "property model for real estate"
    _order = "price desc"

    name = fields.Char(default="House", required=True)
    active = fields.Boolean(default=True)
    state = fields.Selection([
        ('new', 'New'),
        ('offer_received', 'Offer Received'),
        ('offer_accepted', 'Offer Accepted'),
        ('sold', 'Sold'),
        ('canceled', 'Canceled')
    ], default='new', required=True, copy=False)

    price = fields.Float(copy=False)
    
    selling_price = fields.Float(copy=False, readonly=True)

    def _default_availability_date(self):      
        return fields.Date.today() + timedelta(days=90) 
        
    availability_date = fields.Datetime(default=_default_availability_date,copy=False)
    bedrooms = fields.Integer(default=2)

    property_type_id = fields.Many2one("estate.property.type")

    buyer_id = fields.Many2one("res.partner", string="Buyer", copy=False)
    salesperson_id = fields.Many2one("res.users", string="Salesperson", default=lambda self: self.env.user)

    offer_ids = fields.One2many("estate.property.offer", "property_id", string="Offers")

    tag_ids = fields.Many2many("estate.property.tag", string="Tags")

    living_area = fields.Float(string="Living Area")
    garden = fields.Boolean()
    garden_area = fields.Float(string="Garden Area")
    total_area = fields.Float(compute="_compute_total_area", string="Total Area", store=True)
    
    garden_orientation = fields.Selection([
        ('north', 'North'),
        ('south', 'South'),
        ('east', 'East'),
        ('west', 'West')
    ], string="Garden Orientation")

    @api.depends("living_area", "garden_area")
    def _compute_total_area(self):
        for record in self:
            record.total_area = record.living_area + record.garden_area
    
    best_price = fields.Float(compute="_compute_best_price", string="Best Offer", store=True)

    @api.depends("offer_ids.price")
    def _compute_best_price(self):
        for record in self:
            if record.offer_ids:
                record.best_price = max(record.offer_ids.mapped("price"))
            else:
                record.best_price = 0.0


    @api.onchange("garden")
    def _onchange_garden(self):
        for estate in self:
            if not estate.garden:
                estate.garden_area = 0.0

    @api.onchange("availability_date")
    def _onchange_availability_date(self):
        for estate in self:
            return {
                "warning": {
                    "title": _("Warning"), 
                    "message": _("The availability date has changed.")
                } 
            }          


    def action_set_sold(self):
        self.ensure_one()
        if 'canceled' in self.mapped('state'):
            raise UserError(_("Canceled properties cannot be sold."))            
        return self.write({"state" : "sold"})
        

    def action_set_canceled(self):
        self.ensure_one()
        if 'sold' in self.mapped('state'):
            raise UserError(_("Sold properties cannot be canceled."))            
        return self.write({"state" : "canceled"}) 

    @api.constrains("selling_price","price")
    def _check_constraint(self):
        for record in self:
            if record.selling_price and record.selling_price < (0.9 * record.price):
                raise ValidationError(_("The selling price cannot be lower than 90% of the initial price."))      


    @api.ondelete(at_uninstall=False)
    def _check_can_delete(self):
        for record in self:
            if record.state not in ('new', 'canceled'):
                raise UserError("Solo se pueden borrar propiedades en estado 'New' o 'Canceled'.")                 