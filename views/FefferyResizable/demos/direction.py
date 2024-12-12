import feffery_antd_components as fac
import feffery_utils_components as fuc
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdSpace(
        [
            fuc.FefferyResizable(
                fac.AntdCenter(
                    "direction=['right']",
                    style={
                        'height': '100%',
                        'background': '#dee2e6',
                    },
                ),
                defaultSize={'width': 200, 'height': 200},
                direction=['right'],
            ),
            fuc.FefferyResizable(
                fac.AntdCenter(
                    "direction=['right', 'bottom', 'bottomRight']",
                    style={
                        'height': '100%',
                        'background': '#dee2e6',
                    },
                ),
                defaultSize={'width': 300, 'height': 300},
                direction=['right', 'bottom', 'bottomRight'],
            ),
        ],
        direction='vertical',
        style={'width': '100%'},
    )

    return demo_contents


def code_string() -> list:
    """返回当前语种对应的演示代码"""

    return [
        {
            'code': """
fac.AntdSpace(
    [
        fuc.FefferyResizable(
            fac.AntdCenter(
                "direction=['right']",
                style={
                    'height': '100%',
                    'background': '#dee2e6',
                },
            ),
            defaultSize={'width': 200, 'height': 200},
            direction=['right'],
        ),
        fuc.FefferyResizable(
            fac.AntdCenter(
                "direction=['right', 'bottom', 'bottomRight']",
                style={
                    'height': '100%',
                    'background': '#dee2e6',
                },
            ),
            defaultSize={'width': 300, 'height': 300},
            direction=['right', 'bottom', 'bottomRight'],
        ),
    ],
    direction='vertical',
    style={'width': '100%'},
)
"""
        }
    ]
