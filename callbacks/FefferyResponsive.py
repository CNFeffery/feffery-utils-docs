import json
from dash.dependencies import Input, Output

from server import app


@app.callback(
    Output('responsive-demo-output', 'children'),
    Input('responsive-demo', 'responsive')
)
def responsive_demo(responsive):

    return json.dumps(
        responsive,
        ensure_ascii=False,
        indent=4
    )
