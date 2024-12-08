import feffery_antd_components as fac
import feffery_utils_components as fuc
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = [
        fac.AntdDivider(
            'scrollbar="default"（默认）', innerTextOrientation='left'
        ),
        fuc.FefferyDiv(
            '测试' * 100,
            style={'width': '200px', 'maxHeight': '100px', 'overflowY': 'auto'},
        ),
        fac.AntdDivider('scrollbar="simple"', innerTextOrientation='left'),
        fuc.FefferyDiv(
            '测试' * 100,
            scrollbar='simple',
            style={'width': '200px', 'maxHeight': '100px', 'overflowY': 'auto'},
        ),
        fac.AntdDivider('scrollbar="hidden"', innerTextOrientation='left'),
        fuc.FefferyDiv(
            '测试' * 100,
            scrollbar='hidden',
            style={'width': '200px', 'maxHeight': '100px', 'overflowY': 'auto'},
        ),
    ]

    return demo_contents


def code_string() -> list:
    """返回当前语种对应的演示代码"""

    return [
        {
            'code': """
[
    fac.AntdDivider(
        'scrollbar="default"（默认）', innerTextOrientation='left'
    ),
    fuc.FefferyDiv(
        '测试' * 100,
        style={'width': '200px', 'maxHeight': '100px', 'overflowY': 'auto'},
    ),
    fac.AntdDivider('scrollbar="simple"', innerTextOrientation='left'),
    fuc.FefferyDiv(
        '测试' * 100,
        scrollbar='simple',
        style={'width': '200px', 'maxHeight': '100px', 'overflowY': 'auto'},
    ),
    fac.AntdDivider('scrollbar="hidden"', innerTextOrientation='left'),
    fuc.FefferyDiv(
        '测试' * 100,
        scrollbar='hidden',
        style={'width': '200px', 'maxHeight': '100px', 'overflowY': 'auto'},
    ),
]
"""
        }
    ]
