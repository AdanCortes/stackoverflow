from odoo import api, fields, models, tools, _

class Books(models.Model): 
    _name = 'my_module.books'
    
    title = fields.Char(string='Title')
    author = fields.Char(string='Author')
