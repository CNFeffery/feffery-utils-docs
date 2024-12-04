from functools import partial
from dash.dependencies import Component

from . import (
    basic_usage,  # noqa: F401
    basic_callbacks,  # noqa: F401
)
from components import demos_render

# 国际化
from i18n import translator


def demos_config() -> list:
    t = partial(translator.t, locale_topic='FefferyLazyLoad')
    return [
        {
            'path': 'basic_usage',
            'title': t('基础使用'),
            'description': '包裹在懒加载容器内的子元素在达到出现判定条件之前不会渲染到页面中。',
        },
        {
            'path': 'basic_callbacks',
            'title': '回调监听',
            'description': '通过监听懒加载容器出现与否进行可控的内容加载。',
        },
    ]


def render(component: Component, section_name: str = None) -> Component:
    """渲染当前组件演示用例"""

    return demos_render.render(
        component=component,
        demos_config=demos_config,
        section_name=section_name,
    )
