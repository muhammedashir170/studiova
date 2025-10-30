# -*- coding: utf-8 -*-
{
    'name': 'studiova by XAPP',
    'category': 'Theme/Corporate',
    'version': '18.0.0.0',
    'sequence': 1,
    'author': 'Xapp Pvt. Ltd.',
    'website': 'http://www.bizople.com',
    'summary': '''XAPP''',

    'depends': [
        'website',
        'web_editor',
        'website_sale',
    ],

    'data': [
        "views/navv.xml",
        "views/studiova_banner.xml",
        "views/stats_and_facts.xml",
        "views/studiova_snippets.xml",

    ],

    'images': [
        'static/description/eshop_cover.jpg',
        'static/description/eshop_screenshot.gif',

    ],

    'assets': {
        'web.assets_frontend': [
            '/studiova/static/src/css/studiova_banner.css',
            '/studiova/static/src/css/stats_and_facts.css',
            '/studiova/static/src/css/header.css',
            '/studiova/static/src/js/header.js',
            '/studiova/static/src/js/studiova_banner.js',
            '/studiova/static/src/js/stats_and_facts.js',

        ],
    },

    'installable': True,
    'auto_install': False,
    'application': False,
    'license': 'OPL-1',
}
