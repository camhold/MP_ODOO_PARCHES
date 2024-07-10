{
    'name': 'custom field restriction',
    'version': '1.5.0.0.0',
    'description': 'custom field restriction in several views in odoo',
    'summary': 'custom field restriction',
    'author': 'Adrian Ramon Hernandez Vidrio',
    'website': 'AdrianRHV_S@outlook.com',
    'license': 'LGPL-3',
    'category': 'account',
    'depends': [
        'analytic', 'product', 'account', 'hr', 'stock',
    ],
    'data': [
        'views/custom_field_restriction.xml',
    ],
    'demo': [

    ],
    'installable': True,
    'auto_install': False,
    'application': False,
    'assets': {

    }
}