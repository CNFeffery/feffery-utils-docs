from functools import partial
from dash.dependencies import Component

from . import (
    basic_usage,  # noqa: F401
    multiple_segments,  # noqa: F401
    state_animation,  # noqa: F401
    spring_animation,  # noqa: F401
    mount_effect,  # noqa: F401
    variants,  # noqa: F401
)
from components import demos_render

# 国际化
from i18n import translator


def demos_config() -> list:
    t = partial(translator.t, locale_topic='FefferyMotion')
    return [
        {
            'path': 'basic_usage',
            'title': t('基础使用'),
            'description': '**FefferyMotion**本质上是**Div**容器，既可以作为动画编排的本体，也可以充当容器对内部元素编排动画效果。',
        },
        {
            'path': 'multiple_segments',
            'title': '配置多段动画',
            'description': '配置目标样式时设置为等长度的数组，可以编排出连贯的多段动画实现循环播放效果。',
        },
        {
            'path': 'state_animation',
            'title': '使用状态动画',
            'description': '通过`whileHover`、`whileTap`、`whileInView`等参数配置状态动画。',
        },
        {
            'path': 'spring_animation',
            'title': '使用弹簧物理动画',
            'description': "通过设置参数`transition.type='spring'`可以实现更适用于部分场景更自然的物理效果。",
        },
        {
            'path': 'mount_effect',
            'title': '实现元素挂载特效',
            'description': '为指定元素配置出场动画效果。',
        },
        {
            'path': 'variants',
            'title': '使用具有别名的样式组',
            'description': '基于参数`variants`配置具有别名的样式组。',
        },
    ]


def render(component: Component, section_name: str = None) -> Component:
    """渲染当前组件演示用例"""

    return demos_render.render(
        component=component,
        demos_config=demos_config,
        section_name=section_name,
    )
