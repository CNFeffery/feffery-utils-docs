from dash import html
import feffery_antd_components as fac
import feffery_utils_components as fuc
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdSpace(
        [
            fac.AntdRow(
                [
                    fac.AntdCol(
                        fuc.FefferySticky(
                            fac.AntdTitle(
                                f'章节{i}',
                                level=4,
                                style={'textAlign': 'center'},
                            ),
                            top=100,
                            bottomBoundary=f'#sticky-target-block{i}',
                            zIndex=999 - i,
                        ),
                        flex='none',
                        style={'width': '140px'},
                    ),
                    fac.AntdCol(
                        html.Div(
                            id=f'sticky-target-block{i}',
                            style={
                                'height': '800px',
                                'background': '#f2f3f5',
                                'marginBottom': '25px',
                            },
                        ),
                        flex='auto',
                    ),
                ]
            )
            for i in range(5)
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
        fac.AntdRow(
            [
                fac.AntdCol(
                    fuc.FefferySticky(
                        fac.AntdTitle(
                            f'章节{i}',
                            level=4,
                            style={'textAlign': 'center'},
                        ),
                        top=100,
                        bottomBoundary=f'#sticky-target-block{i}',
                        zIndex=999 - i,
                    ),
                    flex='none',
                    style={'width': '140px'},
                ),
                fac.AntdCol(
                    html.Div(
                        id=f'sticky-target-block{i}',
                        style={
                            'height': '800px',
                            'background': '#f2f3f5',
                            'marginBottom': '25px',
                        },
                    ),
                    flex='auto',
                ),
            ]
        )
        for i in range(5)
    ],
    direction='vertical',
    style={'width': '100%'},
)
"""
        }
    ]
