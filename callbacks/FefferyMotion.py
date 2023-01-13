import feffery_utils_components as fuc
from dash.dependencies import Input, Output

from server import app


@app.callback(
    Output('motion-fade-in-demo-output', 'children'),
    Input('motion-fade-in-demo', 'value')
)
def motion_fade_in_demo(value):

    if value == '选项1':
        return fuc.FefferyMotion(
            f'淡入特效',
            id='motion-fade-in-demo-item1',
            style={
                'height': '200px',
                'background': '#00b294',
                'color': 'white',
                'display': 'flex',
                'justifyContent': 'center',
                'alignItems': 'center'
            },
            initial={
                'opacity': 0
            },
            animate={
                'opacity': 1
            },
            transition={
                'duration': 0.3
            }
        )

    elif value == '选项2':
        return fuc.FefferyMotion(
            f'上升+淡入特效',
            id='motion-fade-in-demo-item2',
            style={
                'height': '200px',
                'background': '#00b294',
                'color': 'white',
                'display': 'flex',
                'justifyContent': 'center',
                'alignItems': 'center'
            },
            initial={
                'opacity': 0,
                'marginTop': 25
            },
            animate={
                'opacity': 1,
                'marginTop': 0
            },
            transition={
                'duration': 0.3
            }
        )

    elif value == '选项3':
        return fuc.FefferyMotion(
            f'从右进场+淡入特效',
            id='motion-fade-in-demo-item3',
            style={
                'height': '200px',
                'background': '#00b294',
                'color': 'white',
                'display': 'flex',
                'justifyContent': 'center',
                'alignItems': 'center'
            },
            initial={
                'opacity': 0,
                'marginLeft': 25
            },
            animate={
                'opacity': 1,
                'marginLeft': 0
            },
            transition={
                'duration': 0.3
            }
        )

    elif value == '选项4':
        return fuc.FefferyMotion(
            f'从左进场+淡入特效',
            id='motion-fade-in-demo-item4',
            style={
                'height': '200px',
                'background': '#00b294',
                'color': 'white',
                'display': 'flex',
                'justifyContent': 'center',
                'alignItems': 'center'
            },
            initial={
                'opacity': 0,
                'marginRight': 25
            },
            animate={
                'opacity': 1,
                'marginRight': 0
            },
            transition={
                'duration': 0.3
            }
        )

    elif value == '选项5':
        return fuc.FefferyMotion(
            f'上升+3D+淡入特效',
            id='motion-fade-in-demo-item5',
            style={
                'height': '200px',
                'background': '#00b294',
                'color': 'white',
                'display': 'flex',
                'justifyContent': 'center',
                'alignItems': 'center'
            },
            initial={
                'opacity': 0,
                'marginTop': 25,
                'rotateX': '45deg'
            },
            animate={
                'opacity': 1,
                'marginTop': 0,
                'rotateX': '0deg'
            },
            transition={
                'duration': 0.75
            }
        )
