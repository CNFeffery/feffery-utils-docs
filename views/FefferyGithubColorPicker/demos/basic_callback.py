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
            fuc.FefferyGithubColorPicker(id='github-color-picker-demo'),
            html.Div(
                id='github-color-picker-demo-output',
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
    Output('github-color-picker-demo-output', 'style'),
    Input('github-color-picker-demo', 'color'),
    State('github-color-picker-demo-output', 'style'),
)
def github_color_picker_demo(color, old_style):
    return {**old_style, 'background': color}


def code_string() -> list:
    """返回当前语种对应的演示代码"""

    return [
        {
            'code': """
fac.AntdSpace(
    [
        fuc.FefferyGithubColorPicker(id='github-color-picker-demo'),
        html.Div(
            id='github-color-picker-demo-output',
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
    Output('github-color-picker-demo-output', 'style'),
    Input('github-color-picker-demo', 'color'),
    State('github-color-picker-demo-output', 'style'),
)
def github_color_picker_demo(color, old_style):
    return {**old_style, 'background': color}
"""
        }
    ]
