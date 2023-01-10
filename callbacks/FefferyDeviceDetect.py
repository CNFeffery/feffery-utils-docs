from dash.dependencies import Input, Output

from server import app


@app.callback(
    Output('device-detect-output', 'data'),
    Input('device-detect', 'deviceInfo')
)
def device_detect_demo(deviceInfo):

    return deviceInfo
