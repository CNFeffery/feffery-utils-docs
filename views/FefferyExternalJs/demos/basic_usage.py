import dash
import feffery_antd_components as fac
import feffery_utils_components as fuc
from dash.dependencies import Component, Input, Output

from server import app


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = [
        fac.AntdSpace(
            [
                fac.AntdButton('挂载party.js', id='mount-js'),
                fac.AntdText(id='mount-js-status'),
                fac.AntdButton(
                    '点我试试', id='effect-when-mount', type='primary'
                ),
            ],
            direction='vertical',
        ),
        fuc.FefferyExternalJs(id='external-js-demo'),
        fuc.FefferyExecuteJs(id='execute-party-effect'),
    ]

    return demo_contents


app.clientside_callback(
    '(recentlyStatus) => `recentlyStatus: ${recentlyStatus}`',
    Output('mount-js-status', 'children'),
    Input('external-js-demo', 'recentlyStatus'),
)


@app.callback(
    [
        Output('external-js-demo', 'jsUrl'),
        Output('execute-party-effect', 'jsString'),
    ],
    Input('mount-js', 'nClicks'),
    prevent_initial_call=True,
)
def external_js_demo(nClicks):
    if nClicks and nClicks == 1:
        return [
            'https://fastly.jsdelivr.net/npm/party-js@latest/bundle/party.min.js',
            """
document.querySelector("#effect-when-mount").addEventListener("click", function (e) {
    party.confetti(this);
});
""",
        ]

    return dash.no_update


def code_string() -> list:
    """返回当前语种对应的演示代码"""

    return [
        {
            'code': '''
[
    fac.AntdSpace(
        [
            fac.AntdButton('挂载party.js', id='mount-js'),
            fac.AntdText(id='mount-js-status'),
            fac.AntdButton(
                '点我试试', id='effect-when-mount', type='primary'
            ),
        ],
        direction='vertical',
    ),
    fuc.FefferyExternalJs(id='external-js-demo'),
    fuc.FefferyExecuteJs(id='execute-party-effect'),
]

...

app.clientside_callback(
    '(recentlyStatus) => `recentlyStatus: ${recentlyStatus}`',
    Output('mount-js-status', 'children'),
    Input('external-js-demo', 'recentlyStatus'),
)


@app.callback(
    [
        Output('external-js-demo', 'jsUrl'),
        Output('execute-party-effect', 'jsString'),
    ],
    Input('mount-js', 'nClicks'),
    prevent_initial_call=True,
)
def external_js_demo(nClicks):
    if nClicks and nClicks == 1:
        return [
            'https://fastly.jsdelivr.net/npm/party-js@latest/bundle/party.min.js',
            """
document.querySelector("#effect-when-mount").addEventListener("click", function (e) {
    party.confetti(this);
});
""",
        ]

    return dash.no_update
'''
        }
    ]
