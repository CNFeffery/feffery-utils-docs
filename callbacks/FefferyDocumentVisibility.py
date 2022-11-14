import time
from dash.dependencies import Input, Output

from server import app


@app.callback(
    Output('document-visibility-demo-output', 'children'),
    Input('document-visibility-demo', 'documentVisibility')
)
def document_visibility_demo(documentVisibility):

    if documentVisibility == 'visible':

        time.sleep(2)

    return f'documentVisibility: {documentVisibility}'
