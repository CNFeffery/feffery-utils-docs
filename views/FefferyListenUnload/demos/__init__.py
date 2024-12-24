from functools import partial
from dash.dependencies import Component

from . import (
    basic_usage,  # noqa: F401
)
from components import demos_render

# 国际化
from i18n import translator


def demos_config() -> list:
    t = partial(translator.t, locale_topic='FefferyListenUnload')
    return [
        {
            'path': 'basic_usage',
            'title': t('基础使用'),
            'description': '对标签页刷新/关闭、浏览器关闭行为进行监听，通常用于接受应用销毁信号辅助清理缓存等操作。',
        },
    ]


def render(component: Component, section_name: str = None) -> Component:
    """渲染当前组件演示用例"""

    return demos_render.render(
        component=component,
        demos_config=demos_config,
        section_name=section_name,
    )
