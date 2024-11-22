from dash import html
import feffery_antd_components as fac
import feffery_utils_components as fuc
from dash.dependencies import Component, Input, State, Output

from server import app


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = [
        fuc.FefferyWebSocket(
            id='websocket-demo', socketUrl='wss://ws.postman-echo.com/raw'
        ),
        fac.AntdSpace(
            [
                fac.AntdButton('发送', id='websocket-send', disabled=True),
                fac.AntdButton(
                    '断开连接',
                    id='websocket-disconnect',
                    danger=True,
                    disabled=True,
                ),
                fac.AntdButton(
                    '重新连接',
                    type='primary',
                    id='websocket-connect',
                    disabled=True,
                ),
            ]
        ),
        fac.AntdParagraph(id='websocket-demo-state'),
        fac.AntdText('已接受消息：', strong=True),
        html.Div(
            id='websocket-demo-message-history',
            style={
                'maxHeight': '200px',
                'overflow': 'auto',
                'whiteSpace': 'break-spaces',
                'background': '#f1f3f4',
                'padding': '5px',
            },
        ),
    ]

    return demo_contents


app.clientside_callback(
    """(state) => `state: ${state}`""",
    Output('websocket-demo-state', 'children'),
    Input('websocket-demo', 'state'),
)

app.clientside_callback(
    """(state) => {
        console.log(state)
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
    }""",
    [
        Output('websocket-send', 'disabled'),
        Output('websocket-disconnect', 'disabled'),
        Output('websocket-connect', 'disabled'),
    ],
    Input('websocket-demo', 'state'),
)

app.clientside_callback(
    """(e1, e2, e3) => {
        if ( window.dash_clientside.callback_context.triggered[0].prop_id === "websocket-send.nClicks" ) {
            return ["send", `${Date.now()}`]
        } else if ( window.dash_clientside.callback_context.triggered[0].prop_id === "websocket-disconnect.nClicks" ) {
            return ["disconnect", null]
        } else if ( window.dash_clientside.callback_context.triggered[0].prop_id === "websocket-connect.nClicks" ) {
            return ["connect", null]
        }
    }""",
    [
        Output('websocket-demo', 'operation'),
        Output('websocket-demo', 'message'),
    ],
    [
        Input('websocket-send', 'nClicks'),
        Input('websocket-disconnect', 'nClicks'),
        Input('websocket-connect', 'nClicks'),
    ],
    prevent_initial_call=True,
)


app.clientside_callback(
    """(latestMessage, children) => {
        if ( latestMessage ) {
            return `${latestMessage}\n${children}`;
        }
        return window.dash_clientside.no_update;
    }""",
    Output('websocket-demo-message-history', 'children'),
    Input('websocket-demo', 'latestMessage'),
    State('websocket-demo-message-history', 'children'),
)


def code_string() -> list:
    """返回当前语种对应的演示代码"""

    return [
        {
            'code': '''
[
    fuc.FefferyWebSocket(
        id='websocket-demo', socketUrl='wss://ws.postman-echo.com/raw'
    ),
    fac.AntdSpace(
        [
            fac.AntdButton('发送', id='websocket-send', disabled=True),
            fac.AntdButton(
                '断开连接',
                id='websocket-disconnect',
                danger=True,
                disabled=True,
            ),
            fac.AntdButton(
                '重新连接',
                type='primary',
                id='websocket-connect',
                disabled=True,
            ),
        ]
    ),
    fac.AntdParagraph(id='websocket-demo-state'),
    fac.AntdText('已接受消息：', strong=True),
    html.Div(
        id='websocket-demo-message-history',
        style={
            'maxHeight': '200px',
            'overflow': 'auto',
            'whiteSpace': 'break-spaces',
            'background': '#f1f3f4',
            'padding': '5px',
        },
    ),
]

...

app.clientside_callback(
    """(state) => `state: ${state}`""",
    Output('websocket-demo-state', 'children'),
    Input('websocket-demo', 'state'),
)

app.clientside_callback(
    """(state) => {
        console.log(state)
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
    }""",
    [
        Output('websocket-send', 'disabled'),
        Output('websocket-disconnect', 'disabled'),
        Output('websocket-connect', 'disabled'),
    ],
    Input('websocket-demo', 'state'),
)

app.clientside_callback(
    """(e1, e2, e3) => {
        if ( window.dash_clientside.callback_context.triggered[0].prop_id === "websocket-send.nClicks" ) {
            return ["send", `${Date.now()}`]
        } else if ( window.dash_clientside.callback_context.triggered[0].prop_id === "websocket-disconnect.nClicks" ) {
            return ["disconnect", null]
        } else if ( window.dash_clientside.callback_context.triggered[0].prop_id === "websocket-connect.nClicks" ) {
            return ["connect", null]
        }
    }""",
    [
        Output('websocket-demo', 'operation'),
        Output('websocket-demo', 'message'),
    ],
    [
        Input('websocket-send', 'nClicks'),
        Input('websocket-disconnect', 'nClicks'),
        Input('websocket-connect', 'nClicks'),
    ],
    prevent_initial_call=True,
)


app.clientside_callback(
    """(latestMessage, children) => {
        if ( latestMessage ) {
            return `${latestMessage}\\n${children}`;
        }
        return window.dash_clientside.no_update;
    }""",
    Output('websocket-demo-message-history', 'children'),
    Input('websocket-demo', 'latestMessage'),
    State('websocket-demo-message-history', 'children'),
)
'''
        }
    ]
