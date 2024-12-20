import json
from dash import html
import feffery_utils_components as fuc
from dash.dependencies import Component, Input, Output

from server import app


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = [
        fuc.FefferyGeolocation(id='geolocation-demo'),
        html.Pre(id='geolocation-demo-output'),
    ]

    return demo_contents


@app.callback(
    Output('geolocation-demo-output', 'children'),
    Input('geolocation-demo', 'geoLocationInfo'),
)
def geolocation_demo(geoLocationInfo):
    return json.dumps(geoLocationInfo, ensure_ascii=False, indent=4)


def code_string() -> list:
    """返回当前语种对应的演示代码"""

    return [
        {
            'code': """
[
    fuc.FefferyGeolocation(id='geolocation-demo'),
    html.Pre(id='geolocation-demo-output'),
]

...

@app.callback(
    Output('geolocation-demo-output', 'children'),
    Input('geolocation-demo', 'geoLocationInfo'),
)
def geolocation_demo(geoLocationInfo):
    return json.dumps(geoLocationInfo, ensure_ascii=False, indent=4)
"""
        }
    ]
