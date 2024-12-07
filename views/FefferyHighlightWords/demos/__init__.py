from functools import partial
from dash.dependencies import Component

from . import (
    basic_usage,  # noqa: F401
    regex,  # noqa: F401
    custom_style,  # noqa: F401
)
from components import demos_render

# 国际化
from i18n import translator


def demos_config() -> list:
    t = partial(translator.t, locale_topic='FefferyHighlightWords')
    return [
        {
            'path': 'basic_usage',
            'title': t('基础使用'),
            'description': '通过参数`searchWords`设置要高亮的若干关键词。',
        },
        {
            'path': 'regex',
            'title': '使用正则表达式',
            'description': '设置`useRegex=True`后，`searchWords`中的关键词将被视作正则表达式。',
        },
        {
            'path': 'custom_style',
            'title': '自定义高亮、非高亮部分样式',
            'description': '通过参数`highlightStyle`、`unhighlightStyle`分别设置高亮、非高亮部分的样式。',
        },
    ]


def render(component: Component, section_name: str = None) -> Component:
    """渲染当前组件演示用例"""

    return demos_render.render(
        component=component,
        demos_config=demos_config,
        section_name=section_name,
    )
