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
                {'title': translator.t('存储')},
                {
                    'title': translator.t(
                        'FefferyLocalLargeStorage 客户端大容量存储器'
                    )
                },
            ],
            style={'marginBottom': 8},
        ),
        fac.AntdTitle(
            translator.t('FefferyLocalLargeStorage 客户端大容量存储器'),
            level=2,
        ),
        fac.AntdParagraph(translator.t('在用户浏览器本地缓存大量数据。')),
    ]
