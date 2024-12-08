from functools import partial
from dash.dependencies import Component

from . import (
    basic_usage,  # noqa: F401
    use_with_antd_spin,  # noqa: F401
)
from components import demos_render

# 国际化
from i18n import translator


def demos_config() -> list:
    t = partial(translator.t, locale_topic='FefferyExtraSpinner')
    return [
        {
            'path': 'basic_usage',
            'title': t('基础使用'),
            'description': '可用的全部内置加载动画。',
        },
        {
            'path': 'use_with_antd_spin',
            'title': '配合fac.AntdSpin使用',
            'description': '充当[fac.AntdSpin](https://fac.feffery.tech/AntdSpin)的加载动画使用。',
        },
    ]


def render(component: Component, section_name: str = None) -> Component:
    """渲染当前组件演示用例"""

    return demos_render.render(
        component=component,
        demos_config=demos_config,
        section_name=section_name,
    )
