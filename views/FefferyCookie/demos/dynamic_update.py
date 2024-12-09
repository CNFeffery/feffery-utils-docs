from flask import request
import feffery_antd_components as fac
import feffery_utils_components as fuc
from dash.dependencies import Component, Input, Output, State

from server import app


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = [
        fuc.FefferyCookie(
            id='cookie-dynamic-update-value-demo',
            cookieKey='feffery-cookie-dynamic-update-demo',
            defaultValue='1',
        ),
        fac.AntdCompact(
            [
                fac.AntdButton(
                    'cookie值自增1',
                    id='cookie-dynamic-update-value-demo-add-one',
                ),
                fac.AntdButton(
                    '获取最新cookie值',
                    id='cookie-dynamic-update-value-demo-update-output',
                ),
            ]
        ),
        fac.AntdParagraph(id='cookie-dynamic-update-value-demo-output'),
    ]

    return demo_contents


@app.callback(
    Output('cookie-dynamic-update-value-demo', 'value'),
    Input('cookie-dynamic-update-value-demo-add-one', 'nClicks'),
    State('cookie-dynamic-update-value-demo', 'value'),
    prevent_initial_call=True,
)
def cookie_dynamic_update_value_demo_add_one(nClicks, value):
    return str(int(value) + 1)


@app.callback(
    Output('cookie-dynamic-update-value-demo-output', 'children'),
    Input('cookie-dynamic-update-value-demo-update-output', 'nClicks'),
)
def cookie_dynamic_update_value_demo_output(nClicks):
    return 'feffery-cookie-dynamic-update-demo: {}'.format(
        request.cookies.get('feffery-cookie-dynamic-update-demo')
    )


def code_string() -> list:
    """返回当前语种对应的演示代码"""

    return [
        {
            'code': """
[
    fuc.FefferyCookie(
        id='cookie-dynamic-update-value-demo',
        cookieKey='feffery-cookie-dynamic-update-demo',
        defaultValue='1',
    ),
    fac.AntdCompact(
        [
            fac.AntdButton(
                'cookie值自增1',
                id='cookie-dynamic-update-value-demo-add-one',
            ),
            fac.AntdButton(
                '获取最新cookie值',
                id='cookie-dynamic-update-value-demo-update-output',
            ),
        ]
    ),
    fac.AntdParagraph(id='cookie-dynamic-update-value-demo-output'),
]

...

@app.callback(
    Output('cookie-dynamic-update-value-demo', 'value'),
    Input('cookie-dynamic-update-value-demo-add-one', 'nClicks'),
    State('cookie-dynamic-update-value-demo', 'value'),
    prevent_initial_call=True,
)
def cookie_dynamic_update_value_demo_add_one(nClicks, value):
    return str(int(value) + 1)


@app.callback(
    Output('cookie-dynamic-update-value-demo-output', 'children'),
    Input('cookie-dynamic-update-value-demo-update-output', 'nClicks'),
)
def cookie_dynamic_update_value_demo_output(nClicks):
    return 'feffery-cookie-dynamic-update-demo: {}'.format(
        request.cookies.get('feffery-cookie-dynamic-update-demo')
    )
"""
        }
    ]
