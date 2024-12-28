from dash import html
import feffery_utils_components as fuc
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = html.Div(
        fuc.FefferyMotion(
            html.Img(src='/assets/imgs/fuc-logo.svg', width=150),
            animate='漂浮效果',
            variants={
                '漂浮效果': {
                    'y': [25, -25, 25],
                    'rotateZ': ['-15deg', '15deg', '-15deg'],
                    'scale': 1,
                }
            },
            transition={'duration': 3, 'repeat': 'infinity', 'type': 'spring'},
        ),
        style={
            'display': 'flex',
            'justifyContent': 'center',
            'padding': '50px 0',
        },
    )

    return demo_contents


def code_string() -> list:
    """返回当前语种对应的演示代码"""

    return [
        {
            'code': """
html.Div(
    fuc.FefferyMotion(
        html.Img(src='/assets/imgs/fuc-logo.svg', width=150),
        animate='漂浮效果',
        variants={
            '漂浮效果': {
                'y': [25, -25, 25],
                'rotateZ': ['-15deg', '15deg', '-15deg'],
                'scale': 1,
            }
        },
        transition={'duration': 3, 'repeat': 'infinity', 'type': 'spring'},
    ),
    style={
        'display': 'flex',
        'justifyContent': 'center',
        'padding': '50px 0',
    },
)
"""
        }
    ]
