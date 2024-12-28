from dash import html
import feffery_antd_components as fac
import feffery_utils_components as fuc
from dash.dependencies import Component, Input, Output

from server import app


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdSpace(
        [
            fac.AntdSegmented(
                id='motion-fade-in-demo',
                options=[
                    {'label': f'选项{i}', 'value': f'选项{i}'}
                    for i in range(1, 6)
                ],
                block=True,
                value='选项1',
            ),
            html.Div(id='motion-fade-in-demo-output'),
        ],
        direction='vertical',
        style={'width': '100%'},
    )

    return demo_contents


@app.callback(
    Output('motion-fade-in-demo-output', 'children'),
    Input('motion-fade-in-demo', 'value'),
)
def motion_fade_in_demo(value):
    if value == '选项1':
        return fuc.FefferyMotion(
            '淡入特效',
            id='motion-fade-in-demo-item1',
            style={
                'height': '200px',
                'background': '#00b294',
                'color': 'white',
                'display': 'flex',
                'justifyContent': 'center',
                'alignItems': 'center',
            },
            initial={'opacity': 0},
            animate={'opacity': 1},
            transition={'duration': 0.3},
        )

    elif value == '选项2':
        return fuc.FefferyMotion(
            '上升+淡入特效',
            id='motion-fade-in-demo-item2',
            style={
                'height': '200px',
                'background': '#00b294',
                'color': 'white',
                'display': 'flex',
                'justifyContent': 'center',
                'alignItems': 'center',
            },
            initial={'opacity': 0, 'marginTop': 25},
            animate={'opacity': 1, 'marginTop': 0},
            transition={'duration': 0.3},
        )

    elif value == '选项3':
        return fuc.FefferyMotion(
            '从右进场+淡入特效',
            id='motion-fade-in-demo-item3',
            style={
                'height': '200px',
                'background': '#00b294',
                'color': 'white',
                'display': 'flex',
                'justifyContent': 'center',
                'alignItems': 'center',
            },
            initial={'opacity': 0, 'marginLeft': 25},
            animate={'opacity': 1, 'marginLeft': 0},
            transition={'duration': 0.3},
        )

    elif value == '选项4':
        return fuc.FefferyMotion(
            '从左进场+淡入特效',
            id='motion-fade-in-demo-item4',
            style={
                'height': '200px',
                'background': '#00b294',
                'color': 'white',
                'display': 'flex',
                'justifyContent': 'center',
                'alignItems': 'center',
            },
            initial={'opacity': 0, 'marginRight': 25},
            animate={'opacity': 1, 'marginRight': 0},
            transition={'duration': 0.3},
        )

    elif value == '选项5':
        return fuc.FefferyMotion(
            '上升+3D+淡入特效',
            id='motion-fade-in-demo-item5',
            style={
                'height': '200px',
                'background': '#00b294',
                'color': 'white',
                'display': 'flex',
                'justifyContent': 'center',
                'alignItems': 'center',
            },
            initial={'opacity': 0, 'marginTop': 25, 'rotateX': '45deg'},
            animate={'opacity': 1, 'marginTop': 0, 'rotateX': '0deg'},
            transition={'duration': 0.75},
        )


def code_string() -> list:
    """返回当前语种对应的演示代码"""

    return [
        {
            'code': """
fac.AntdSpace(
    [
        fac.AntdSegmented(
            id='motion-fade-in-demo',
            options=[
                {'label': f'选项{i}', 'value': f'选项{i}'}
                for i in range(1, 6)
            ],
            block=True,
            value='选项1',
        ),
        html.Div(id='motion-fade-in-demo-output'),
    ],
    direction='vertical',
    style={'width': '100%'},
)

...

@app.callback(
    Output('motion-fade-in-demo-output', 'children'),
    Input('motion-fade-in-demo', 'value'),
)
def motion_fade_in_demo(value):
    if value == '选项1':
        return fuc.FefferyMotion(
            '淡入特效',
            id='motion-fade-in-demo-item1',
            style={
                'height': '200px',
                'background': '#00b294',
                'color': 'white',
                'display': 'flex',
                'justifyContent': 'center',
                'alignItems': 'center',
            },
            initial={'opacity': 0},
            animate={'opacity': 1},
            transition={'duration': 0.3},
        )

    elif value == '选项2':
        return fuc.FefferyMotion(
            '上升+淡入特效',
            id='motion-fade-in-demo-item2',
            style={
                'height': '200px',
                'background': '#00b294',
                'color': 'white',
                'display': 'flex',
                'justifyContent': 'center',
                'alignItems': 'center',
            },
            initial={'opacity': 0, 'marginTop': 25},
            animate={'opacity': 1, 'marginTop': 0},
            transition={'duration': 0.3},
        )

    elif value == '选项3':
        return fuc.FefferyMotion(
            '从右进场+淡入特效',
            id='motion-fade-in-demo-item3',
            style={
                'height': '200px',
                'background': '#00b294',
                'color': 'white',
                'display': 'flex',
                'justifyContent': 'center',
                'alignItems': 'center',
            },
            initial={'opacity': 0, 'marginLeft': 25},
            animate={'opacity': 1, 'marginLeft': 0},
            transition={'duration': 0.3},
        )

    elif value == '选项4':
        return fuc.FefferyMotion(
            '从左进场+淡入特效',
            id='motion-fade-in-demo-item4',
            style={
                'height': '200px',
                'background': '#00b294',
                'color': 'white',
                'display': 'flex',
                'justifyContent': 'center',
                'alignItems': 'center',
            },
            initial={'opacity': 0, 'marginRight': 25},
            animate={'opacity': 1, 'marginRight': 0},
            transition={'duration': 0.3},
        )

    elif value == '选项5':
        return fuc.FefferyMotion(
            '上升+3D+淡入特效',
            id='motion-fade-in-demo-item5',
            style={
                'height': '200px',
                'background': '#00b294',
                'color': 'white',
                'display': 'flex',
                'justifyContent': 'center',
                'alignItems': 'center',
            },
            initial={'opacity': 0, 'marginTop': 25, 'rotateX': '45deg'},
            animate={'opacity': 1, 'marginTop': 0, 'rotateX': '0deg'},
            transition={'duration': 0.75},
        )
"""
        }
    ]
