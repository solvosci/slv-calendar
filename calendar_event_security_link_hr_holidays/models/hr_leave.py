# © 2025 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html

from odoo import models


class HrLeave(models.Model):
    _inherit = "hr.leave"

    def action_refuse(self):
        if self.env.user.has_group('hr_holidays.group_hr_holidays_user'):
            super(HrLeave, self.sudo()).action_refuse()
        else:
            super(HrLeave, self).action_refuse()
