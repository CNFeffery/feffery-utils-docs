import feffery_utils_components as fuc
from dash.dependencies import Component, Input, Output

from server import app


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = [
        fuc.FefferyDeviceDetect(id='device-detect'),
        fuc.FefferyJsonViewer(id='device-detect-output'),
    ]

    return demo_contents


@app.callback(
    Output('device-detect-output', 'data'), Input('device-detect', 'deviceInfo')
)
def device_detect_demo(deviceInfo):
    return deviceInfo


def code_string() -> list:
    """返回当前语种对应的演示代码"""

    return [
        {
            'code': """
[
    fuc.FefferyDeviceDetect(id='device-detect'),
    fuc.FefferyJsonViewer(id='device-detect-output'),
]

...

@app.callback(
    Output('device-detect-output', 'data'), Input('device-detect', 'deviceInfo')
)
def device_detect_demo(deviceInfo):
    return deviceInfo
"""
        }
    ]
