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
                {'title': translator.t('图片')},
                {
                    'title': translator.t(
                        'FefferyPhotoSphereViewer 全景图片查看器'
                    )
                },
            ],
            style={'marginBottom': 8},
        ),
        fac.AntdTitle(
            translator.t('FefferyPhotoSphereViewer 全景图片查看器'),
            level=2,
        ),
        fac.AntdParagraph(translator.t('功能丰富的全景图片查看器。')),
    ]
