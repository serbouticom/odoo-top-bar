from odoo import models, fields


class AnnouncementBar(models.Model):
    _name = 'medamine.announcement'
    _description = 'Announcement Bar'
    _order = 'sequence asc, id asc'

    name = fields.Char(
        string='Title',
        required=True,
        help='Internal reference name for this announcement.'
    )
    message = fields.Html(
        string='Message',
        required=True,
        sanitize=True,
        translate=True,
        help='The message displayed in the announcement bar.'
    )
    bg_color = fields.Char(
        string='Background Color',
        default='#1a73e8',
        help='Background color of the announcement bar.'
    )
    text_color = fields.Char(
        string='Text Color',
        default='#ffffff',
        help='Text color of the announcement bar.'
    )
    link_url = fields.Char(
        string='Button URL',
        help='Optional URL for the call-to-action button.'
    )
    link_label = fields.Char(
        string='Button Label',
        default='Learn More',
        translate=True,
        help='Label displayed on the call-to-action button.'
    )
    is_closable = fields.Boolean(
        string='Closable',
        default=True,
        help='Allow visitors to close the announcement bar.'
    )
    website_id = fields.Many2one(
        'website',
        string='Website',
        ondelete='cascade',
        help='Leave empty to display on all websites.'
    )
    sequence = fields.Integer(
        string='Sequence',
        default=10,
        help='Used to order announcements. Lower is first.'
    )
    active = fields.Boolean(
        string='Active',
        default=True,
    )
    date_start = fields.Datetime(
        string='Start Date',
        help='Leave empty to show immediately.'
    )
    date_end = fields.Datetime(
        string='End Date',
        help='Leave empty to show indefinitely.'
    )

    def get_active_announcement(self):
        """Return the first active announcement valid for the current datetime."""
        now = fields.Datetime.now()
        domain = [
            ('active', '=', True),
            '|', ('date_start', '=', False), ('date_start', '<=', now),
            '|', ('date_end', '=', False), ('date_end', '>=', now),
        ]
        return self.sudo().search(domain, limit=1)
