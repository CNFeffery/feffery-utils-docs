from dash import html
import feffery_antd_components as fac
import feffery_utils_components as fuc
from dash.dependencies import Component, Input, Output

from server import app


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = [
        fuc.FefferyInViewport(
            html.Div(
                '向下滑动观察可见性变化',
                style={
                    'width': '300px',
                    'height': '100px',
                    'background': 'grey',
                    'color': 'white',
                    'display': 'flex',
                    'justifyContent': 'center',
                    'alignItems': 'center',
                    'marginBottom': '300px',
                },
            ),
            id='in-viewport-demo1',
        ),
        fac.AntdTitle(
            id='in-viewport-demo1-output',
            level=5,
            style={'marginBottom': '300px'},
        ),
    ]

    return demo_contents


@app.callback(
    Output('in-viewport-demo1-output', 'children'),
    Input('in-viewport-demo1', 'inViewport'),
)
def in_viewport_demo1(inViewport):
    return f'inViewport: {inViewport}'


def code_string() -> list:
    """返回当前语种对应的演示代码"""

    return [
        {
            'code': """
[
    fuc.FefferyInViewport(
        html.Div(
            '向下滑动观察可见性变化',
            style={
                'width': '300px',
                'height': '100px',
                'background': 'grey',
                'color': 'white',
                'display': 'flex',
                'justifyContent': 'center',
                'alignItems': 'center',
                'marginBottom': '300px',
            },
        ),
        id='in-viewport-demo1',
    ),
    fac.AntdTitle(
        id='in-viewport-demo1-output',
        level=5,
        style={'marginBottom': '300px'},
    ),
]

...

@app.callback(
    Output('in-viewport-demo1-output', 'children'),
    Input('in-viewport-demo1', 'inViewport'),
)
def in_viewport_demo1(inViewport):
    return f'inViewport: {inViewport}'
"""
        }
    ]
