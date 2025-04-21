# © 2025 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html
{
    "name": "Calendar Event Security",
    "summary": """
        By default, all users can modify/delete a calendar event if they are followers of the event or not.
        To restrict that, now only the followers of an calendar event will be able to modify/delete it.
        Also, there is a new group in "Extra Rights" that allows a user, follower or not, to modify/delete an calendar event.
        By default, user admin will be able to modify and delete calendar events.
    """,
    "author": "Solvos",
    "license": "LGPL-3",
    "version": "13.0.1.0.0",
    "category": "Account",
    "website": "https://github.com/solvosci/slv-calendar",
    "depends": [
        "calendar",
    ],
    "data": [
        "security/calendar_event.xml",
    ],
    "installable": True,
}
