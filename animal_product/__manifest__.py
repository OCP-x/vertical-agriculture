# Copyright (C) 2020 Open Source Integrators
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "Animal Product",
    "version": "15.0.1.0.0",
    "license": "AGPL-3",
    "summary": "Add product to the animal",
    "author": "Open Source Integrators, Odoo Community Association (OCA)",
    "maintainer": "Open Source Integrators",
    "website": "https://github.com/OCA/partner-contact",
    "depends": ["animal"],
    "data": [
        "views/animal_views.xml",
        "views/herd_views.xml",
        "views/product_template_views.xml",
        "views/product_views.xml",
        # "views/res_config_settings_views.xml",
        "views/specie_views.xml",
        "views/stock_production_lot.xml",
    ],
    "development_status": "Beta",
    "maintainers": ["osscar"],
}
