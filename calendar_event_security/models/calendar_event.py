# © 2025 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html

from odoo import models, fields, api


class CalendarEvent(models.Model):
    _inherit = 'calendar.event'

    message_follower_ids = fields.One2many(auto_join=True)

    @api.depends('partner_ids', 'message_follower_ids')
    @api.depends_context('uid')
    def _compute_user_can_edit(self):
        super()._compute_user_can_edit()
        if self.env.user.has_group("calendar_event_security.group_calendar_event_manager"):
            self.update({"user_can_edit": True})
        else:
            self.filtered(
                lambda x: self.env.user.partner_id in x.message_follower_ids.partner_id
            ).update({"user_can_edit": True})

    def copy(self, default=None):
        self._compute_user_can_edit()
        return super().copy(default=default)
