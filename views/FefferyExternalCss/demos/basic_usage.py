import dash
from dash import html
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
                fac.AntdButton('挂载dark.css', id='mount-dark-css'),
                fac.AntdButton('卸载已有css', id='unmount-css'),
            ],
            style={'marginBottom': '15px'},
        ),
        fuc.FefferyExternalCss(id='external-css-demo'),
        html.Div('FefferyExternalCss示例', className='external-css-dark-demo'),
    ]

    return demo_contents


@app.callback(
    Output('external-css-demo', 'cssUrl'),
    [Input('mount-dark-css', 'nClicks'), Input('unmount-css', 'nClicks')],
    prevent_initial_call=True,
)
def external_css_demo(*args):
    if dash.ctx.triggered_id == 'mount-dark-css':
        return '/assets/css/dark.css'

    return ''


def code_string() -> list:
    """返回当前语种对应的演示代码"""

    return [
        {
            'code': """
[
    fac.AntdSpace(
        [
            fac.AntdButton('挂载dark.css', id='mount-dark-css'),
            fac.AntdButton('卸载已有css', id='unmount-css'),
        ],
        style={'marginBottom': '15px'},
    ),
    fuc.FefferyExternalCss(id='external-css-demo'),
    html.Div('FefferyExternalCss示例', className='external-css-dark-demo'),
]

...

@app.callback(
    Output('external-css-demo', 'cssUrl'),
    [Input('mount-dark-css', 'nClicks'), Input('unmount-css', 'nClicks')],
    prevent_initial_call=True,
)
def external_css_demo(*args):
    if dash.ctx.triggered_id == 'mount-dark-css':
        return '/assets/css/dark.css'

    return ''
"""
        }
    ]
