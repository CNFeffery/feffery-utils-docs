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
                {'title': translator.t('静态资源控制')},
                {
                    'title': translator.t(
                        'FefferyExternalCss 外部css资源动态注入'
                    )
                },
            ],
            style={'marginBottom': 8},
        ),
        fac.AntdTitle(
            translator.t('FefferyExternalCss 外部css资源动态注入'),
            level=2,
        ),
        fac.AntdParagraph(translator.t('动态控制注入外部css资源。')),
    ]
