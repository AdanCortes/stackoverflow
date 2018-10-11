# -*- coding: utf-8 -*-
# References:
#   * [[OCA Module Development][http://odoo-development.readthedocs.io/en/latest/dev/docs/__openerp__.py.html]]

{
    'name': "my_module",
    'summary': "Answer to Stack Overflow Question 52733625",
    'description': "Answer to Stack Overflow Question 52733625",
    'author': "Adán Cortés Medina",
    'website': "http://www.linkedin.com/in/1acme",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/9.0/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['website'],

    # always loaded
    'data': [
        'views/views.xml',
        'security/ir.model.access.csv',
    ],
    # only loaded in demonstration mode
    'demo': [
        #'demo/demo.xml',
    ],
}
