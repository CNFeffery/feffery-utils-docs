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
                {'title': translator.t('编辑器')},
                {'title': translator.t('FefferyRichTextEditor 富文本编辑器')},
            ],
            style={'marginBottom': 8},
        ),
        fac.AntdTitle(
            translator.t('FefferyRichTextEditor 富文本编辑器'),
            level=2,
        ),
        fac.AntdParagraph(translator.t('具有丰富功能的富文本编辑器。')),
    ]
