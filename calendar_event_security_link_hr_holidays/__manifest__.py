# © 2025 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html
{
    "name": "Calendar Event Security Link Hr Holidays",
    "summary": """
        This module links calendar_event_security with hr_holidays with the necessary functionalities required by hr_holidays
        to work correctly with calendar_event_security installed.
        - 'All Approver' users can refuse any leave
    """,
    "author": "Solvos",
    "license": "LGPL-3",
    "version": "13.0.1.0.0",
    "category": "Account",
    "website": "https://github.com/solvosci/slv-calendar",
    "depends": [
        "calendar_event_security",
        "hr_holidays",
    ],
    "installable": True,
}
