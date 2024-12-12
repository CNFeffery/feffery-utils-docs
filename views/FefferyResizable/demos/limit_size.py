import feffery_antd_components as fac
import feffery_utils_components as fuc
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fuc.FefferyResizable(
        fac.AntdCenter(
            '示例内容',
            style={
                'height': '100%',
                'background': '#dee2e6',
            },
        ),
        defaultSize={'width': 200, 'height': 200},
        minWidth=100,
        minHeight=100,
        maxWidth=400,
        maxHeight=400,
    )

    return demo_contents


def code_string() -> list:
    """返回当前语种对应的演示代码"""

    return [
        {
            'code': """
fuc.FefferyResizable(
    fac.AntdCenter(
        '示例内容',
        style={
            'height': '100%',
            'background': '#dee2e6',
        },
    ),
    defaultSize={'width': 200, 'height': 200},
    minWidth=100,
    minHeight=100,
    maxWidth=400,
    maxHeight=400,
)
"""
        }
    ]
