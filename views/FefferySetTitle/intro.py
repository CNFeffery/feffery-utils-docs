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
                {'title': translator.t('页面控制')},
                {'title': translator.t('FefferySetTitle 页面title设置')},
            ],
            style={'marginBottom': 8},
        ),
        fac.AntdTitle(
            translator.t('FefferySetTitle 页面title设置'),
            level=2,
        ),
        fac.AntdParagraph(translator.t('快捷设置页面title。')),
    ]
