import feffery_antd_components as fac
import feffery_utils_components as fuc
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fuc.FefferyScrollbars(
        [
            fac.AntdParagraph(
                '请将鼠标移入本区域进行滚动' * 5, style={'whiteSpace': 'pre'}
            )
        ]
        * 5,
        style={
            'maxHeight': '150px',
            'maxWidth': '200px',
            'border': '1px dashed #e1dfdd',
        },
    )

    return demo_contents


def code_string() -> list:
    """返回当前语种对应的演示代码"""

    return [
        {
            'code': """
fuc.FefferyScrollbars(
    [
        fac.AntdParagraph(
            '请将鼠标移入本区域进行滚动' * 5, style={'whiteSpace': 'pre'}
        )
    ]
    * 5,
    style={
        'maxHeight': '150px',
        'maxWidth': '200px',
        'border': '1px dashed #e1dfdd',
    },
)
"""
        }
    ]
