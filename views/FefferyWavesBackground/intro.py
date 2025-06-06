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
                {'title': translator.t('动效')},
                {'title': translator.t('FefferyWavesBackground 3D-Waves背景')},
            ],
            style={'marginBottom': 8},
        ),
        fac.AntdTitle(
            translator.t('FefferyWavesBackground 3D-Waves背景'),
            level=2,
        ),
        fac.AntdParagraph(translator.t('渲染3D-Waves动画背景。')),
    ]
