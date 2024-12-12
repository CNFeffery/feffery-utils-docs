from functools import partial
import feffery_antd_components as fac
from dash.dependencies import Component

from utils.doc_renderer import MarkdownRenderer

# 国际化
from i18n import translator

markdown_renderer = MarkdownRenderer()


def render(component: Component, section_name: str = None) -> Component:
    """渲染当前组件演示用例"""
    t = partial(translator.t, locale_topic='FefferyGridItem')
    return fac.AntdParagraph(
        markdown_renderer.render(
            t(
                '注：**FefferyGridItem**使用需配合**FefferyGrid**，请前往[FefferyGrid文档页](/FefferyGrid)查看具体使用示例。'
            )
        ),
        style={'paddingBottom': 'calc(100vh - 550px)'},
    )
