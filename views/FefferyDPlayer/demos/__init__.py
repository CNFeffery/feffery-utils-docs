from functools import partial
from dash.dependencies import Component

from . import (
    basic_usage,
    listen_video_info,  # noqa: F401
    theme_color,  # noqa: F401
    logo  # noqa: F401,  # noqa: F401
)
from components import demos_render

# 国际化
from i18n import translator


def demos_config() -> list:
    t = partial(translator.t, locale_topic='FefferyDPlayer')
    return [
        {
            'path': 'basic_usage',
            'title': t('基础使用'),
            'description': '最基础的视频播放器，自动识别视频源格式类型。',
        },
        {
            'path': 'theme_color',
            'title': '主题色',
            'description': '自定义视频播放器主题色。',
        },
        {
            'path': 'logo',
            'title': '视频logo',
            'description': '在左上角展示一个 logo，可以通过`CSS`调整它的大小和位置。',
        },
        {
            'path': 'listen_video_info',
            'title': '监听视频播放信息',
            'description': '视频播放状态 currentVideoInfo 回调。',
        },
    ]


def render(component: Component, section_name: str = None) -> Component:
    """渲染当前组件演示用例"""

    return demos_render.render(
        component=component,
        demos_config=demos_config,
        section_name=section_name,
    )
