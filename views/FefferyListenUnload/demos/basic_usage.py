import feffery_antd_components as fac
import feffery_utils_components as fuc
from dash.dependencies import Component, Input

from server import app


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = [
        fac.AntdText(
            '请在本地运行此示例，通过终端打印的结果查看监听效果。',
            type='secondary',
        ),
        fuc.FefferyListenUnload(id='listen-unload-demo'),
    ]

    return demo_contents


@app.callback(
    Input('listen-unload-demo', 'unloaded'),
    prevent_initial_call=True,
)
def listen_unload_demo(unloaded):
    print(f'unloaded: {unloaded}')


def code_string() -> list:
    """返回当前语种对应的演示代码"""

    return [
        {
            'code': """
fuc.FefferyListenUnload(id='listen-unload-demo')

...

@app.callback(
    Input('listen-unload-demo', 'unloaded'),
    prevent_initial_call=True,
)
def listen_unload_demo(unloaded):
    print(f'unloaded: {unloaded}')
"""
        }
    ]
