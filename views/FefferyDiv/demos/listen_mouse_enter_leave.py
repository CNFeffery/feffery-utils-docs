import feffery_utils_components as fuc
from dash.dependencies import Component, Input, Output

from server import app


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fuc.FefferyDiv(
        id='div-demo2',
        enableEvents=['mouseenter', 'mouseleave'],
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
