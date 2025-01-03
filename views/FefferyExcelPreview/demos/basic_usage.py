import feffery_utils_components as fuc
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fuc.FefferyExcelPreview(
        src='/assets/other/components/FefferyExcelPreview/test.xlsx',
        style={'height': 600},
    )

    return demo_contents


def code_string() -> list:
    """返回当前语种对应的演示代码"""

    return [
        {
            'code': """
fuc.FefferyExcelPreview(
    src='/assets/other/components/FefferyExcelPreview/test.xlsx',
    style={'height': 600},
)
"""
        }
    ]
