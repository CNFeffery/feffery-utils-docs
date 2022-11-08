from dash.dependencies import Input, Output

from server import app

# 使用浏览器端回调以实现更丝滑的响应速度
app.clientside_callback(
    '''(checked) => {
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
    }''',
    Output('css-var-demo-output', 'cssVars'),
    Input('css-var-demo', 'checked')
)
