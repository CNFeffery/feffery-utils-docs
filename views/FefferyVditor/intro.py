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
                {'title': translator.t('编辑器')},
                {
                    'title': translator.t(
                        'FefferyVditor 类Typora的markdown编辑器'
                    )
                },
            ],
            style={'marginBottom': 8},
        ),
        fac.AntdTitle(
            translator.t('FefferyVditor 类Typora的markdown编辑器'),
            level=2,
        ),
        fac.AntdParagraph(translator.t('类似Typora操作风格的markdown编辑器。')),
    ]
