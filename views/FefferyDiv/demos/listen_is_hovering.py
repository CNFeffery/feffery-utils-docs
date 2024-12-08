import feffery_utils_components as fuc
from dash.dependencies import Component, Input, Output

from server import app


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fuc.FefferyDiv(
        id='div-demo5',
        enableEvents=['hover'],
        style={
            'height': '200px',
            'background': 'grey',
            'borderRadius': '8px',
            'color': 'white',
            'padding': '20px',
            'userSelect': 'none',
        },
    )

    return demo_contents


@app.callback(Output('div-demo5', 'children'), Input('div-demo5', 'isHovering'))
def div_demo5(isHovering):
    return f'isHovering: {isHovering}'


def code_string() -> list:
    """返回当前语种对应的演示代码"""

    return [
        {
            'code': """
fuc.FefferyDiv(
    id='div-demo5',
    style={
        'height': '200px',
        'background': 'grey',
        'borderRadius': '8px',
        'color': 'white',
        'padding': '20px',
        'userSelect': 'none',
    },
)

...

@app.callback(Output('div-demo5', 'children'), Input('div-demo5', 'isHovering'))
def div_demo5(isHovering):
    return f'isHovering: {isHovering}'
"""
        }
    ]
