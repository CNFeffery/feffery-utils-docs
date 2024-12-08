import feffery_antd_components as fac
import feffery_utils_components as fuc
from dash.dependencies import Component, Input, Output

from server import app


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdSpace(
        [
            fac.AntdSwitch(
                id='css-var-demo',
                checked=False,
                unCheckedChildren='🌞',
                checkedChildren='🌛',
            ),
            fuc.FefferyCssVar(id='css-var-demo-output'),
            fac.AntdCenter(
                'FefferyCssVar示例',
                style={
                    'background': 'var(--demo-bg-color)',
                    'color': 'var(--demo-color)',
                    'fontSize': '28px',
                    'transition': '0.2s',
                    'padding': '100px 150px',
                    'borderRadius': '5px',
                },
            ),
        ],
        direction='vertical',
    )

    return demo_contents


app.clientside_callback(
    """(checked) => {
        if (checked) {
            return {
                '--demo-bg-color': 'black',
                '--demo-color': 'white'
            }
        }
        return {
            '--demo-bg-color': '#fffbe6',
            '--demo-color': 'black'
        }
    }""",
    Output('css-var-demo-output', 'cssVars'),
    Input('css-var-demo', 'checked'),
)


def code_string() -> list:
    """返回当前语种对应的演示代码"""

    return [
        {
            'code': '''
fac.AntdSpace(
    [
        fac.AntdSwitch(
            id='css-var-demo',
            checked=False,
            unCheckedChildren='🌞',
            checkedChildren='🌛',
        ),
        fuc.FefferyCssVar(id='css-var-demo-output'),
        fac.AntdCenter(
            'FefferyCssVar示例',
            style={
                'background': 'var(--demo-bg-color)',
                'color': 'var(--demo-color)',
                'fontSize': '28px',
                'transition': '0.2s',
                'padding': '100px 150px',
                'borderRadius': '5px',
            },
        ),
    ],
    direction='vertical',
)

...

app.clientside_callback(
    """(checked) => {
        if (checked) {
            return {
                '--demo-bg-color': 'black',
                '--demo-color': 'white'
            }
        }
        return {
            '--demo-bg-color': '#fffbe6',
            '--demo-color': 'black'
        }
    }""",
    Output('css-var-demo-output', 'cssVars'),
    Input('css-var-demo', 'checked'),
)
'''
        }
    ]
