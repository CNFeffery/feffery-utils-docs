from functools import partial
from dash.dependencies import Component

from . import (
    basic_usage,  # noqa: F401
    percent,  # noqa: F401
)
from components import demos_render

# 国际化
from i18n import translator


def demos_config() -> list:
    t = partial(translator.t, locale_topic='FefferyFormatNumber')
    return [
        {
            'path': 'basic_usage',
            'title': t('基础使用'),
            'description': '针对参数`value`设定的值进行格式化显示。',
        },
        {
            'path': 'percent',
            'title': '百分数格式化',
            'description': "设置参数`type='percent'`后，可针对小数进行百分数格式化显示。",
        },
    ]


def render(component: Component, section_name: str = None) -> Component:
    """渲染当前组件演示用例"""

    return demos_render.render(
        component=component,
        demos_config=demos_config,
        section_name=section_name,
    )
