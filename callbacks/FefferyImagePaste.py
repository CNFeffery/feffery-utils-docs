from dash.dependencies import Input, Output

from server import app

app.clientside_callback(
    '''(isHovering) => !isHovering;''',
    Output('image-paste-demo', 'disabled'),
    Input('image-paste-container', 'isHovering')
)


app.clientside_callback(
    '''(imageInfo) => imageInfo.base64;''',
    Output('image-paste-output', 'src'),
    Input('image-paste-demo', 'imageInfo'),
    prevent_initial_call=True
)
