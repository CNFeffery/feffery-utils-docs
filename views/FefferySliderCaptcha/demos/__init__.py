from functools import partial
from dash.dependencies import Component

from . import (
    basic_usage,  # noqa: F401
    float_mode,  # noqa: F401
    basic_callback,  # noqa: F401
)
from components import demos_render

# 国际化
from i18n import translator


def demos_config() -> list:
    t = partial(translator.t, locale_topic='FefferySliderCaptcha')
    return [
        {
            'path': 'basic_usage',
            'title': t('基础使用'),
            'description': '基于设定的图片及尺寸，自动生成滑块验证码。',
        },
        {
            'path': 'float_mode',
            'title': 'float模式',
            'description': "设置参数`mode='float'`后开启浮动显示模式。",
        },
        {
            'path': 'basic_callback',
            'title': '回调监听',
            'description': '通过回调监听`verifyResult`属性变化获取最新的滑块验证结果。',
        },
    ]


def render(component: Component, section_name: str = None) -> Component:
    """渲染当前组件演示用例"""

    return demos_render.render(
        component=component,
        demos_config=demos_config,
        section_name=section_name,
    )
