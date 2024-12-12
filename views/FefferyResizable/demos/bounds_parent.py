from dash import html
import feffery_utils_components as fuc
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = html.Div(
        [
            fuc.FefferyResizable(
                html.Div(
                    '示例内容',
                    style={
                        'display': 'flex',
                        'height': '100%',
                        'justifyContent': 'center',
                        'alignItems': 'center',
                        'background': '#dee2e6',
                    },
                ),
                defaultSize={'width': 200, 'height': 200},
                bounds='parent',
            )
        ],
        style={'height': 400, 'width': 400, 'border': '1px solid #868e96'},
    )

    return demo_contents


def code_string() -> list:
    """返回当前语种对应的演示代码"""

    return [
        {
            'code': """
html.Div(
    [
        fuc.FefferyResizable(
            html.Div(
                '示例内容',
                style={
                    'display': 'flex',
                    'height': '100%',
                    'justifyContent': 'center',
                    'alignItems': 'center',
                    'background': '#dee2e6',
                },
            ),
            defaultSize={'width': 200, 'height': 200},
            bounds='parent',
        )
    ],
    style={'height': 400, 'width': 400, 'border': '1px solid #868e96'},
)
"""
        }
    ]
