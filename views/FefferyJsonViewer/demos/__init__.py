from functools import partial
from dash.dependencies import Component

from . import (
    basic_usage,  # noqa: F401
    theme,  # noqa: F401
    indent,  # noqa: F401
    data_update,  # noqa: F401
    root_name,  # noqa: F401
)
from components import demos_render

# 国际化
from i18n import translator


def demos_config() -> list:
    t = partial(translator.t, locale_topic='FefferyJsonViewer')
    return [
        {
            'path': 'basic_usage',
            'title': t('基础使用'),
            'description': '展示**JSON**格式的数据。',
        },
        {
            'path': 'theme',
            'title': '风格主题',
            'description': '通过参数`theme`设置使用不同的风格主题。',
        },
        {
            'path': 'indent',
            'title': '缩进大小',
            'description': '通过参数`indent`设置缩进大小。',
        },
        {
            'path': 'data_update',
            'title': '数据可更新',
            'description': '通过参数`editable`、`addible`、`deletable`控制开启对应的数据编辑更新功能。',
        },
        {
            'path': 'root_name',
            'title': '根节点显示名称',
            'description': '通过参数`rootName`设置根节点显示名称。',
        },
    ]


def render(component: Component, section_name: str = None) -> Component:
    """渲染当前组件演示用例"""

    return demos_render.render(
        component=component,
        demos_config=demos_config,
        section_name=section_name,
    )
