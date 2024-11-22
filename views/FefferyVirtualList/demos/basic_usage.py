import feffery_utils_components as fuc
from dash.dependencies import Component, Input, Output

from server import app


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fuc.FefferyVirtualList(
        id='virtual-list-demo', height=400, itemHeight=40
    )

    return demo_contents


app.clientside_callback(
    """(pathname) => {
        let childrenList = [];
        for (let i = 0;i<1000;i++) {
            childrenList.push(
                {
                    'props': {
                        'message': `演示列表子元素${i}`,
                        'showIcon': true,
                        'type': 'info'
                    },
                    'type': 'AntdAlert',
                    'namespace': 'feffery_antd_components'
                }
            );
        }

        return childrenList;
    }""",
    Output('virtual-list-demo', 'children'),
    Input('virtual-list-demo', 'id'),
)


def code_string() -> list:
    """返回当前语种对应的演示代码"""

    return [
        {
            'code': '''
fuc.FefferyVirtualList(
    id='virtual-list-demo', height=400, itemHeight=40
)

...

app.clientside_callback(
    """(pathname) => {
        let childrenList = [];
        for (let i = 0;i<1000;i++) {
            childrenList.push(
                {
                    'props': {
                        'message': `演示列表子元素${i}`,
                        'showIcon': true,
                        'type': 'info'
                    },
                    'type': 'AntdAlert',
                    'namespace': 'feffery_antd_components'
                }
            );
        }

        return childrenList;
    }""",
    Output('virtual-list-demo', 'children'),
    Input('virtual-list-demo', 'id'),
)
'''
        }
    ]
