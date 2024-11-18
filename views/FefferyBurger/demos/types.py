import feffery_antd_components as fac
import feffery_utils_components as fuc
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdSpace(
        [
            fac.AntdSpace(
                [fuc.FefferyBurger(type=t), fac.AntdText(t, copyable=True)],
                direction='vertical',
            )
            for t in [
                'default',
                'squash',
                'cross',
                'twirl',
                'fade',
                'slant',
                'spiral',
                'divide',
                'turn',
                'pivot',
                'sling',
                'squeeze',
                'spin',
                'rotate',
            ]
        ],
        wrap=True,
        size='large',
    )

    return demo_contents


def code_string() -> list:
    """返回当前语种对应的演示代码"""

    return [
        {
            'code': """
fac.AntdSpace(
    [
        fac.AntdSpace(
            [fuc.FefferyBurger(type=t), fac.AntdText(t, copyable=True)],
            direction='vertical',
        )
        for t in [
            'default',
            'squash',
            'cross',
            'twirl',
            'fade',
            'slant',
            'spiral',
            'divide',
            'turn',
            'pivot',
            'sling',
            'squeeze',
            'spin',
            'rotate',
        ]
    ],
    wrap=True,
    size='large',
)
"""
        }
    ]
