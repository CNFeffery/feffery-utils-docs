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
                {'title': translator.t('拖拽交互')},
                {'title': translator.t('FefferyRND 尺寸可调可拖拽')},
            ],
            style={'marginBottom': 8},
        ),
        fac.AntdTitle(
            translator.t('FefferyRND 尺寸可调可拖拽'),
            level=2,
        ),
        fac.AntdParagraph(translator.t('实现尺寸可调+可拖拽功能。')),
    ]
