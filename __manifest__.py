# -*- coding: utf-8 -*-
{
    'name': "veterinariaupo",

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
        'reports/reports.xml',
        'reports/cliente_report.xml',
        'reports/veterinario_report.xml', 
        'reports/ats_report.xml',
        'reports/mascota_report.xml', 
        'reports/seguro_report.xml', 
        'reports/laboratorio_report.xml',
        'reports/cita_report.xml',
        'reports/clinica_report.xml',
        'reports/pruebamedica_report.xml',
        'reports/tipomedicina_report.xml',
        'reports/medicina_report.xml',
        'reports/tratamiento_report.xml',     
        'views/ats_view.xml',
        'views/cliente_view.xml',
        'views/laboratorio_view.xml',
        'views/veterinario_view.xml',
        'views/cita_view.xml',
        'views/seguro_view.xml',
        'views/mascota_view.xml',
        'views/clinica_view.xml',
        'views/medicina_view.xml',
        'views/tipomedicina_view.xml',
        'views/tratamiento_view.xml',
        'views/pruebamedica_view.xml',
        'views/views.xml',
        'views/templates.xml',
        'views/owl.xml',
        'views/menu.xml',
    ],
    # only loaded in demonstration mode
    'demo': [      
        'demo/veterinariaupo.ats.csv',
        'demo/veterinariaupo.veterinario.csv',
        'demo/veterinariaupo.cliente.csv',
        'demo/veterinariaupo.mascota.csv',
        'demo/veterinariaupo.seguro.csv',
        'demo/veterinariaupo.medicina.csv',
        'demo/veterinariaupo.tratamiento.csv',
        'demo/veterinariaupo.tipomedicina.csv'
        
    ],
    'assets': {
    'web.assets_backend': [
        'static/src/components/*/*.js',
        'static/src/components/*/*.xml',
        'static/src/components/*/*.scss',
        ],
    },
    'images': ['static/description/icon.png'],
    'auto_install': True,
    'application': True,
    'logo': {
        '128': 'src/logo.png'
    }
}

