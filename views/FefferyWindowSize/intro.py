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
                {'title': translator.t('事件监听')},
                {'title': translator.t('FefferyWindowSize 浏览器窗口尺寸监听')},
            ],
            style={'marginBottom': 8},
        ),
        fac.AntdTitle(
            translator.t('FefferyWindowSize 浏览器窗口尺寸监听'),
            level=2,
        ),
        fac.AntdParagraph(translator.t('针对浏览器窗口尺寸变化事件进行监听。')),
    ]