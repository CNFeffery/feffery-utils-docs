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
                {'title': translator.t('文件预览')},
                {'title': translator.t('FefferyWordPreview word文件预览')},
            ],
            style={'marginBottom': 8},
        ),
        fac.AntdTitle(
            translator.t('FefferyWordPreview word文件预览'),
            level=2,
        ),
        fac.AntdParagraph(translator.t('预览word文件。')),
    ]
