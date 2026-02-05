from odoo.exceptions import ValidationError
from odoo import models, fields, api
import re


class FeedbackForm(models.Model):
    _name = "feedback.form"
    _description = "Feedback Form"
    _rec_name = "full_name"
    _order = "state asc, priority desc, create_date desc"

    name = fields.Char(string="Reference", required=True, readonly=True, default="New")

    full_name = fields.Char(string="Full Name", required=True)
    email = fields.Char(string="Email")
    phone = fields.Char(string="Phone Number")
    comment = fields.Text(string="Comment")

    rating_value = fields.Integer(
        string="Rating (1–5)",
        required=True
    )

    rating_stars = fields.Char(
        string="Rating Stars",
        compute="_compute_rating_stars"
    )

    state = fields.Selection(
        [
            ("new", "New"),
            ("reviewed", "Reviewed"),
        ],
        default="new",
        string="Status"
    )

    priority = fields.Selection(
        [
            ("0", "Low"),
            ("1", "Medium"),
            ("2", "High"),
        ],
        compute="_compute_priority",
        store=True
    )

    create_date = fields.Datetime(string="Submitted On", readonly=True)

    @api.depends("rating_value")
    @api.depends("rating_value")
    def _compute_rating_stars(self):
        for record in self:
            record.rating_stars = "⭐" * (record.rating_value or 0)

    @api.depends("rating_value")
    def _compute_priority(self):
        for record in self:
            if record.rating_value in (1, 2):
                record.priority = "2"  # High
            elif record.rating_value == 3:
                record.priority = "1"  # Medium
            elif record.rating_value in (4, 5):
                record.priority = "0"  # Low
            else:
                record.priority = "0"

    def action_mark_reviewed(self):
        for record in self:
            record.state = "reviewed"

    @api.constrains("rating_value")
    def _check_rating_value(self):
        for record in self:
            if record.rating_value < 1 or record.rating_value > 5:
                raise ValidationError(
                    "Rating must be between 1 and 5."
                )

    @api.constrains("phone")
    def _check_phone_number(self):
        for record in self:
            if record.phone:
                if not record.phone.isdigit():
                    raise ValidationError(
                        "Phone number must contain only digits."
                    )
                if len(record.phone) < 10 or len(record.phone) > 12:
                    raise ValidationError(
                        "Phone number must be between 10 and 12 digits."
                    )

    @api.constrains("email")
    def _check_email_format(self):
        email_regex = r"^[\w\.-]+@[\w\.-]+\.\w+$"
        for record in self:
            if record.email:
                if not re.match(email_regex, record.email):
                    raise ValidationError(
                        "Please enter a valid email address."
                    )

    @api.model
    def create(self, vals):
        if vals.get("name", "New") == "New":
            vals["name"] = self.env["ir.sequence"].next_by_code(
                "feedback.form"
            ) or "New"
        return super().create(vals)
