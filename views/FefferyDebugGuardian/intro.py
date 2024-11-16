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
                {'title': translator.t('安全')},
                {'title': translator.t('FefferyDebugGuardian 调试守护')},
            ],
            style={'marginBottom': 8},
        ),
        fac.AntdTitle(
            translator.t('FefferyDebugGuardian 调试守护'),
            level=2,
        ),
        fac.AntdParagraph(translator.t('提供多种策略的前端防调试功能。')),
    ]
