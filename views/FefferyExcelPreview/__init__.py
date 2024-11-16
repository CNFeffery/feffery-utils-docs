import feffery_utils_components as fuc
from dash.dependencies import Component

from . import intro, demos
from components import doc_layout


def render() -> Component:
    return doc_layout.render(
        component=fuc.FefferyExcelPreview,
        intro=intro.render(),
        demos=demos.render(component=fuc.FefferyExcelPreview),
        catalog=demos.demos_config,
    )
