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
                {'title': translator.t('FefferyExtraSpinner 额外加载动画')},
            ],
            style={'marginBottom': 8},
        ),
        fac.AntdTitle(
            translator.t('FefferyExtraSpinner 额外加载动画'),
            level=2,
        ),
        fac.AntdParagraph(translator.t('提供一系列丰富的加载动画图标。')),
    ]
