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
                {'title': translator.t('其他')},
                {'title': translator.t('FefferyShortcutPanel 快捷指令面板')},
            ],
            style={'marginBottom': 8},
        ),
        fac.AntdTitle(
            translator.t('FefferyShortcutPanel 快捷指令面板'),
            level=2,
        ),
        fac.AntdParagraph(translator.t('快捷指令面板。')),
    ]
