from functools import partial
from dash.dependencies import Component

from . import (
    basic_usage,  # noqa: F401
    levels,  # noqa: F401
    with_image,  # noqa: F401
    renderer,  # noqa: F401
)
from components import demos_render

# 国际化
from i18n import translator


def demos_config() -> list:
    t = partial(translator.t, locale_topic='FefferyQRCode')
    return [
        {
            'path': 'basic_usage',
            'title': t('基础使用'),
            'description': '渲染具有指定信息的二维码。',
        },
        {
            'path': 'levels',
            'title': '精确水平',
            'description': '通过参数`level`控制二维码的精确水平。',
        },
        {
            'path': 'with_image',
            'title': '内嵌图片',
            'description': '通过参数`imageSettings`配置内嵌图片。',
        },
        {
            'path': 'renderer',
            'title': '渲染模式',
            'description': '通过参数`renderer`控制渲染模式。',
        },
    ]


def render(component: Component, section_name: str = None) -> Component:
    """渲染当前组件演示用例"""

    return demos_render.render(
        component=component,
        demos_config=demos_config,
        section_name=section_name,
    )
