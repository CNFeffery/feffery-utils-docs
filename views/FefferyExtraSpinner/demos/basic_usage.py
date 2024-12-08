from dash import html
import feffery_antd_components as fac
import feffery_utils_components as fuc
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdRow(
        [
            fac.AntdCol(
                html.Div(
                    [
                        fuc.FefferyExtraSpinner(type=_type),
                        fac.AntdText(_type, copyable=True),
                    ],
                    style={'textAlign': 'center'},
                ),
                xs=24,
                sm=12,
                md=8,
                lg=6,
                xl=4,
                xxl=4,
                style={'padding': '10px'},
            )
            for _type in [
                'ball',
                'swap',
                'bars',
                'grid',
                'wave',
                'push',
                'firework',
                'stage',
                'ring',
                'heart',
                'guard',
                'rotate',
                'spiral',
                'pulse',
                'swish',
                'sequence',
                'impulse',
                'cube',
                'magic',
                'flag',
                'fill',
                'sphere',
                'domino',
                'goo',
                'comb',
                'pong',
                'rainbow',
                'hoop',
                'flapper',
                'jellyfish',
                'trace',
                'classic',
                'whisper',
                'metro',
            ]
        ],
        wrap=True,
    )

    return demo_contents


def code_string() -> list:
    """返回当前语种对应的演示代码"""

    return [
        {
            'code': """
fac.AntdRow(
    [
        fac.AntdCol(
            html.Div(
                [
                    fuc.FefferyExtraSpinner(type=_type),
                    fac.AntdText(_type, copyable=True),
                ],
                style={'textAlign': 'center'},
            ),
            xs=24,
            sm=12,
            md=8,
            lg=6,
            xl=4,
            xxl=4,
            style={'padding': '10px'},
        )
        for _type in [
            'ball',
            'swap',
            'bars',
            'grid',
            'wave',
            'push',
            'firework',
            'stage',
            'ring',
            'heart',
            'guard',
            'rotate',
            'spiral',
            'pulse',
            'swish',
            'sequence',
            'impulse',
            'cube',
            'magic',
            'flag',
            'fill',
            'sphere',
            'domino',
            'goo',
            'comb',
            'pong',
            'rainbow',
            'hoop',
            'flapper',
            'jellyfish',
            'trace',
            'classic',
            'whisper',
            'metro',
        ]
    ],
    wrap=True,
)
"""
        }
    ]
