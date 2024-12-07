from functools import partial
from dash.dependencies import Component

from . import (
    basic_usage,  # noqa: F401
)
from components import demos_render

# 国际化
from i18n import translator


def demos_config() -> list:
    t = partial(translator.t, locale_topic='FefferyImagePaste')
    return [
        {
            'path': 'basic_usage',
            'title': t('基础使用'),
            'description': '配合[FefferyDiv](/FefferyDiv)的鼠标悬停监听功能，实现鼠标在指定容器内时才启用图片粘贴捕获功能。',
        },
    ]


def render(component: Component, section_name: str = None) -> Component:
    """渲染当前组件演示用例"""

    return demos_render.render(
        component=component,
        demos_config=demos_config,
        section_name=section_name,
    )
