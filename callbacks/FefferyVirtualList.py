from dash.dependencies import Input, Output

from server import app

app.clientside_callback(
    '''(pathname) => {
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
    }''',
    Output('virtual-list-demo', 'children'),
    Input('url', 'pathname')
)