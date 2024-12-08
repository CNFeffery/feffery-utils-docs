from functools import partial
from dash.dependencies import Component

from . import (
    basic_usage,  # noqa: F401
    duration,  # noqa: F401
)
from components import demos_render

# 国际化
from i18n import translator


def demos_config() -> list:
    t = partial(translator.t, locale_topic='FefferyCountUp')
    return [
        {
            'path': 'basic_usage',
            'title': t('基础使用'),
            'description': '以目标数值为终点自动呈现数字变化的效果。',
        },
        {
            'path': 'duration',
            'title': '控制变化过程时长',
            'description': '通过参数`duration`控制变化过程时长。',
        },
    ]


def render(component: Component, section_name: str = None) -> Component:
    """渲染当前组件演示用例"""

    return demos_render.render(
        component=component,
        demos_config=demos_config,
        section_name=section_name,
    )
