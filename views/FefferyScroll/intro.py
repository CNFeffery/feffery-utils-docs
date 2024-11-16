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
                {'title': translator.t('页面控制')},
                {'title': translator.t('FefferyScroll 滚动操作')},
            ],
            style={'marginBottom': 8},
        ),
        fac.AntdTitle(
            translator.t('FefferyScroll 滚动操作'),
            level=2,
        ),
        fac.AntdParagraph(translator.t('快捷实现滚动操作。')),
    ]
