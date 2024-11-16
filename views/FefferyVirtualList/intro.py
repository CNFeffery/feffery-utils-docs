import feffery_antd_components as fac
from dash.dependencies import Component

# 国际化
from i18n import translator


def render() -> Component:
    """渲染组件介绍内容"""
    return [
        fac.AntdBreadcrumb(
            items=[
                {'title': translator.t('组件介绍')},
                {'title': translator.t('性能优化')},
                {'title': translator.t('FefferyVirtualList 虚拟滚动')},
            ],
            style={'marginBottom': 8},
        ),
        fac.AntdTitle(
            translator.t('FefferyVirtualList 虚拟滚动'),
            level=2,
        ),
        fac.AntdParagraph(
            translator.t('基于虚拟滚动实现对众多元素的高性能渲染。')
        ),
    ]
