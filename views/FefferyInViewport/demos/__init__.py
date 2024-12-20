from functools import partial
from dash.dependencies import Component

from . import (
    basic_usage,  # noqa: F401
    threshold,  # noqa: F401
)
from components import demos_render

# 国际化
from i18n import translator


def demos_config() -> list:
    t = partial(translator.t, locale_topic='FefferyInViewport')
    return [
        {
            'path': 'basic_usage',
            'title': t('基础使用'),
            'description': '监听目标元素是否出现在视口中。',
        },
        {
            'path': 'threshold',
            'title': '设置显示比例阈值',
            'description': '通过参数`threshold`设置满足出现状态的显示比例阈值。',
        },
    ]


def render(component: Component, section_name: str = None) -> Component:
    """渲染当前组件演示用例"""

    return demos_render.render(
        component=component,
        demos_config=demos_config,
        section_name=section_name,
    )
