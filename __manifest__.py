# -*- coding: utf-8 -*-
{
    'name': 'Jinasena : MasterData : MRP',
    'version': '17.0.0.0.5',
    'summary': 'Master-data extracted from CDB for MRP domain.',
    'description': 'Extracted from Clear-DB. Test-env master data. Edit the CSVs in data/ to add/remove rows before install.',
    'author': 'Jinasena Agricultural Machinery (Pvt) Ltd.',
    'category': 'Extra Tools',
    'license': 'LGPL-3',
    'depends': [
        'BugFix-MRP',
        'Jinasena_MasterData_Stock',
        'Jinasena_KnownGood_Data',
    ],
    'data': [
        'data/x_work_center_costing.csv',
        'data/mrp.bom.csv',
        'data/mrp.bom.line.csv',
        'data/x_mrp_bom_material_cos.csv',
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}
