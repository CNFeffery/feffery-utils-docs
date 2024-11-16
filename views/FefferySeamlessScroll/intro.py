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
                {'title': translator.t('数据展示')},
                {'title': translator.t('FefferySeamlessScroll 无缝滚动')},
            ],
            style={'marginBottom': 8},
        ),
        fac.AntdTitle(
            translator.t('FefferySeamlessScroll 无缝滚动'),
            level=2,
        ),
        fac.AntdParagraph(translator.t('针对一组元素进行无缝滚动。')),
    ]
