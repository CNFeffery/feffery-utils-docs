from functools import partial
from dash.dependencies import Component

from . import (
    basic_usage,  # noqa: F401
    types,  # noqa: F401
    size,  # noqa: F401
    color,  # noqa: F401
    basic_callback,  # noqa: F401
)
from components import demos_render

# 国际化
from i18n import translator


def demos_config() -> list:
    t = partial(translator.t, locale_topic='FefferyBurger')
    return [
        {
            'path': 'basic_usage',
            'title': t('基础使用'),
            'description': t('点击图标进行状态切换。'),
        },
        {
            'path': 'types',
            'title': '图标类型',
            'description': '通过参数`type`切换不同的图标类型。',
        },
        {
            'path': 'size',
            'title': '图标尺寸',
            'description': '通过参数`size`控制图标尺寸。',
        },
        {
            'path': 'color',
            'title': '图标颜色',
            'description': '通过参数`color`控制图标颜色。',
        },
        {
            'path': 'basic_callback',
            'title': '回调监听',
            'description': '通过参数`toggled`监听图标切换状态。',
        },
    ]


def render(component: Component, section_name: str = None) -> Component:
    """渲染当前组件演示用例"""

    return demos_render.render(
        component=component,
        demos_config=demos_config,
        section_name=section_name,
    )
