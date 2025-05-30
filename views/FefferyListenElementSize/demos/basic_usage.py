import feffery_antd_components as fac
import feffery_utils_components as fuc
from dash.dependencies import Component, Input, Output

from server import app


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = [
        fuc.FefferyListenElementSize(
            id='listen-element-size-demo',
            target='listen-element-size-demo-output',
        ),
        fac.AntdCenter(
            id='listen-element-size-demo-output',
            style={'border': '1px dashed #69c0ff', 'height': 300},
        ),
    ]

    return demo_contents


@app.callback(
    Output('listen-element-size-demo-output', 'children'),
    [
        Input('listen-element-size-demo', 'width'),
        Input('listen-element-size-demo', 'height'),
    ],
)
def listen_element_size_demo(width, height):
    return f'width: {width}, height: {height}'


def code_string() -> list:
    """返回当前语种对应的演示代码"""

    return [
        {
            'code': """
[
    fuc.FefferyListenElementSize(
        id='listen-element-size-demo',
        target='listen-element-size-demo-output',
    ),
    fac.AntdCenter(
        id='listen-element-size-demo-output',
        style={'border': '1px dashed #69c0ff', 'height': 300},
    ),
]

...

@app.callback(
    Output('listen-element-size-demo-output', 'children'),
    [
        Input('listen-element-size-demo', 'width'),
        Input('listen-element-size-demo', 'height'),
    ],
)
def listen_element_size_demo(width, height):
    return f'width: {width}, height: {height}'
"""
        }
    ]
