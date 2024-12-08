from functools import partial
from dash.dependencies import Component

from . import (
    basic_usage,  # noqa: F401
)
from components import demos_render

# 国际化
from i18n import translator


def demos_config() -> list:
    t = partial(translator.t, locale_topic='FefferyExternalCss')
    return [
        {
            'path': 'basic_usage',
            'title': t('基础使用'),
            'description': '通过观察浏览器开发者工具-网络可以更清楚地了解到上述回调过程运作原理。',
        },
    ]


def render(component: Component, section_name: str = None) -> Component:
    """渲染当前组件演示用例"""

    return demos_render.render(
        component=component,
        demos_config=demos_config,
        section_name=section_name,
    )
