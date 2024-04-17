from dash import html
import feffery_antd_components as fac
import feffery_utils_components as fuc
import feffery_markdown_components as fmc

import callbacks.FefferyWebSocket
from views.side_props import render_side_props_layout

docs_content = html.Div(
    [
        html.Div(
            [
                fac.AntdBackTop(
                    duration=0.3
                ),

                fac.AntdBreadcrumb(
                    items=[
                        {
                            'title': '通用组件'
                        },
                        {
                            'title': 'FefferyWebSocket WebSocket通信'
                        }
                    ]
                ),

                fac.AntdDivider(isDashed=True),

                fac.AntdParagraph(
                    [
                        fac.AntdText('　　用于与WebSocket服务进行通信。')
                    ]
                ),

                html.Div(
                    [

                        fuc.FefferyWebSocket(
                            id='websocket-demo',
                            socketUrl='wss://ws.postman-echo.com/raw'
                        ),

                        fac.AntdSpace(
                            [
                                fac.AntdButton(
                                    '发送',
                                    id='websocket-send',
                                    disabled=True
                                ),
                                fac.AntdButton(
                                    '断开连接',
                                    id='websocket-disconnect',
                                    danger=True,
                                    disabled=True
                                ),
                                fac.AntdButton(
                                    '重新连接',
                                    type='primary',
                                    id='websocket-connect',
                                    disabled=True
                                )
                            ]
                        ),

                        fac.AntdParagraph(
                            id='websocket-demo-state'
                        ),

                        fac.AntdText(
                            '已接受消息：',
                            strong=True
                        ),

                        html.Div(
                            id='websocket-demo-message-history',
                            style={
                                'maxHeight': '200px',
                                'overflow': 'auto',
                                'whiteSpace': 'break-spaces',
                                'background': '#f1f3f4',
                                'padding': '5px'
                            }
                        ),

                        fac.AntdDivider(
                            '基础使用',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdCollapse(
                            fmc.FefferySyntaxHighlighter(
                                showLineNumbers=True,
                                language='python',
                                codeTheme='coy-without-shadows',
                                codeString="""
fuc.FefferyWebSocket(
    id='websocket-demo',
    socketUrl='wss://ws.postman-echo.com/raw'
),

fac.AntdSpace(
    [
        fac.AntdButton(
            '发送',
            id='websocket-send',
            disabled=True
        ),
        fac.AntdButton(
            '断开连接',
            id='websocket-disconnect',
            danger=True,
            disabled=True
        ),
        fac.AntdButton(
            '重新连接',
            type='primary',
            id='websocket-connect',
            disabled=True
        )
    ]
),

fac.AntdParagraph(
    id='websocket-demo-state'
),

fac.AntdText(
    '已接受消息：',
    strong=True
),

html.Div(
    id='websocket-demo-message-history',
    style={
        'maxHeight': '200px',
        'overflow': 'auto',
        'whiteSpace': 'break-spaces',
        'background': '#f1f3f4',
        'padding': '5px'
    }
)

...

app.clientside_callback(
    '''(state) => `state: ${state}`''',
    Output('websocket-demo-state', 'children'),
    Input('websocket-demo', 'state')
)

app.clientside_callback(
    '''(state) => {
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
            return `${latestMessage}\\n${children}`;
        }
        return window.dash_clientside.no_update;
    }''',
    Output('websocket-demo-message-history', 'children'),
    Input('websocket-demo', 'latestMessage'),
    State('websocket-demo-message-history', 'children')
)
"""
                            ),
                            title='点击查看代码',
                            isOpen=False,
                            ghost=True
                        )
                    ],
                    style={
                        'marginBottom': '40px',
                        'padding': '10px 10px 20px 10px',
                        'border': '1px solid #f0f0f0'
                    },
                    id='基础使用',
                    className='div-highlight'
                ),

                html.Div(style={'height': '100px'})
            ],
            style={
                'flex': 'auto',
                'padding': '25px'
            }
        ),
        html.Div(
            fac.AntdAnchor(
                linkDict=[
                    {'title': '基础使用', 'href': '#基础使用'}
                ],
                offsetTop=0
            ),
            style={
                'flex': 'none',
                'padding': '25px'
            }
        ),
        # 侧边参数栏
        render_side_props_layout(
            component_name='FefferyWebSocket'
        )
    ],
    style={
        'display': 'flex'
    }
)
