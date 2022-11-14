import json
from dash.dependencies import Input, Output

from server import app


@app.callback(
    Output('geolocation-demo-output', 'children'),
    Input('geolocation-demo', 'geoLocationInfo')
)
def geolocation_demo(geoLocationInfo):

    return json.dumps(
        geoLocationInfo,
        ensure_ascii=False,
        indent=4
    )
