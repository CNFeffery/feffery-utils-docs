from functools import partial
from dash.dependencies import Component

from . import (
    basic_usage,  # noqa: F401
)
from components import demos_render

# 国际化
from i18n import translator


def demos_config() -> list:
    t = partial(translator.t, locale_topic='FefferyIdle')
    return [
        {
            'path': 'basic_usage',
            'title': t('基础使用'),
            'description': '本例中，若超过`3`秒没有任何用户操作，则`isIdle`会更新为`True`，直到继续有交互操作发生。',
        },
    ]


def render(component: Component, section_name: str = None) -> Component:
    """渲染当前组件演示用例"""

    return demos_render.render(
        component=component,
        demos_config=demos_config,
        section_name=section_name,
    )
