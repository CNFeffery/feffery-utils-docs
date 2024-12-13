import json
from dash import html, dcc
import feffery_antd_components as fac
import feffery_utils_components as fuc
from dash.dependencies import Component, Input, Output

from server import app


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = [
        fuc.FefferyLocation(id='location-demo'),
        fac.AntdSpace(
            [
                fac.AntdText('示例链接：'),
                dcc.Link(
                    '/FefferyLocation#基础使用',
                    href='/FefferyLocation#基础使用',
                ),
                dcc.Link(
                    '/FefferyLocation?a=1&b=2', href='/FefferyLocation?a=1&b=2'
                ),
            ]
        ),
        html.Pre(id='location-demo-output'),
    ]

    return demo_contents


@app.callback(
    Output('location-demo-output', 'children'),
    [
        Input('location-demo', 'href'),
        Input('location-demo', 'pathname'),
        Input('location-demo', 'search'),
        Input('location-demo', 'hash'),
        Input('location-demo', 'host'),
        Input('location-demo', 'hostname'),
        Input('location-demo', 'port'),
        Input('location-demo', 'protocol'),
        Input('location-demo', 'trigger'),
    ],
)
def lcoation_demo(
    href, pathname, search, hash, host, hostname, port, protocol, trigger
):
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
            trigger=trigger,
        ),
        indent=4,
        ensure_ascii=False,
    )


def code_string() -> list:
    """返回当前语种对应的演示代码"""

    return [
        {
            'code': """
[
    fuc.FefferyLocation(id='location-demo'),
    fac.AntdSpace(
        [
            fac.AntdText('示例链接：'),
            dcc.Link(
                '/FefferyLocation#基础使用',
                href='/FefferyLocation#基础使用',
            ),
            dcc.Link(
                '/FefferyLocation?a=1&b=2', href='/FefferyLocation?a=1&b=2'
            ),
        ]
    ),
    html.Pre(id='location-demo-output'),
]

...

@app.callback(
    Output('location-demo-output', 'children'),
    [
        Input('location-demo', 'href'),
        Input('location-demo', 'pathname'),
        Input('location-demo', 'search'),
        Input('location-demo', 'hash'),
        Input('location-demo', 'host'),
        Input('location-demo', 'hostname'),
        Input('location-demo', 'port'),
        Input('location-demo', 'protocol'),
        Input('location-demo', 'trigger'),
    ],
)
def lcoation_demo(
    href, pathname, search, hash, host, hostname, port, protocol, trigger
):
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
            trigger=trigger,
        ),
        indent=4,
        ensure_ascii=False,
    )
"""
        }
    ]
