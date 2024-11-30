from functools import partial
from dash.dependencies import Component

from . import (
    basic_usage,  # noqa: F401
    remote_search,  # noqa: F401
)
from components import demos_render

# 国际化
from i18n import translator


def demos_config() -> list:
    t = partial(translator.t, locale_topic='FefferyShortcutPanel')
    return [
        {
            'path': 'basic_usage',
            'title': t('基础使用'),
            'description': '构建可通过指定快捷键组合唤出的指令选择面板。',
        },
        {
            'path': 'remote_search',
            'title': '远程搜索',
            'description': '配合回调函数实现远程搜索功能。',
        },
    ]


def render(component: Component, section_name: str = None) -> Component:
    """渲染当前组件演示用例"""

    return demos_render.render(
        component=component,
        demos_config=demos_config,
        section_name=section_name,
    )
