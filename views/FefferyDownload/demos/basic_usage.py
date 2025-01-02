import feffery_antd_components as fac
import feffery_utils_components as fuc
from dash.dependencies import Component, Input, Output

from server import app


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = [
        fac.AntdButton('下载示例文件', id='download-demo-trigger', type='link'),
        fuc.FefferyDownload(
            id='download-demo',
        ),
    ]

    return demo_contents


@app.callback(
    Output('download-demo', 'file'),
    Input('download-demo-trigger', 'nClicks'),
    prevent_initial_call=True,
)
def download_demo(nClicks):
    return {'url': '/assets/imgs/fuc-logo.svg'}


def code_string() -> list:
    """返回当前语种对应的演示代码"""

    return [
        {
            'code': """
[
    fac.AntdButton('下载示例文件', id='download-demo-trigger', type='link'),
    fuc.FefferyDownload(
        id='download-demo',
    ),
]

...

@app.callback(
    Output('download-demo', 'file'),
    Input('download-demo-trigger', 'nClicks'),
    prevent_initial_call=True,
)
def download_demo(nClicks):
    return {'url': '/assets/imgs/fuc-logo.svg'}
"""
        }
    ]
