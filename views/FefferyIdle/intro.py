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
                {'title': translator.t('FefferyIdle 闲置状态监听')},
            ],
            style={'marginBottom': 8},
        ),
        fac.AntdTitle(
            translator.t('FefferyIdle 闲置状态监听'),
            level=2,
        ),
        fac.AntdParagraph(translator.t('监听应用是否处于无用户操作闲置状态。')),
    ]
