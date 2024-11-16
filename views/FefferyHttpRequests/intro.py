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
                {'title': translator.t('通信')},
                {'title': translator.t('FefferyHttpRequests http请求')},
            ],
            style={'marginBottom': 8},
        ),
        fac.AntdTitle(
            translator.t('FefferyHttpRequests http请求'),
            level=2,
        ),
        fac.AntdParagraph(
            translator.t('在浏览器端发起http请求并获取响应数据。')
        ),
    ]
