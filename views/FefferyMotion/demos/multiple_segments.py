from dash import html
import feffery_utils_components as fuc
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = html.Div(
        [
            fuc.FefferyMotion(
                style={
                    'background': '#71afe5',
                    'width': '50px',
                    'height': '50px',
                    'marginBottom': '75px',
                },
                animate={
                    'x': [50, 50, 0, 0, 50],
                    'y': [0, 50, 50, 0, 0],
                    'background': [
                        '#d83b01',
                        '#fff100',
                        '#d83b01',
                        '#fff100',
                        '#d83b01',
                    ],
                },
                transition={
                    # 无限循环动画
                    'repeat': 'infinity',
                    'duration': 2,
                },
            ),
            fuc.FefferyMotion(
                style={
                    'background': '#605e5c',
                    'width': '25px',
                    'height': '25px',
                    'borderRadius': '100%',
                    'marginLeft': '25px',
                },
                animate={
                    'scale': [2, 1, 2],
                    'background': ['#e1dfdd', '#605e5c', '#e1dfdd'],
                },
                transition={
                    # 无限循环动画
                    'repeat': 'infinity',
                    'duration': 2,
                    'times': [0.1, 0.9, 1],
                },
            ),
        ],
        style={'width': '200px', 'height': '200px'},
    )

    return demo_contents


def code_string() -> list:
    """返回当前语种对应的演示代码"""

    return [
        {
            'code': """
html.Div(
    [
        fuc.FefferyMotion(
            style={
                'background': '#71afe5',
                'width': '50px',
                'height': '50px',
                'marginBottom': '75px',
            },
            animate={
                'x': [50, 50, 0, 0, 50],
                'y': [0, 50, 50, 0, 0],
                'background': [
                    '#d83b01',
                    '#fff100',
                    '#d83b01',
                    '#fff100',
                    '#d83b01',
                ],
            },
            transition={
                # 无限循环动画
                'repeat': 'infinity',
                'duration': 2,
            },
        ),
        fuc.FefferyMotion(
            style={
                'background': '#605e5c',
                'width': '25px',
                'height': '25px',
                'borderRadius': '100%',
                'marginLeft': '25px',
            },
            animate={
                'scale': [2, 1, 2],
                'background': ['#e1dfdd', '#605e5c', '#e1dfdd'],
            },
            transition={
                # 无限循环动画
                'repeat': 'infinity',
                'duration': 2,
                'times': [0.1, 0.9, 1],
            },
        ),
    ],
    style={'width': '200px', 'height': '200px'},
)
"""
        }
    ]
