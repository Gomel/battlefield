{
    'name': 'Battlefield',
    'version': '0.1',
    'author': 'Petushkou Andrei',
    'summary': "Battle tanks game management system",
    'sequence': 1,
    'description':  "Система управления играми",
    'category': 'Uncategorized',
    'website': 'https://github.com/Gomel/battlefield',
    'depends': ['base', 'website'],
    'data': [
        "security/ir.model.access.csv",
        "views/battle_view.xml",
        "views/battle_view.xml",
        "views/game_mode_view.xml",
        "views/player_view.xml",
        "views/arena_view.xml",
        "views/team_view.xml",
        "reports/reports.xml",
        "views/menu_view.xml",
        "views/summary_table_view.xml"
    ],
    'demo': ['demo/demo.xml'],
    'application': True,
    "installable": True
}
