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
                {'title': translator.t('FefferyRawHTML HTML字符渲染')},
            ],
            style={'marginBottom': 8},
        ),
        fac.AntdTitle(
            translator.t('FefferyRawHTML HTML字符渲染'),
            level=2,
        ),
        fac.AntdParagraph(translator.t('将HTML源码渲染为页面元素。')),
    ]
