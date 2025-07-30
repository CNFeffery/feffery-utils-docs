from functools import partial
from dash.dependencies import Component

from . import (
    basic_usage,  # noqa: F401
    manual,  # noqa: F401
)
from components import demos_render

# 国际化
from i18n import translator


def demos_config() -> list:
    t = partial(translator.t, locale_topic='FefferyTopProgress')
    return [
        {
            'path': 'basic_usage',
            'title': t('基础使用'),
            'description': '体现正在进行中的回调计算过程。',
        },
        {
            'path': 'manual',
            'title': '手动控制',
            'description': '设置参数`manual=True`后，可开启手动控制模式，通过回调函数主动控制加载状态切换，适合配合回调函数中的`running`机制使用。',
        },
    ]


def render(component: Component, section_name: str = None) -> Component:
    """渲染当前组件演示用例"""

    return demos_render.render(
        component=component,
        demos_config=demos_config,
        section_name=section_name,
    )
