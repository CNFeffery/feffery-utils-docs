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
                {'title': translator.t('图片')},
                {'title': translator.t('FefferyAnimatedImage 动图')},
            ],
            style={'marginBottom': 8},
        ),
        fac.AntdTitle(
            translator.t('FefferyAnimatedImage 动图'),
            level=2,
        ),
        fac.AntdParagraph(translator.t('交互式的动图展示功能。')),
    ]
