from functools import partial
from dash.dependencies import Component

from . import (
    listen_size,  # noqa: F401
    listen_mouse_enter_leave,  # noqa: F401
    listen_click,  # noqa: F401
    listen_context_menu,  # noqa: F401
    listen_is_hovering,  # noqa: F401
    listen_click_away,  # noqa: F401
    shadow,  # noqa: F401
    scrollbar,  # noqa: F401
)
from components import demos_render

# 国际化
from i18n import translator


def demos_config() -> list:
    t = partial(translator.t, locale_topic='FefferyDiv')  # noqa: F841
    return [
        {
            'path': 'listen_size',
            'title': '监听自身尺寸',
            'description': '通过参数`enableEvents`启用尺寸监听功能后，可通过回调函数监听`_width`、`_height`变化。',
        },
        {
            'path': 'listen_mouse_enter_leave',
            'title': '监听鼠标移入移出',
            'description': '通过参数`enableEvents`启用鼠标移入、移出监听功能后，可通过回调函数监听`mouseEnterCount`、`mouseLeaveCount`变化。',
        },
        {
            'path': 'listen_click',
            'title': '监听单击、双击',
            'description': '通过参数`enableEvents`启用单击、双击监听功能后，可通过回调函数监听`nClicks`、`nDoubleClicks`变化。',
        },
        {
            'path': 'listen_context_menu',
            'title': '监听鼠标右键',
            'description': '通过参数`enableEvents`启用鼠标右键监听功能后，可通过回调函数监听`contextMenuEvent`变化。',
        },
        {
            'path': 'listen_is_hovering',
            'title': '监听鼠标悬停状态',
            'description': '通过参数`enableEvents`启用鼠标悬停监听功能后，可通过回调函数监听`isHovering`变化。',
        },
        {
            'path': 'listen_click_away',
            'title': '监听容器外点击',
            'description': '通过参数`enableEvents`启用容器外点击监听功能后，可通过回调函数监听`clickAwayCount`变化。',
        },
        {
            'path': 'shadow',
            'title': '快捷设置阴影效果',
            'description': '通过参数`shadow`快捷设置阴影效果。',
        },
        {
            'path': 'scrollbar',
            'title': '快捷设置滚动条效果',
            'description': '通过参数`scrollbar`快捷设置滚动条效果。',
        },
    ]


def render(component: Component, section_name: str = None) -> Component:
    """渲染当前组件演示用例"""

    return demos_render.render(
        component=component,
        demos_config=demos_config,
        section_name=section_name,
    )
