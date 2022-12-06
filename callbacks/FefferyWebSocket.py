from dash.dependencies import Input, Output, State

from server import app

app.clientside_callback(
    '''(state) => `state: ${state}`''',
    Output('websocket-demo-state', 'children'),
    Input('websocket-demo', 'state')
)

app.clientside_callback(
    '''(state) => {
        if ( state === "connecting" ) {
            return [true, true, true];
        } else if ( state === "open" ) {
            return [false, false, true];
        } else if ( state === "closing" ) {
            return [true, true, true];
        } else if ( state === "closed" ) {
            return [true, true, false];
        }
        return [false, false, false];
    }''',
    [Output('websocket-send', 'disabled'),
     Output('websocket-disconnect', 'disabled'),
     Output('websocket-connect', 'disabled')],
    Input('websocket-demo', 'state')
)

app.clientside_callback(
    '''(e1, e2, e3) => {
        if ( window.dash_clientside.callback_context.triggered[0].prop_id === "websocket-send.nClicks" ) {
            return ["send", `${Date.now()}`]
        } else if ( window.dash_clientside.callback_context.triggered[0].prop_id === "websocket-disconnect.nClicks" ) {
            return ["disconnect", null]
        } else if ( window.dash_clientside.callback_context.triggered[0].prop_id === "websocket-connect.nClicks" ) {
            return ["connect", null]
        }
    }''',
    [Output('websocket-demo', 'operation'),
     Output('websocket-demo', 'message')],
    [Input('websocket-send', 'nClicks'),
     Input('websocket-disconnect', 'nClicks'),
     Input('websocket-connect', 'nClicks')],
    prevent_initial_call=True
)


app.clientside_callback(
    '''(latestMessage, children) => {
        if ( latestMessage ) {
            return `${latestMessage}\n${children}`;
        }
        return window.dash_clientside.no_update;
    }''',
    Output('websocket-demo-message-history', 'children'),
    Input('websocket-demo', 'latestMessage'),
    State('websocket-demo-message-history', 'children')
)