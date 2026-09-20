# -*- coding: utf-8 -*-
{
    'name': 'Jinasena : MasterData : MRP',
    'version': '17.0.0.0.2',
    'summary': 'Master-data extracted from CDB for MRP domain.',
    'description': 'Extracted from Clear-DB. Test-env master data. Edit the CSVs in data/ to add/remove rows before install.',
    'author': 'Jinasena Agricultural Machinery (Pvt) Ltd.',
    'category': 'Extra Tools',
    'license': 'LGPL-3',
    'depends': [
        'BugFix-MRP',
        'Jinasena_MasterData_Stock',
    ],
    'data': [
        'data/mrp.bom.csv',
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}
