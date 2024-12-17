from functools import partial
from dash.dependencies import Component

from . import (
    basic_usage,  # noqa: F401
    target,  # noqa: F401
)
from components import demos_render

# 国际化
from i18n import translator


def demos_config() -> list:
    t = partial(translator.t, locale_topic='FefferyListenScroll')
    return [
        {
            'path': 'basic_usage',
            'title': t('基础使用'),
            'description': '默认可监听页面整体滚动位置。',
        },
        {
            'path': 'target',
            'title': '指定目标容器',
            'description': '通过参数`target`指定目标监听容器的id。',
        },
    ]


def render(component: Component, section_name: str = None) -> Component:
    """渲染当前组件演示用例"""

    return demos_render.render(
        component=component,
        demos_config=demos_config,
        section_name=section_name,
    )
