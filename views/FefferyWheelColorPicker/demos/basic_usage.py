from dash import html
import feffery_antd_components as fac
import feffery_utils_components as fuc
from dash.dependencies import Component, Input, Output, State

from server import app


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdSpace(
        [
            fuc.FefferyWheelColorPicker(id='wheel-color-picker-demo'),
            html.Div(
                id='wheel-color-picker-demo-output',
                style={
                    'width': '200px',
                    'height': '200px',
                    'display': 'flex',
                    'alignItems': 'center',
                    'justifyContent': 'center',
                    'borderRadius': '5px',
                    'boxShadow': '0px 0px 12px rgba(0, 0, 0, .12)',
                    'transition': '0.25s',
                },
            ),
        ],
        size='large',
    )

    return demo_contents


@app.callback(
    [
        Output('wheel-color-picker-demo-output', 'style'),
        Output('wheel-color-picker-demo-output', 'children'),
    ],
    Input('wheel-color-picker-demo', 'color'),
    State('wheel-color-picker-demo-output', 'style'),
)
def wheel_color_picker_demo(color, old_style):
    return [{**old_style, 'background': color}, color]


def code_string() -> list:
    """返回当前语种对应的演示代码"""

    return [
        {
            'code': """
fac.AntdSpace(
    [
        fuc.FefferyWheelColorPicker(id='wheel-color-picker-demo'),
        html.Div(
            id='wheel-color-picker-demo-output',
            style={
                'width': '200px',
                'height': '200px',
                'display': 'flex',
                'alignItems': 'center',
                'justifyContent': 'center',
                'borderRadius': '5px',
                'boxShadow': '0px 0px 12px rgba(0, 0, 0, .12)',
                'transition': '0.25s',
            },
        ),
    ],
    size='large',
)

...

@app.callback(
    [
        Output('wheel-color-picker-demo-output', 'style'),
        Output('wheel-color-picker-demo-output', 'children'),
    ],
    Input('wheel-color-picker-demo', 'color'),
    State('wheel-color-picker-demo-output', 'style'),
)
def wheel_color_picker_demo(color, old_style):
    return [{**old_style, 'background': color}, color]
"""
        }
    ]
