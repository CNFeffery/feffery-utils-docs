from functools import partial
from dash.dependencies import Component

from . import (
    basic_usage,  # noqa: F401
    basic_callback,  # noqa: F401
)
from components import demos_render

# 国际化
from i18n import translator


def demos_config() -> list:
    t = partial(translator.t, locale_topic='FefferyBlockColorPicker')
    return [
        {
            'path': 'basic_usage',
            'title': t('基础使用'),
            'description': '供用户在给定的一系列颜色中进行选择。',
        },
        {
            'path': 'basic_callback',
            'title': '回调监听',
            'description': '监听`color`变化获取当前选中颜色。',
        },
    ]


def render(component: Component, section_name: str = None) -> Component:
    """渲染当前组件演示用例"""

    return demos_render.render(
        component=component,
        demos_config=demos_config,
        section_name=section_name,
    )
