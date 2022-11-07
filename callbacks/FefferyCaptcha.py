from dash.dependencies import Input, Output

from server import app


@app.callback(
    Output('output-demo1', 'children'),
    Input('captcha-demo1', 'captcha')
)
def captcha_demo1(captcha):

    return f'当前验证码：{captcha}'


@app.callback(
    Output('captcha-demo2', 'refresh'),
    Input('refresh-captcha', 'nClicks'),
    prevent_initial_call=True
)
def captcha_demo2(nClicks):

    return True
