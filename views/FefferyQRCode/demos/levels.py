import feffery_antd_components as fac
import feffery_utils_components as fuc
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdSpace(
        [
            fac.AntdDivider('默认level="L"', innerTextOrientation='left'),
            fuc.FefferyQRCode(value='FefferyQRCode示例'),
            fac.AntdDivider('level="M"', innerTextOrientation='left'),
            fuc.FefferyQRCode(value='FefferyQRCode示例', level='M'),
            fac.AntdDivider('level="Q"', innerTextOrientation='left'),
            fuc.FefferyQRCode(value='FefferyQRCode示例', level='Q'),
            fac.AntdDivider('level="H"', innerTextOrientation='left'),
            fuc.FefferyQRCode(value='FefferyQRCode示例', level='H'),
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
        fac.AntdDivider('默认level="L"', innerTextOrientation='left'),
        fuc.FefferyQRCode(value='FefferyQRCode示例'),
        fac.AntdDivider('level="M"', innerTextOrientation='left'),
        fuc.FefferyQRCode(value='FefferyQRCode示例', level='M'),
        fac.AntdDivider('level="Q"', innerTextOrientation='left'),
        fuc.FefferyQRCode(value='FefferyQRCode示例', level='Q'),
        fac.AntdDivider('level="H"', innerTextOrientation='left'),
        fuc.FefferyQRCode(value='FefferyQRCode示例', level='H'),
    ],
    direction='vertical',
    style={'width': '100%'},
)
"""
        }
    ]
