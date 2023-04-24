import json
from dash import html
from dash.dependencies import Input, Output

from server import app


@app.callback(
    Output('div-demo1', 'children'),
    [Input('div-demo1', '_width'),
     Input('div-demo1', '_height')],
    prevent_initial_call=True
)
def div_demo1(_width, _height):

    return f'_width: {_width}  _height: {_height}'


@app.callback(
    Output('div-demo2', 'children'),
    [Input('div-demo2', 'mouseEnterCount'),
     Input('div-demo2', 'mouseLeaveCount')]
)
def div_demo2(mouseEnterCount, mouseLeaveCount):

    return f'mouseEnterCount: {mouseEnterCount} mouseLeaveCount: {mouseLeaveCount}'


@app.callback(
    Output('div-demo3', 'children'),
    [Input('div-demo3', 'nClicks'),
     Input('div-demo3', 'nDoubleClicks')]
)
def div_demo3(nClicks, nDoubleClicks):

    return f'nClicks: {nClicks} nDoubleClicks: {nDoubleClicks}'


@app.callback(
    Output('div-demo4', 'children'),
    Input('div-demo4', 'contextMenuEvent'),
    prevent_initial_call=True
)
def div_demo4(contextMenuEvent):

    return html.Pre(
        json.dumps(
            contextMenuEvent,
            ensure_ascii=False,
            indent=4
        )
    )


@app.callback(
    Output('div-demo5', 'children'),
    Input('div-demo5', 'isHovering')
)
def div_demo5(isHovering):

    return f'isHovering: {isHovering}'


@app.callback(
    Output('div-demo6', 'children'),
    Input('div-demo6', 'clickAwayCount')
)
def div_demo6(clickAwayCount):

    return f'clickAwayCount: {clickAwayCount}'
