import feffery_utils_components as fuc
from dash.dependencies import Component, Input, Output

from server import app


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fuc.FefferyDiv(
        id='div-demo1',
        enableEvents=['size'],
        style={
            'height': '200px',
            'background': 'grey',
            'borderRadius': '8px',
            'color': 'white',
            'padding': '20px',
        },
    )

    return demo_contents


@app.callback(
    Output('div-demo1', 'children'),
    [Input('div-demo1', '_width'), Input('div-demo1', '_height')],
    prevent_initial_call=True,
)
def div_demo1(_width, _height):
    return f'_width: {_width}  _height: {_height}'


def code_string() -> list:
    """返回当前语种对应的演示代码"""

    return [
        {
            'code': """
fuc.FefferyDiv(
    id='div-demo1',
    enableEvents=['size'],
    style={
        'height': '200px',
        'background': 'grey',
        'borderRadius': '8px',
        'color': 'white',
        'padding': '20px',
    },
)

...

@app.callback(
    Output('div-demo1', 'children'),
    [Input('div-demo1', '_width'), Input('div-demo1', '_height')],
    prevent_initial_call=True,
)
def div_demo1(_width, _height):
    return f'_width: {_width}  _height: {_height}'
"""
        }
    ]
