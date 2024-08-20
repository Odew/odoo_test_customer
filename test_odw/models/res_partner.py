from odoo import api, fields, models


class ResPartner(models.Model):
    """
    Res Partner
    """
    _inherit = "res.partner"

    odw_code = fields.Char("ODW Code")