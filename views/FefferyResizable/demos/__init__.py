from functools import partial
from dash.dependencies import Component

from . import (
    basic_usage,  # noqa: F401
    bounds_parent,  # noqa: F401
    direction,  # noqa: F401
    custom_handle_style,  # noqa: F401
    limit_size,  # noqa: F401
)
from components import demos_render

# 国际化
from i18n import translator


def demos_config() -> list:
    t = partial(translator.t, locale_topic='FefferyResizable')
    return [
        {
            'path': 'basic_usage',
            'title': t('基础使用'),
            'description': '默认情况下尺寸调整组件可从8个方向上进行尺寸调整。',
        },
        {
            'path': 'bounds_parent',
            'title': '限制父容器内可调',
            'description': '设置参数`bounds="parent"`后，将会限制尺寸调整组件只能在父容器内进行调整。',
        },
        {
            'path': 'direction',
            'title': '限制可调整方向',
            'description': '通过参数`direction`限制可调整的方向。',
        },
        {
            'path': 'custom_handle_style',
            'title': '自定义拖拽控件样式',
            'description': '通过参数`handleClassNames`自定义拖拽控件样式。',
        },
        {
            'path': 'limit_size',
            'title': '限制可调范围',
            'description': '通过参数`minWidth`、`minHeight`、`maxWidth`、`maxHeight`限制可调范围。',
        },
    ]


def render(component: Component, section_name: str = None) -> Component:
    """渲染当前组件演示用例"""

    return demos_render.render(
        component=component,
        demos_config=demos_config,
        section_name=section_name,
    )
