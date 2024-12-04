import feffery_antd_components as fac
import feffery_utils_components as fuc
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdSpace(
        [
            fuc.FefferyQRCode(
                value='https://fuc.feffery.tech',
                imageSettings={
                    'src': '/assets/imgs/fuc-logo.svg',
                    'width': 30,
                    'height': 30,
                },
            ),
            fuc.FefferyQRCode(
                value='https://fac.feffery.tech',
                imageSettings={
                    'src': 'https://fac.feffery.tech/assets/imgs/fac-logo.svg',
                    'width': 50,
                    'height': 50,
                },
                size=256,
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
        fuc.FefferyQRCode(
            value='https://fuc.feffery.tech',
            imageSettings={
                'src': '/assets/imgs/fuc-logo.svg',
                'width': 30,
                'height': 30,
            },
        ),
        fuc.FefferyQRCode(
            value='https://fac.feffery.tech',
            imageSettings={
                'src': 'https://fac.feffery.tech/assets/imgs/fac-logo.svg',
                'width': 50,
                'height': 50,
            },
            size=256,
        ),
    ],
    direction='vertical',
)
"""
        }
    ]
