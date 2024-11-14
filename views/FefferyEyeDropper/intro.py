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
                {'title': translator.t('颜色选择')},
                {'title': translator.t('FefferyEyeDropper 色彩拾取')},
            ],
            style={'marginBottom': 8},
        ),
        fac.AntdTitle(translator.t('FefferyEyeDropper 色彩拾取'), level=2),
        fac.AntdParagraph(translator.t('通过色彩拾取的方式进行颜色选择。')),
    ]
