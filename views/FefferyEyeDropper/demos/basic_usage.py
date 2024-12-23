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
            fac.AntdButton('开启拾取', id='enable-eye-dropper', type='primary'),
            fuc.FefferyEyeDropper(id='eye-dropper-demo'),
            html.Div(
                id='eye-dropper-demo-output',
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
    Output('eye-dropper-demo', 'enable'),
    Input('enable-eye-dropper', 'nClicks'),
    prevent_initial_call=True,
)
def enable_eye_dropper_demo(nClicks):
    return True


@app.callback(
    Output('eye-dropper-demo-output', 'style'),
    Input('eye-dropper-demo', 'color'),
    State('eye-dropper-demo-output', 'style'),
    prevent_initial_call=True,
)
def eye_dropper_demo(color, old_style):
    return {**old_style, 'background': color}


def code_string() -> list:
    """返回当前语种对应的演示代码"""

    return [
        {
            'code': """
fac.AntdSpace(
    [
        fac.AntdButton('开启拾取', id='enable-eye-dropper', type='primary'),
        fuc.FefferyEyeDropper(id='eye-dropper-demo'),
        html.Div(
            id='eye-dropper-demo-output',
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
    Output('eye-dropper-demo', 'enable'),
    Input('enable-eye-dropper', 'nClicks'),
    prevent_initial_call=True,
)
def enable_eye_dropper_demo(nClicks):
    return True


@app.callback(
    Output('eye-dropper-demo-output', 'style'),
    Input('eye-dropper-demo', 'color'),
    State('eye-dropper-demo-output', 'style'),
    prevent_initial_call=True,
)
def eye_dropper_demo(color, old_style):
    return {**old_style, 'background': color}
"""
        }
    ]
