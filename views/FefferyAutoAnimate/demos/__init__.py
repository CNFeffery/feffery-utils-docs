from functools import partial
from dash.dependencies import Component

from . import (
    basic_usage,  # noqa: F401
)
from components import demos_render

# 国际化
from i18n import translator


def demos_config() -> list:
    t = partial(translator.t, locale_topic='FefferyAutoAnimate')
    return [
        {
            'path': 'basic_usage',
            'title': t('基础使用'),
            'description': '**FefferyAutoAnimate**可视作常规的容器使用，其内部的有唯一`id`或`key`定义的子元素，在发生新增、删除、顺序变化等操作时会自动渲染动画效果。',
        },
    ]


def render(component: Component, section_name: str = None) -> Component:
    """渲染当前组件演示用例"""

    return demos_render.render(
        component=component,
        demos_config=demos_config,
        section_name=section_name,
    )
