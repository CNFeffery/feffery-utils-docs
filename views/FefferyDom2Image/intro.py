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
                {'title': translator.t('FefferyDom2Image 元素转图片')},
            ],
            style={'marginBottom': 8},
        ),
        fac.AntdTitle(
            translator.t('FefferyDom2Image 元素转图片'),
            level=2,
        ),
        fac.AntdParagraph(translator.t('将目标元素转成任意精度的图片数据。')),
    ]
