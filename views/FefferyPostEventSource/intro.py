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
                {
                    'title': translator.t(
                        'FefferyPostEventSource POST请求EventSource通信'
                    )
                },
            ],
            style={'marginBottom': 8},
        ),
        fac.AntdTitle(
            translator.t('FefferyPostEventSource POST请求EventSource通信'),
            level=2,
        ),
        fac.AntdParagraph(
            translator.t(
                '处理与POST请求类型SSE（Server Sent Events）服务的通信。'
            )
        ),
    ]
