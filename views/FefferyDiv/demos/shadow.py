import feffery_antd_components as fac
import feffery_utils_components as fuc
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdSpace(
        [
            fuc.FefferyDiv(
                f'shadow="{shadow}"',
                shadow=shadow,
                style={
                    'width': '220px',
                    'height': '100px',
                    'borderRadius': '6px',
                    'border': '1px solid #f1f2f6',
                    'display': 'flex',
                    'justifyContent': 'center',
                    'alignItems': 'center',
                },
            )
            for shadow in [
                'no-shadow',
                'hover-shadow',
                'always-shadow',
                'hover-shadow-light',
                'always-shadow-light',
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
fac.AntdSpace(
    [
        fuc.FefferyDiv(
            f'shadow="{shadow}"',
            shadow=shadow,
            style={
                'width': '220px',
                'height': '100px',
                'borderRadius': '6px',
                'border': '1px solid #f1f2f6',
                'display': 'flex',
                'justifyContent': 'center',
                'alignItems': 'center',
            },
        )
        for shadow in [
            'no-shadow',
            'hover-shadow',
            'always-shadow',
            'hover-shadow-light',
            'always-shadow-light',
        ]
    ],
    wrap=True,
)
"""
        }
    ]
