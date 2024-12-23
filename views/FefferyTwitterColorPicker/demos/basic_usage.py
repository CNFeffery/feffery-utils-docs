import feffery_antd_components as fac
import feffery_utils_components as fuc
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdSpace(
        [
            fuc.FefferyTwitterColorPicker(),
            fuc.FefferyTwitterColorPicker(
                colors=[
                    '#fff4ce',
                    '#797673',
                    '#fed9cc',
                    '#d83b01',
                    '#fde7e9',
                    '#a80000',
                    '#dff6dd',
                    '#107c10',
                ]
            ),
        ],
        direction='vertical',
    )

    return demo_contents


def code_string() -> list:
    """返回当前语种对应的演示代码"""

    return [
        {
            'code': """
fac.AntdSpace(
    [
        fuc.FefferyTwitterColorPicker(),
        fuc.FefferyTwitterColorPicker(
            colors=[
                '#fff4ce',
                '#797673',
                '#fed9cc',
                '#d83b01',
                '#fde7e9',
                '#a80000',
                '#dff6dd',
                '#107c10',
            ]
        ),
    ],
    direction='vertical',
)
"""
        }
    ]
