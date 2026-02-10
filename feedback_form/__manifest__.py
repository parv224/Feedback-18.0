{
    "name": "Feedback Form",
    "version": "18.0.1.0.0",
    "summary": "Simple feedback form with rating",
    "category": "Tools",
    "depends": ["base"],
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
    "installable": True,
    "application": False,
}

