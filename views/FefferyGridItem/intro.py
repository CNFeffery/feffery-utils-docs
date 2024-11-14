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
                {'title': translator.t('拖拽交互')},
                {'title': translator.t('FefferyGridItem 可拖拽网格项')},
            ],
            style={'marginBottom': 8},
        ),
        fac.AntdTitle(
            translator.t('FefferyGridItem 可拖拽网格项'),
            level=2,
        ),
        fac.AntdParagraph(translator.t('在“可拖拽网格”功能中充当网格子项。')),
    ]
