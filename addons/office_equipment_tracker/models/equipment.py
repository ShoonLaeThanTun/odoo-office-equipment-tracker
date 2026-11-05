
from odoo import models, fields, api
from odoo.exceptions import ValidationError


class OfficeEquipment(models.Model):
    _name = 'office.equipment.asset'
    _description = 'Office Equipment'
    _order = 'name'

    # Basic equipment information
    name = fields.Char(
        string='Equipment Name',
        required=True
    )

    asset_code = fields.Char(
        string='Asset Code',
        required=True
    )

    category = fields.Selection([
        ('laptop', 'Laptop'),
        ('monitor', 'Monitor'),
        ('keyboard', 'Keyboard'),
        ('mouse', 'Mouse'),
        ('other', 'Other'),
    ], string='Category', required=True)

    # Employee assignment
    assigned_to = fields.Many2one(
        'res.users',
        string='Assigned Employee'
    )

    checkout_date = fields.Date(
        string='Checkout Date'
    )

    due_date = fields.Date(
        string='Due Date'
    )

    return_date = fields.Date(
        string='Return Date'
    )

    # Equipment status
    state = fields.Selection([
        ('available', 'Available'),
        ('assigned', 'Assigned'),
        ('maintenance', 'Maintenance'),
    ], string='Status', default='available', required=True)

    notes = fields.Text(string='Notes')

    # Automatically calculate overdue status
    is_overdue = fields.Boolean(
        string='Overdue',
        compute='_compute_is_overdue',
        search='_search_is_overdue'
    )

    # Prevent duplicate asset codes
    _sql_constraints = [
        (
            'asset_code_unique',
            'unique(asset_code)',
            'Asset Code must be unique!'
        )
    ]

    @api.depends('due_date', 'state')
    def _compute_is_overdue(self):
        today = fields.Date.today()

        for record in self:
            record.is_overdue = bool(
                record.state == 'assigned'
                and record.due_date
                and record.due_date < today
            )

    # Allow users to search for overdue equipment
    @api.model
    def _search_is_overdue(self, operator, value):
        today = fields.Date.today()

        if operator not in ('=', '!='):
            return []

        if (operator == '=' and value) or (
            operator == '!=' and not value
        ):
            return [
                ('state', '=', 'assigned'),
                ('due_date', '<', today)
            ]

        return [
            '|', '|',
            ('state', '!=', 'assigned'),
            ('due_date', '=', False),
            ('due_date', '>=', today)
        ]

    # Require an employee when equipment is assigned
    @api.constrains('state', 'assigned_to')
    def _check_assignment(self):
        for record in self:
            if record.state == 'assigned' and not record.assigned_to:
                raise ValidationError(
                    'Please select an employee before assigning equipment.'
                )

    # Mark equipment as returned
    def action_mark_returned(self):
        for record in self:
            record.write({
                'state': 'available',
                'return_date': fields.Date.today(),
                'assigned_to': False,
            })
