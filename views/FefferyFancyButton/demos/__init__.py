from functools import partial
from dash.dependencies import Component

from . import (
    basic_usage,  # noqa: F401
    ripple,  # noqa: F401
    basic_callbacks,  # noqa: F401
)
from components import demos_render

# 国际化
from i18n import translator


def demos_config() -> list:
    t = partial(translator.t, locale_topic='FefferyFancyButton')
    return [
        {
            'path': 'basic_usage',
            'title': t('基础使用'),
            'description': '不同类型的按钮。',
        },
        {
            'path': 'ripple',
            'title': t('点击涟漪效果'),
            'description': '设置参数`ripple=True`开启点击涟漪效果。',
        },
        {
            'path': 'basic_callbacks',
            'title': t('回调监听'),
            'description': '在默认、防抖情况下分别监听按钮点击事件。',
        },
    ]


def render(component: Component, section_name: str = None) -> Component:
    """渲染当前组件演示用例"""

    return demos_render.render(
        component=component,
        demos_config=demos_config,
        section_name=section_name,
    )
