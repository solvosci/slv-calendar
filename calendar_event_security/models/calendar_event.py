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
        for event in self:
            if event.user_can_edit:
                continue

            if self.env.user.partner_id in event.message_follower_ids.partner_id or self.env.user.has_group("calendar_event_security.group_calendar_event_manager"):
                event.user_can_edit = True
