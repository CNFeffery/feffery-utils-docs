from functools import partial
from dash.dependencies import Component

from . import (
    basic_usage,  # noqa: F401
    get_current_captcha,  # noqa: F401
    update_captcha,  # noqa: F401
)
from components import demos_render

# 国际化
from i18n import translator


def demos_config() -> list:
    t = partial(translator.t, locale_topic='FefferyCaptcha')
    return [
        {
            'path': 'basic_usage',
            'title': t('基础使用'),
            'description': '对所生成图片验证码的字符数量、宽度、高度进行设置。',
        },
        {
            'path': 'get_current_captcha',
            'title': '获取当前验证码',
            'description': '通过回调函数监听`captcha`属性获取当前图片对应验证码。',
        },
        {
            'path': 'update_captcha',
            'title': '控制验证码刷新',
            'description': '每次将属性`refresh`更新为`True`都会触发验证码刷新。',
        },
    ]


def render(component: Component, section_name: str = None) -> Component:
    """渲染当前组件演示用例"""

    return demos_render.render(
        component=component,
        demos_config=demos_config,
        section_name=section_name,
    )
