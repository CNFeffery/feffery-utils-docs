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
                {'title': translator.t('容器')},
                {'title': translator.t('FefferyHighlightWords 关键词高亮')},
            ],
            style={'marginBottom': 8},
        ),
        fac.AntdTitle(
            translator.t('FefferyHighlightWords 关键词高亮'),
            level=2,
        ),
        fac.AntdParagraph(
            translator.t('针对一段内容中的指定关键词进行高亮展示。')
        ),
    ]
