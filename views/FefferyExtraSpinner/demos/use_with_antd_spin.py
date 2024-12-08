import time
from datetime import datetime
import feffery_antd_components as fac
import feffery_utils_components as fuc
from dash.dependencies import Component, Input, Output

from server import app


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdSpace(
        [
            fac.AntdSpace(
                [
                    fac.AntdSelect(
                        id='extra-spinner-demo-type',
                        options=[
                            {'label': _type, 'value': _type}
                            for _type in [
                                'ball',
                                'swap',
                                'bars',
                                'grid',
                                'wave',
                                'push',
                                'firework',
                                'stage',
                                'ring',
                                'heart',
                                'guard',
                                'rotate',
                                'spiral',
                                'pulse',
                                'swish',
                                'sequence',
                                'impulse',
                                'cube',
                                'magic',
                                'flag',
                                'fill',
                                'sphere',
                                'domino',
                                'goo',
                                'comb',
                                'pong',
                                'rainbow',
                                'hoop',
                                'flapper',
                                'jellyfish',
                                'trace',
                                'classic',
                                'metro',
                            ]
                        ],
                        allowClear=False,
                        defaultValue='ball',
                        style={'width': '100px'},
                    ),
                    fac.AntdButton('触发时长5秒回调', id='extra-spinner-demo'),
                ]
            ),
            fac.AntdSpin(
                fac.AntdCenter(
                    datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                    id='extra-spinner-demo-output',
                    style={
                        'width': '100%',
                        'height': '200px',
                        'boxShadow': '0px 0px 12px rgba(0, 0, 0, .12)',
                        'borderRadius': '5px',
                    },
                ),
                id='extra-spinner-demo-spin',
                delay=300,
            ),
        ],
        direction='vertical',
    )

    return demo_contents


@app.callback(
    Output('extra-spinner-demo-output', 'children'),
    Input('extra-spinner-demo', 'nClicks'),
    prevent_initial_call=True,
)
def extra_spinner_demo(nClicks):
    time.sleep(5)

    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')


@app.callback(
    Output('extra-spinner-demo-spin', 'indicator'),
    Input('extra-spinner-demo-type', 'value'),
)
def extra_spinner_demo_indicator(value):
    return fuc.FefferyExtraSpinner(type=value)


def code_string() -> list:
    """返回当前语种对应的演示代码"""

    return [
        {
            'code': """
fac.AntdSpace(
    [
        fac.AntdSpace(
            [
                fac.AntdSelect(
                    id='extra-spinner-demo-type',
                    options=[
                        {'label': _type, 'value': _type}
                        for _type in [
                            'ball',
                            'swap',
                            'bars',
                            'grid',
                            'wave',
                            'push',
                            'firework',
                            'stage',
                            'ring',
                            'heart',
                            'guard',
                            'rotate',
                            'spiral',
                            'pulse',
                            'swish',
                            'sequence',
                            'impulse',
                            'cube',
                            'magic',
                            'flag',
                            'fill',
                            'sphere',
                            'domino',
                            'goo',
                            'comb',
                            'pong',
                            'rainbow',
                            'hoop',
                            'flapper',
                            'jellyfish',
                            'trace',
                            'classic',
                            'metro',
                        ]
                    ],
                    allowClear=False,
                    defaultValue='ball',
                    style={'width': '100px'},
                ),
                fac.AntdButton('触发时长5秒回调', id='extra-spinner-demo'),
            ]
        ),
        fac.AntdSpin(
            fac.AntdCenter(
                datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                id='extra-spinner-demo-output',
                style={
                    'width': '100%',
                    'height': '200px',
                    'boxShadow': '0px 0px 12px rgba(0, 0, 0, .12)',
                    'borderRadius': '5px',
                },
            ),
            id='extra-spinner-demo-spin',
            delay=300,
        ),
    ],
    direction='vertical',
)

...

@app.callback(
    Output('extra-spinner-demo-output', 'children'),
    Input('extra-spinner-demo', 'nClicks'),
    prevent_initial_call=True,
)
def extra_spinner_demo(nClicks):
    time.sleep(5)

    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')


@app.callback(
    Output('extra-spinner-demo-spin', 'indicator'),
    Input('extra-spinner-demo-type', 'value'),
)
def extra_spinner_demo_indicator(value):
    return fuc.FefferyExtraSpinner(type=value)
"""
        }
    ]
