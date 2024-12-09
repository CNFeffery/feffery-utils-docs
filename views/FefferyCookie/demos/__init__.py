from functools import partial
from dash.dependencies import Component

from . import (
    basic_usage,  # noqa: F401
    dynamic_update,  # noqa: F401
)
from components import demos_render

# 国际化
from i18n import translator


def demos_config() -> list:
    t = partial(translator.t, locale_topic='FefferyCookie')
    return [
        {
            'path': 'basic_usage',
            'title': t('基础使用'),
            'description': '若当前指定的**cookie**键值对在浏览器中原先不存在，则可以通过设置`defaultValue`参数实现对应cookie值的初始化。',
        },
        {
            'path': 'dynamic_update',
            'title': '动态更新cookie值',
            'description': '动态更新**cookie**值，并配合**flask**在回调函数中获取最新的**cookie**值。',
        },
    ]


def render(component: Component, section_name: str = None) -> Component:
    """渲染当前组件演示用例"""

    return demos_render.render(
        component=component,
        demos_config=demos_config,
        section_name=section_name,
    )
