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
                {'title': translator.t('FefferyFullscreen 全屏化')},
            ],
            style={'marginBottom': 8},
        ),
        fac.AntdTitle(
            translator.t('FefferyFullscreen 全屏化'),
            level=2,
        ),
        fac.AntdParagraph(translator.t('控制指定目标元素的全屏化。')),
    ]
