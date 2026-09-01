# © 2025 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html


def uninstall_hook(env):
    """At uninstall, revert changes made to record rules"""
    env.ref("calendar.calendar_event_rule_employee").write(
        {
            "name": "All Calendar Event for employees",
            "domain_force": [(1, '=', 1)]
        }
    )
