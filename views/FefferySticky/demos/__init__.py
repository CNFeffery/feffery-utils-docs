from functools import partial
from dash.dependencies import Component

from . import (
    basic_usage,  # noqa: F401
    with_target,  # noqa: F401
)
from components import demos_render

# 国际化
from i18n import translator


def demos_config() -> list:
    t = partial(translator.t, locale_topic='FefferySticky')
    return [
        {
            'path': 'basic_usage',
            'title': t('基础使用'),
            'description': '在这个例子中，示例元素受参数`top`设置的影响，在距离页面顶端100px时进入粘性状态，随着继续下滑，在参数`bottomBoundary`设置的影响下，距离文档顶端绝对距离超出800px时随之解除粘性状态。',
        },
        {
            'path': 'with_target',
            'title': '滚动目标元素',
            'description': '通过向`top`或`bottomBoundary`参数传入css选择器规则，配合`zIndex`参数以实现更为灵活的页面布局效果。',
        },
    ]


def render(component: Component, section_name: str = None) -> Component:
    """渲染当前组件演示用例"""

    return demos_render.render(
        component=component,
        demos_config=demos_config,
        section_name=section_name,
    )
