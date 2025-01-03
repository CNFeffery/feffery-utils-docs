import feffery_antd_components as fac
import feffery_utils_components as fuc
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdCenter(
        fuc.FefferySliderCaptcha(
            imgSrc='/assets/imgs/components/FefferySliderCaptcha/demo.jpg',
            # 按照图片实际尺寸设定
            imgWidth=520,
            imgHeight=304,
            mode='float',
        ),
        style={'height': 400},
    )

    return demo_contents


def code_string() -> list:
    """返回当前语种对应的演示代码"""

    return [
        {
            'code': """
fac.AntdCenter(
    fuc.FefferySliderCaptcha(
        imgSrc='/assets/imgs/components/FefferySliderCaptcha/demo.jpg',
        # 按照图片实际尺寸设定
        imgWidth=520,
        imgHeight=304,
        mode='float',
    ),
    style={'height': 400},
)
"""
        }
    ]
