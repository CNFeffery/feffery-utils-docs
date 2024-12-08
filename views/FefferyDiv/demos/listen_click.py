import feffery_utils_components as fuc
from dash.dependencies import Component, Input, Output

from server import app


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fuc.FefferyDiv(
        id='div-demo3',
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


@app.callback(
    Output('div-demo3', 'children'),
    [Input('div-demo3', 'nClicks'), Input('div-demo3', 'nDoubleClicks')],
)
def div_demo3(nClicks, nDoubleClicks):
    return f'nClicks: {nClicks} nDoubleClicks: {nDoubleClicks}'


def code_string() -> list:
    """返回当前语种对应的演示代码"""

    return [
        {
            'code': """
fuc.FefferyDiv(
    id='div-demo2',
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
    Output('div-demo2', 'children'),
    [
        Input('div-demo2', 'mouseEnterCount'),
        Input('div-demo2', 'mouseLeaveCount'),
    ],
)
def div_demo2(mouseEnterCount, mouseLeaveCount):
    return (
        f'mouseEnterCount: {mouseEnterCount} mouseLeaveCount: {mouseLeaveCount}'
    )
"""
        }
    ]
