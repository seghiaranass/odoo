from odoo import fields, models 
from datetime import timedelta
class EstatePropertyV1(models.Model):
    _name = "estate_property_v1"
    _description = "Test Model"

    name = fields.Char(required=True)
    description = fields.Text()
    postcode = fields.Char()
    date_availability = fields.Date(copy=False,default=lambda self: fields.date.today() + timedelta(days=90))
    expected_price = fields.Float(required=True)
    selling_price = fields.Float(readonly=True,copy=False)
    bedrooms = fields.Integer(default=2)
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection(
        string='garden_orientation',
        selection=[('north','North'),('south','South'),('east','East'),('west','West')],
        help = "garden_orientation is used to look which orientation that a garden refers to")
    active = fields.Boolean(string='Display', default=True)
    state = fields.Selection(
        string= 'Status',
        selection= [('new','New'),('offer_received','Offer Received'),('offer_accepted','Offer Accepted'),('sold','Sold'),('canceled','Canceled')],
        help= '',
        default = 'new'
    )
    
    