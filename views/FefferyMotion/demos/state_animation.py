from dash import html
import feffery_antd_components as fac
import feffery_utils_components as fuc
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdSpace(
        [
            fuc.FefferyMotion(
                '鼠标悬停',
                style={
                    'width': '75px',
                    'borderRadius': '12px',
                    'background': '#71afe5',
                    'textAlign': 'center',
                    'cursor': 'pointer',
                },
                whileHover={'scale': 1.5},
            ),
            fuc.FefferyMotion(
                '鼠标点按',
                style={
                    'width': '75px',
                    'borderRadius': '12px',
                    'background': '#ff8c00',
                    'textAlign': 'center',
                    'cursor': 'pointer',
                },
                whileTap={'scale': 1.5},
            ),
            html.Div(
                [
                    fac.AntdText('向下滑动'),
                    fuc.FefferyMotion(
                        style={
                            'width': '50px',
                            'height': '50px',
                            'background': '#000000',
                            'opacity': 0,
                            'marginBottom': 400,
                            'marginTop': 400,
                        },
                        whileInView={'opacity': 1, 'borderRadius': '100%'},
                        transition={'duration': 3},
                        viewport={'once': False},
                    ),
                ],
                style={
                    'border': '1px dashed #323130',
                    'maxHeight': '150px',
                    'overflow': 'auto',
                    'padding': 25,
                },
            ),
        ],
        direction='vertical',
        size=25,
        style={'paddingLeft': '25px', 'width': '100%'},
    )

    return demo_contents


def code_string() -> list:
    """返回当前语种对应的演示代码"""

    return [
        {
            'code': """
fac.AntdSpace(
    [
        fuc.FefferyMotion(
            '鼠标悬停',
            style={
                'width': '75px',
                'borderRadius': '12px',
                'background': '#71afe5',
                'textAlign': 'center',
                'cursor': 'pointer',
            },
            whileHover={'scale': 1.5},
        ),
        fuc.FefferyMotion(
            '鼠标点按',
            style={
                'width': '75px',
                'borderRadius': '12px',
                'background': '#ff8c00',
                'textAlign': 'center',
                'cursor': 'pointer',
            },
            whileTap={'scale': 1.5},
        ),
        html.Div(
            [
                fac.AntdText('向下滑动'),
                fuc.FefferyMotion(
                    style={
                        'width': '50px',
                        'height': '50px',
                        'background': '#000000',
                        'opacity': 0,
                        'marginBottom': 400,
                        'marginTop': 400,
                    },
                    whileInView={'opacity': 1, 'borderRadius': '100%'},
                    transition={'duration': 3},
                    viewport={'once': False},
                ),
            ],
            style={
                'border': '1px dashed #323130',
                'maxHeight': '150px',
                'overflow': 'auto',
                'padding': 25,
            },
        ),
    ],
    direction='vertical',
    size=25,
    style={'paddingLeft': '25px', 'width': '100%'},
)
"""
        }
    ]
