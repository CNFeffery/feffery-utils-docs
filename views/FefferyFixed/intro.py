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
                {'title': translator.t('容器')},
                {'title': translator.t('FefferyFixed 固定布局')},
            ],
            style={'marginBottom': 8},
        ),
        fac.AntdTitle(
            translator.t('FefferyFixed 固定布局'),
            level=2,
        ),
        fac.AntdParagraph(translator.t('实现相对页面的元素快捷固定效果。')),
    ]