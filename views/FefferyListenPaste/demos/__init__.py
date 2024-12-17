from functools import partial
from dash.dependencies import Component

from . import (
    basic_usage,  # noqa: F401
    target_container,  # noqa: F401
)
from components import demos_render

# 国际化
from i18n import translator


def demos_config() -> list:
    t = partial(translator.t, locale_topic='FefferyListenPaste')
    return [
        {
            'path': 'basic_usage',
            'title': t('基础使用'),
            'description': '设置参数`enableListenPaste=True`后，用户在当前页面任何位置进行的文本粘贴行为都会被捕获到。',
        },
        {
            'path': 'target_container',
            'title': '绑定指定容器',
            'description': '通过设置参数`targetContainerId`可限制仅监听目标容器内的粘贴事件。',
        },
    ]


def render(component: Component, section_name: str = None) -> Component:
    """渲染当前组件演示用例"""

    return demos_render.render(
        component=component,
        demos_config=demos_config,
        section_name=section_name,
    )
