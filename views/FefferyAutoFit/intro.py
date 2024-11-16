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
                {'title': translator.t('尺寸调整')},
                {'title': translator.t('FefferyAutoFit 自适应')},
            ],
            style={'marginBottom': 8},
        ),
        fac.AntdTitle(
            translator.t('FefferyAutoFit 自适应'),
            level=2,
        ),
        fac.AntdParagraph(translator.t('为页面整体添加屏幕自适应功能。')),
    ]
