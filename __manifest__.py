# -*- coding: utf-8 -*-
{
    'name': "pwc_module",
    'summary': """Module dedicated to given tasks""",
    'description': """
       Module have a cron that run's every 24 hours and archive all records from sale_order which are older than 7 days.
       It also have wizard where user can manually select records to archive.
    """,
    'author': "Marek Kupka",
    'category': 'Sale',
    'version': '1.1',
    'depends': ['base','sale'],
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'data/pwc_archive_sale_order_cron.xml',
        'wizard/sale_order_archive_wizard_view.xml',
    ],
    'installable': True,
    'application': True,
}
