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
                {'title': translator.t('性能优化')},
                {'title': translator.t('FefferyDebounceProp 防抖属性')},
            ],
            style={'marginBottom': 8},
        ),
        fac.AntdTitle(
            translator.t('FefferyDebounceProp 防抖属性'),
            level=2,
        ),
        fac.AntdParagraph(
            translator.t('实现针对任意目标组件属性值的防抖改造。')
        ),
    ]
