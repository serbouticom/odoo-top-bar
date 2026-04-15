{
    "name": "Announcement Bar",
    "version": "17.0.1.0.0",
    "category": "Website",
    "summary": "Display a customizable announcement bar at the top of your website.",
    "description": """
Announcement Bar
================

Display a fully customizable announcement bar at the top of your Odoo website.

Features
--------
* Rich-text message editor with translation support
* Custom background & text colors via visual color picker
* Optional call-to-action button with translatable label and URL
* Closable bar (dismiss button) with session memory
* Schedule visibility with start/end dates
* Multi-website support
* Manage multiple announcements with ordering (drag & drop)
* Accessible from Website > Configuration > Announcement Bar
    """,
    "author": "Mohamed Amine Serbouti",
    "website": "https://github.com/serbouticom",
    "license": "LGPL-3",
    "depends": ["website"],
    "data": [
        "security/ir.model.access.csv",
        "views/announcement_bar_views.xml",
        "views/announcement_bar_template.xml",
    ],
    "assets": {
        "web.assets_frontend": [
            "medamine/static/src/scss/announcement_bar.scss",
            "medamine/static/src/js/announcement_bar.js",
        ],
    },
    "images": [],
    "installable": True,
    "application": False,
    "auto_install": False,
    "development_status": "Production/Stable",
}
