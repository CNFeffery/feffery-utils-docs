import json
from dash import html
import feffery_utils_components as fuc
from dash.dependencies import Component, Input, Output

from server import app


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fuc.FefferyDiv(
        id='div-demo4',
        enableEvents=['contextmenu'],
        style={
            'height': '300px',
            'background': 'grey',
            'borderRadius': '8px',
            'color': 'white',
            'padding': '20px',
            'userSelect': 'none',
        },
    )

    return demo_contents


@app.callback(
    Output('div-demo4', 'children'),
    Input('div-demo4', 'contextMenuEvent'),
    prevent_initial_call=True,
)
def div_demo4(contextMenuEvent):
    return html.Pre(json.dumps(contextMenuEvent, ensure_ascii=False, indent=4))


def code_string() -> list:
    """返回当前语种对应的演示代码"""

    return [
        {
            'code': """
fuc.FefferyDiv(
    id='div-demo4',
    enableEvents=['contextmenu'],
    style={
        'height': '300px',
        'background': 'grey',
        'borderRadius': '8px',
        'color': 'white',
        'padding': '20px',
        'userSelect': 'none',
    },
)

...

@app.callback(
    Output('div-demo4', 'children'),
    Input('div-demo4', 'contextMenuEvent'),
    prevent_initial_call=True,
)
def div_demo4(contextMenuEvent):
    return html.Pre(json.dumps(contextMenuEvent, ensure_ascii=False, indent=4))
"""
        }
    ]
