import dash
from dash import html

import feffery_utils_components as fuc
from dash.dependencies import Component
from dash.dependencies import Input, Output, State
import json

from server import app


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = [
        fuc.FefferyDPlayer(
            id='video-player',
            video={
                'url': 'https://vjs.zencdn.net/v/oceans.mp4',
                'type': 'auto',
            },
            theme='#FADFA3',
            style={'width': '100%'},
            intervalMonitor=True,
        ),
        html.Pre(
            id='video-info',
            style={'height': 100},
        ),
    ]

    return demo_contents  # type: ignore


@app.callback(
    Output('video-info', 'children'),
    Input('video-player', 'currentVideoInfo'),
)
def listen_video_info(currentVideoInfo):
    if currentVideoInfo is None:
        return dash.no_update
    if currentVideoInfo['currentTime'] > 0:
        return [json.dumps(currentVideoInfo, indent=4, ensure_ascii=False)]
    return dash.no_update


def code_string() -> list:
    """返回当前语种对应的演示代码"""

    return [
        {
            'code': """
        fuc.FefferyDPlayer(
            id='video-player',
            video={
                'url': 'https://vjs.zencdn.net/v/oceans.mp4',
                'type': 'auto',
            },
            theme='#FADFA3',
            style={'width': '100%'},
            intervalMonitor=True,
        ),
        html.Pre(
            id='video-info',
            style={'height': 100},
        ),

        @app.callback(
            Output('video-info', 'children'),
            Input('video-player', 'currentVideoInfo'),
        )
        def listen_video_info(currentVideoInfo):
            if currentVideoInfo is None:
                return dash.no_update
            if currentVideoInfo['currentTime'] > 0:
                return [json.dumps(currentVideoInfo, indent=4, ensure_ascii=False)]
            return dash.no_update
"""
        }
    ]
