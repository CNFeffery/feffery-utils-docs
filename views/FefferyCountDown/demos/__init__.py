from functools import partial
from dash.dependencies import Component

from . import (
    basic_usage,  # noqa: F401
    classic_usage,  # noqa: F401
)
from components import demos_render

# 国际化
from i18n import translator


def demos_config() -> list:
    t = partial(translator.t, locale_topic='FefferyCountDown')
    return [
        {
            'path': 'basic_usage',
            'title': t('基础使用'),
            'description': '每次有效的`delay`被设置后，且目标倒计时组件没有正在进行中的倒计时过程时，都会启动新的倒计时过程。',
        },
        {
            'path': 'classic_usage',
            'title': '经典使用场景',
            'description': '这里展示了基于倒计时组件的经典使用场景。',
        },
    ]


def render(component: Component, section_name: str = None) -> Component:
    """渲染当前组件演示用例"""

    return demos_render.render(
        component=component,
        demos_config=demos_config,
        section_name=section_name,
    )
