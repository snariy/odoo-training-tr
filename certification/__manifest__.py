# Copyright 2014-2015 Grupo ESOC <www.grupoesoc.es>
# Copyright 2017-Apertoso N.V. (<http://www.apertoso.be>)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
{
    "name": "Certification",
    "summary": "Defines certification for different purposes",
    'version': '12.0.1.0.0',
    "category": "Certificatipn Management",
    "website": "https://github.com/oca/snariy",
    "author": "Grupo ESOC, Tecnativa",

    "license": "AGPL-3",
    "depends": ['base'],
    "data": [
        'security/certification_security.xml',
        'security/ir.model.access.csv',
        'views/certification_view.xml',
        'views/res_partner_view.xml',
        'views/certification_bodies.xml',
        'views/standard_view.xml',
        'reports/certification_report.xml',

    ],
    'demo': ['demo/certification_data.xml'],
    'development_status':'Beta',
    'maintainers':['ceeficent'],
}
