from odoo import api, fields, models
"""extends the base model 'hr.leave.type' """

class HolidaysType(models.Model):
    """Time Off Type Model."""
    _inherit = "hr.leave.type"
    _description = "Time Off Type"

    code = fields.Char('code')
