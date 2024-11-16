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
                {'title': translator.t('反馈')},
                {'title': translator.t('FefferyFancyMessage 美观消息提示')},
            ],
            style={'marginBottom': 8},
        ),
        fac.AntdTitle(
            translator.t('FefferyFancyMessage 美观消息提示'),
            level=2,
        ),
        fac.AntdParagraph(translator.t('渲染美观的消息提示。')),
    ]
