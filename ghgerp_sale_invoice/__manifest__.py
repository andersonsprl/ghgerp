{
    #  Information

    'name': 'Ghgerp Custom Development',
    'version': '15.1.2',
    'summary': 'Ghgerp Custom Development',
    'description': """
        Ghgerp Custom Development """,
    'category': 'Customization',

    # Author

    'author': 'Odoo PS',
    'website': 'https://www.odoo.com',

    # Dependency
    'depends': [
        'sale_management',
        'account',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/product_project_config_menu.xml',
        'views/product_project_config_view.xml',
        'views/res_partner_views.xml',
        'views/sale_order_view.xml',
        'views/ir_attachment_view.xml',
    ],

    # Other
    'auto_install': False,
    'application': True,
    'installable': True,
}
