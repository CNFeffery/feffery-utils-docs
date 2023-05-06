import json
from dash.dependencies import Input, Output

from server import app


@app.callback(
    Output('location-demo-output', 'children'),
    [Input('location-demo', 'href'),
     Input('location-demo', 'pathname'),
     Input('location-demo', 'search'),
     Input('location-demo', 'hash'),
     Input('location-demo', 'host'),
     Input('location-demo', 'hostname'),
     Input('location-demo', 'port'),
     Input('location-demo', 'protocol'),
     Input('location-demo', 'trigger')]
)
def lcoation_demo(href,
                  pathname,
                  search,
                  hash,
                  host,
                  hostname,
                  port,
                  protocol,
                  trigger):

    return json.dumps(
        dict(
            href=href,
            pathname=pathname,
            search=search,
            hash=hash,
            host=host,
            hostname=hostname,
            port=port,
            protocol=protocol,
            trigger=trigger
        ),
        indent=4,
        ensure_ascii=False
    )
