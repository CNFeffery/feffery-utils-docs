import feffery_antd_components as fac
import feffery_utils_components as fuc
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdSpace(
        [
            fuc.FefferyCountUp(end=99999, duration=5),
            fuc.FefferyCountUp(end=-99999, duration=5),
        ],
        style={'fontSize': 18},
    )

    return demo_contents


def code_string() -> list:
    """返回当前语种对应的演示代码"""

    return [
        {
            'code': """
fac.AntdSpace(
    [
        fuc.FefferyCountUp(end=99999, duration=5),
        fuc.FefferyCountUp(end=-99999, duration=5),
    ],
    style={'fontSize': 18},
)
"""
        }
    ]
