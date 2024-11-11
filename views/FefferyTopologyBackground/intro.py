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
                {
                    'title': translator.t(
                        'FefferyTopologyBackground 3D-Topology背景'
                    )
                },
            ],
            style={'marginBottom': 8},
        ),
        fac.AntdTitle(
            translator.t('FefferyTopologyBackground 3D-Topology背景'),
            level=2,
        ),
        fac.AntdParagraph(translator.t('渲染3D-Topology动画背景。')),
    ]