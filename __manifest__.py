# -*- coding: utf-8 -*-
{
    'name': "VeterinariaUPO",

    'summary': """
        Gestionar una clinica Veterinaria""",

    'description': """
        Con este modulo se podran gestionar todos los tramites y sus
    """,

    'author': "VeterinariaUPO S.L.",
    'website': "https://github.com/danimap27/VeterinariaUPO",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Aplicaciones',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/veterinario_view.xml',
        'views/views.xml',
        'views/templates.xml',
        'views/menu.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
