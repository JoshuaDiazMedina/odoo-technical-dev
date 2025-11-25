{
    'name' : 'Real Estate',
    'summary' : 'Test Module',
    'version' : '19.0.0.0.0',
    'license' : 'OEEL-1',
    'depends' : ['crm'],
    'author' : 'Joshua Diaz',
    'data' : [
        'security/res_groups.xml',
        'security/ir.model.access.csv',
        'views/estate_property_view.xml',
        'views/estate_property_type_view.xml',
        'views/estate_property_tags_view.xml',
        'views/estate_property_offer_view.xml',
        'views/estate_menus.xml',
    ],
    "demo": [
        'demo/demo.xml'
    ]
}
