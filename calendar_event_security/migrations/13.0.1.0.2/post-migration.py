# © 2025 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html

from openupgradelib import openupgrade


@openupgrade.migrate()
def migrate(env, version):

    openupgrade.load_data(
        env.cr, "calendar_event_security", "migrations/13.0.1.0.2/noupdate_changes.xml"
    )
