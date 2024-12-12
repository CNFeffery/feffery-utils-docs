import feffery_antd_components as fac
import feffery_utils_components as fuc
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = [
        fuc.FefferyStyle(
            rawStyle="""
.custom-right-resize-handle:hover, .custom-right-resize-handle:active {
    background: #007fd4;
    transition: 0.3s background;
}

.custom-right-resize-handle {
    transition: 0.3s background;
    width: 4px !important;
    right: -2px !important;
}
"""
        ),
        fuc.FefferyResizable(
            fac.AntdCenter(
                "direction=['right']",
                style={
                    'height': '100%',
                    'background': '#dee2e6',
                },
            ),
            defaultSize={'width': 200, 'height': 200},
            direction=['right'],
            handleClassNames={'right': 'custom-right-resize-handle'},
            bounds='parent',
        ),
    ]

    return demo_contents


def code_string() -> list:
    """返回当前语种对应的演示代码"""

    return [
        {
            'code': '''
[
    fuc.FefferyStyle(
        rawStyle="""
.custom-right-resize-handle:hover, .custom-right-resize-handle:active {
    background: #007fd4;
    transition: 0.3s background;
}

.custom-right-resize-handle {
    transition: 0.3s background;
    width: 4px !important;
    right: -2px !important;
}
"""
    ),
    fuc.FefferyResizable(
        fac.AntdCenter(
            "direction=['right']",
            style={
                'height': '100%',
                'background': '#dee2e6',
            },
        ),
        defaultSize={'width': 200, 'height': 200},
        direction=['right'],
        handleClassNames={'right': 'custom-right-resize-handle'},
        bounds='parent',
    ),
]
'''
        }
    ]
