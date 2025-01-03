from functools import partial
from dash.dependencies import Component

from . import (
    basic_usage,  # noqa: F401
    basic_callback,  # noqa: F401
)
from components import demos_render

# 国际化
from i18n import translator


def demos_config() -> list:
    t = partial(translator.t, locale_topic='FefferyEventListener')
    return [
        {
            'path': 'basic_usage',
            'title': t('基础使用'),
            'description': '针对浏览器中任何指定目标的合法事件进行监听。',
        },
        {
            'path': 'basic_callback',
            'title': '回调监听',
            'description': '通过参数`handler`所定义函数的返回值，将在每次事件触发后赋值给`result`。',
        },
    ]


def render(component: Component, section_name: str = None) -> Component:
    """渲染当前组件演示用例"""

    return demos_render.render(
        component=component,
        demos_config=demos_config,
        section_name=section_name,
    )
