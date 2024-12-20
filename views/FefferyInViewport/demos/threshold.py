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
            fac.AntdSpace(
                [
                    html.Div(
                        style={
                            'width': '300px',
                            'height': '150px',
                            'background': 'green',
                        }
                    ),
                    html.Div(
                        style={
                            'width': '300px',
                            'height': '150px',
                            'background': 'red',
                        }
                    ),
                ],
                direction='vertical',
                size=0,
            ),
            id='in-viewport-demo2',
            threshold=0.5,
        ),
        fac.AntdTitle(
            id='in-viewport-demo2-output', level=5, style={'margin': '500px 0'}
        ),
    ]

    return demo_contents


@app.callback(
    Output('in-viewport-demo2-output', 'children'),
    Input('in-viewport-demo2', 'inViewport'),
)
def in_viewport_demo2(inViewport):
    return f'inViewport: {inViewport}'


def code_string() -> list:
    """返回当前语种对应的演示代码"""

    return [
        {
            'code': """
[
    fuc.FefferyInViewport(
        fac.AntdSpace(
            [
                html.Div(
                    style={
                        'width': '300px',
                        'height': '150px',
                        'background': 'green',
                    }
                ),
                html.Div(
                    style={
                        'width': '300px',
                        'height': '150px',
                        'background': 'red',
                    }
                ),
            ],
            direction='vertical',
            size=0,
        ),
        id='in-viewport-demo2',
        threshold=0.5,
    ),
    fac.AntdTitle(
        id='in-viewport-demo2-output', level=5, style={'margin': '500px 0'}
    ),
]

...

@app.callback(
    Output('in-viewport-demo2-output', 'children'),
    Input('in-viewport-demo2', 'inViewport'),
)
def in_viewport_demo2(inViewport):
    return f'inViewport: {inViewport}'
"""
        }
    ]
