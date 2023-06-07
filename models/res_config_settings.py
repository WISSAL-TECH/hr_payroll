# -*- coding: utf-8 -*-
"""Module for configuration settings related to payroll modules"""
from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    "configuration settings related to payroll modules"
    _inherit = 'res.config.settings'

    module_account_accountant = fields.Boolean(string='Account Accountant')
    module_l10n_fr_hr_payroll = fields.Boolean(string='French Payroll')
    module_l10n_be_hr_payroll = fields.Boolean(string='Belgium Payroll')
    module_l10n_in_hr_payroll = fields.Boolean(string='Indian Payroll')
