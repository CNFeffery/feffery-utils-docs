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
                {'title': translator.t('样式控制')},
                {'title': translator.t('FefferyStyle 动态样式')},
            ],
            style={'marginBottom': 8},
        ),
        fac.AntdTitle(
            translator.t('FefferyStyle 动态样式'),
            level=2,
        ),
        fac.AntdParagraph(translator.t('动态注入CSS样式规则片段并生效。')),
    ]
