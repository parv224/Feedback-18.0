{
    "name": "Feedback Form",
    "version": "18.0.1.0.0",
    "summary": "Simple feedback form with rating",
    "category": "Tools",
    "author": "AppForge",
    "license": "OPL-1",
    "website": "https://www.odoo.com",


    "price": 10.0,
    "currency": "EUR",

    "data": [
        "security/ir.model.access.csv",
        "data/sequence.xml",
        "views/feedback_view.xml",
    ],

    "assets": {
        "web.assets_backend": [
            "feedback_form/static/src/css/feedback.css",
        ],
    },

    "images": ["static/description/cover.png"],

    "installable": True,
    "application": False,
}






















