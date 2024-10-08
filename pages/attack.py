'''
Page Navigation url : app/attack
Page Description : Allows interaction with Halberd attack modules. Displays attack surfaces, tactics, techniques and corresponding technique config. The main content of the page is generated dynamically by core.Functions.TabContentGenerator (generates the content as per selected attack surface tab), core.Functions.TechniqueOptionsGenerator (generates the techniques available in each tactic of an attack surface) & core.Functions.TechniqueInfoGenerator (generates techniques information pane). The technique configuration form is generated dynamically by callback C004.
'''

import dash_bootstrap_components as dbc
from dash import html, dcc
                   
page_layout = html.Div([
    html.H2("Attack Console", className="text-success mb-3"),
    dbc.Tabs(
        [
            dbc.Tab(label="EntraID", tab_id="tab-attack-EntraID", labelClassName="text-success"),
            dbc.Tab(label="M365", tab_id="tab-attack-M365", labelClassName="text-success"),
            dbc.Tab(label="AWS", tab_id="tab-attack-AWS", labelClassName="text-success"),
            dbc.Tab(label="Azure", tab_id="tab-attack-Azure", labelClassName="text-success"),
        ],
        id="attack-surface-tabs",
        active_tab="tab-attack-EntraID",
        class_name="bg-dark"
    ),
    html.Div(id="tabs-content-div",className="bg-dark", style={"height": "90vh", "justify-content": "center", "align-items": "center"}),
    dcc.Store(id="technique-output-memory-store"),
], className="bg-dark", style={"height": "100vh", 'overflow': 'auto', "padding-right": "20px", "padding-left": "20px"})