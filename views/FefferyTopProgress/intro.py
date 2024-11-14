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
                {'title': translator.t('加载动画')},
                {'title': translator.t('FefferyTopProgress 顶端加载进度条')},
            ],
            style={'marginBottom': 8},
        ),
        fac.AntdTitle(
            translator.t('FefferyTopProgress 顶端加载进度条'),
            level=2,
        ),
        fac.AntdParagraph(translator.t('页面顶端进度条形式的加载动画。')),
    ]
