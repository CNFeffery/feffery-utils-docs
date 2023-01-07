from dash import dcc, html
import feffery_antd_components as fac
import feffery_utils_components as fuc
from dash.dependencies import Input, Output, State

from config import Config
from server import app, server
from views import (
    FefferyBlockColorPicker,
    FefferyCircleColorPicker,
    FefferyEyeDropper,
    FefferyGithubColorPicker,
    FefferyHexColorPicker,
    FefferyRgbColorPicker,
    FefferyTwitterColorPicker,
    FefferyWheelColorPicker,
    FefferyDocumentVisibility,
    FefferyGeolocation,
    FefferyIdle,
    FefferyInViewport,
    FefferyResponsive,
    FefferyWindowSize,
    FefferyGrid,
    FefferyGridItem,
    FefferyCaptcha,
    FefferyCountDown,
    FefferyCssVar,
    FefferyDiv,
    FefferyExecuteJs,
    FefferyExternalCss,
    FefferyExternalJs,
    FefferyExtraSpinner,
    FefferyFancyButton,
    FefferyFancyMessage,
    FefferyFancyNotification,
    FefferyGuide,
    FefferyHighlightWords,
    FefferyJsonViewer,
    FefferyLazyLoad,
    FefferyQRCode,
    FefferyRawHTML,
    FefferyReload,
    FefferyScroll,
    FefferyScrollbars,
    FefferySessionStorage,
    FefferySetTitle,
    FefferyShadowDom,
    FefferyShortcutPanel,
    FefferyStyle,
    FefferyTimeout,
    FefferyTopProgress,
    FefferyVirtualList,
    FefferyWebSocket,
    what_is_fuc
)

app.layout = fuc.FefferyTopProgress(
    html.Div(
        [
            # 注入url监听
            dcc.Location(id='url'),

            # 注入快捷添加好友悬浮卡片
            html.Div(
                [
                    fac.AntdPopover(
                        fac.AntdButton(
                            fac.AntdIcon(icon='antd-bulb'),
                            shape='circle',
                            style={
                                'zoom': '1.25',
                                'boxShadow': '0 3px 6px -4px #0000001f, 0 6px 16px #00000014, 0 9px 28px 8px #0000000d'
                            }
                        ),
                        placement='left',
                        content=[
                            fac.AntdText(
                                '微信扫码加我好友，备注【dash学习】加入学习交流群，更多灵感更快进步',
                                strong=True
                            ),
                            fac.AntdImage(
                                src=app.get_asset_url(
                                    'imgs/feffery-添加好友二维码.jpg'),
                                width=250,
                                preview=False
                            )
                        ],
                        overlayStyle={
                            'width': '300px',
                            'height': '408px'
                        }
                    )
                ],
                style={
                    'position': 'fixed',
                    'right': '100px',
                    'bottom': '200px',
                    'zIndex': 99999
                }
            ),

            # 页面结构
            fac.AntdRow(
                [
                    fac.AntdCol(
                        html.Img(
                            src=app.get_asset_url(
                                'imgs/fuc-logo.svg'
                            ),
                            style={
                                'height': '50px',
                                'padding': '0 10px',
                                'marginTop': '7px'
                            }
                        ),
                    ),
                    fac.AntdCol(
                        fac.AntdParagraph(
                            [
                                fac.AntdText(
                                    'feffery-utils-components',
                                    strong=True,
                                    style={
                                        'fontSize': '35px'
                                    }
                                ),
                                fac.AntdText(
                                    f'v{fuc.__version__}',
                                    style={
                                        'fontSize': '10px',
                                        'paddingLeft': '2px'
                                    }
                                )
                            ]
                        )
                    ),

                    fac.AntdCol(
                        html.Div(
                            [
                                html.A(
                                    fac.AntdImage(
                                        id='github-entry',
                                        alt='fuc源码仓库，欢迎star',
                                        src='https://img.shields.io/github/stars/CNFeffery/feffery-utils-components?style=social',
                                        preview=False,
                                        fallback=None,
                                        style={
                                            'transform': 'translateY(0px) scale(1.25)'
                                        }
                                    ),
                                    href='https://github.com/CNFeffery/feffery-utils-components',
                                    target='_blank',
                                    style={
                                        'cursor': 'pointer'
                                    }
                                ),

                                html.A(
                                    '皖ICP备2021012734号-1',
                                    href='https://beian.miit.gov.cn/',
                                    target='_blank',
                                    style={
                                        'fontSize': '10px',
                                        'marginLeft': '50px',
                                        'color': '#494f54'
                                    }
                                )
                            ],
                            style={
                                'float': 'right',
                                'paddingRight': '20px',
                                'marginTop': '20.5px'
                            }
                        ),
                        flex='auto'
                    )
                ],
                align="middle",
                style={
                    'height': '64px',
                    'boxShadow': 'rgb(240 241 242) 0px 2px 14px',
                    'background': 'white',
                    'marginBottom': '5px'
                }
            ),

            fac.AntdRow(
                [
                    fac.AntdCol(
                        fac.AntdAffix(
                            html.Div(
                                [
                                    fac.AntdMenu(
                                        id='router-menu',
                                        menuItems=Config.menuItems,
                                        mode='inline',
                                        defaultOpenKeys=[],
                                        style={
                                            'height': '100%',
                                            'paddingBottom': '50px'
                                        }
                                    ),

                                    fac.AntdButton(
                                        fac.AntdIcon(
                                            id='fold-side-menu-icon',
                                            icon='antd-arrow-left'
                                        ),
                                        id='fold-side-menu',
                                        type='text',
                                        shape='circle',
                                        style={
                                            'position': 'absolute',
                                            'zIndex': 999,
                                            'top': '10px',
                                            'right': '-15px',
                                            'boxShadow': '0 4px 10px 0 rgba(0,0,0,.1)',
                                            'background': 'white'
                                        }
                                    )
                                ],
                                id='side-menu',
                                style={
                                    'width': '290px',
                                    'height': '100vh',
                                    'transition': 'width 0.2s',
                                    'borderRight': '1px solid rgb(240, 240, 240)',
                                    'paddingRight': 20
                                }
                            ),
                            offsetTop=0
                        ),
                        flex='none'
                    ),

                    fac.AntdCol(
                        [
                            html.Div(
                                id='docs-content',
                                style={
                                    'backgroundColor': 'rgb(255, 255, 255)'
                                }
                            )
                        ],
                        flex='auto'
                    ),

                    fac.AntdBackTop(
                        duration=0.5
                    )
                ],
                wrap=False
            )
        ]
    ),
    listenPropsMode='include',
    includeProps=Config.include_props,
    minimum=0.33,
    speed=800,
    debug=True
)


@app.callback(
    [Output('docs-content', 'children'),
     Output('router-menu', 'currentKey')],
    Input('url', 'pathname')
)
def render_docs_content(pathname):
    '''
    路由回调
    '''

    if pathname == '/what-is-fmc' or pathname == '/':
        pathname = '/what-is-fmc'
        return what_is_fuc.docs_content, pathname

    elif pathname == '/FefferyCaptcha':
        return FefferyCaptcha.docs_content, pathname

    elif pathname == '/FefferyExecuteJs':
        return FefferyExecuteJs.docs_content, pathname

    elif pathname == '/FefferyHighlightWords':
        return FefferyHighlightWords.docs_content, pathname

    elif pathname == '/FefferyQRCode':
        return FefferyQRCode.docs_content, pathname

    elif pathname == '/FefferyReload':
        return FefferyReload.docs_content, pathname

    elif pathname == '/FefferyStyle':
        return FefferyStyle.docs_content, pathname

    elif pathname == '/FefferyTopProgress':
        return FefferyTopProgress.docs_content, pathname

    elif pathname == '/FefferyCountDown':
        return FefferyCountDown.docs_content, pathname

    elif pathname == '/FefferyCssVar':
        return FefferyCssVar.docs_content, pathname

    elif pathname == '/FefferyExtraSpinner':
        return FefferyExtraSpinner.docs_content, pathname

    elif pathname == '/FefferyRawHTML':
        return FefferyRawHTML.docs_content, pathname

    elif pathname == '/FefferyBlockColorPicker':
        return FefferyBlockColorPicker.docs_content, pathname

    elif pathname == '/FefferyCircleColorPicker':
        return FefferyCircleColorPicker.docs_content, pathname

    elif pathname == '/FefferyEyeDropper':
        return FefferyEyeDropper.docs_content, pathname

    elif pathname == '/FefferyGithubColorPicker':
        return FefferyGithubColorPicker.docs_content, pathname

    elif pathname == '/FefferyHexColorPicker':
        return FefferyHexColorPicker.docs_content, pathname

    elif pathname == '/FefferyRgbColorPicker':
        return FefferyRgbColorPicker.docs_content, pathname

    elif pathname == '/FefferyTwitterColorPicker':
        return FefferyTwitterColorPicker.docs_content, pathname

    elif pathname == '/FefferyWheelColorPicker':
        return FefferyWheelColorPicker.docs_content, pathname

    elif pathname == '/FefferyGuide':
        return FefferyGuide.docs_content(), pathname

    elif pathname == '/FefferyScroll':
        return FefferyScroll.docs_content, pathname

    elif pathname == '/FefferyDocumentVisibility':
        return FefferyDocumentVisibility.docs_content, pathname

    elif pathname == '/FefferyGeolocation':
        return FefferyGeolocation.docs_content, pathname

    elif pathname == '/FefferyIdle':
        return FefferyIdle.docs_content, pathname

    elif pathname == '/FefferyInViewport':
        return FefferyInViewport.docs_content, pathname

    elif pathname == '/FefferyResponsive':
        return FefferyResponsive.docs_content, pathname

    elif pathname == '/FefferyWindowSize':
        return FefferyWindowSize.docs_content, pathname

    elif pathname == '/FefferyDiv':
        return FefferyDiv.docs_content, pathname

    elif pathname == '/FefferyExternalCss':
        return FefferyExternalCss.docs_content, pathname

    elif pathname == '/FefferyExternalJs':
        return FefferyExternalJs.docs_content, pathname

    elif pathname == '/FefferyFancyMessage':
        return FefferyFancyMessage.docs_content, pathname

    elif pathname == '/FefferyFancyNotification':
        return FefferyFancyNotification.docs_content, pathname

    elif pathname == '/FefferySessionStorage':
        return FefferySessionStorage.docs_content, pathname

    elif pathname == '/FefferyWebSocket':
        return FefferyWebSocket.docs_content, pathname

    elif pathname == '/FefferyShadowDom':
        return FefferyShadowDom.docs_content, pathname

    elif pathname == '/FefferyGrid':
        return FefferyGrid.docs_content, pathname

    elif pathname == '/FefferyGridItem':
        return FefferyGridItem.docs_content, pathname

    elif pathname == '/FefferyLazyLoad':
        return FefferyLazyLoad.docs_content(), pathname

    elif pathname == '/FefferyVirtualList':
        return FefferyVirtualList.docs_content(), pathname

    elif pathname == '/FefferyScrollbars':
        return FefferyScrollbars.docs_content, pathname

    elif pathname == '/FefferySetTitle':
        return FefferySetTitle.docs_content, pathname

    elif pathname == '/FefferyTimeout':
        return FefferyTimeout.docs_content, pathname

    elif pathname == '/FefferyFancyButton':
        return FefferyFancyButton.docs_content, pathname

    elif pathname == '/FefferyJsonViewer':
        return FefferyJsonViewer.docs_content, pathname

    elif pathname == '/FefferyShortcutPanel':
        return FefferyShortcutPanel.docs_content, pathname

    return fac.AntdResult(status='404', title='您访问的页面不存在！'), pathname


app.clientside_callback(
    '''
    (nClicks, oldStyle) => {
        if (nClicks) {
            if (oldStyle.width === '290px') {
                return [
                    {
                        'width': 20,
                        'height': '100vh',
                        'transition': 'width 0.2s',
                        'borderRight': '1px solid rgb(240, 240, 240)',
                        'paddingRight': 20
                    },
                    'antd-arrow-right'
                ]
            }
            return [
                {
                    'width': '290px',
                    'height': '100vh',
                    'transition': 'width 0.2s',
                    'borderRight': '1px solid rgb(240, 240, 240)',
                    'paddingRight': 20
                },
                'antd-arrow-left'
            ]
        }
        return window.dash_clientside.no_update;
    }
    ''',
    [Output('side-menu', 'style'),
     Output('fold-side-menu-icon', 'icon')],
    Input('fold-side-menu', 'nClicks'),
    State('side-menu', 'style')
)

app.clientside_callback(
    '''
    (nClicks, oldStyle) => {
        if (nClicks) {
            if (oldStyle.width === '600px') {
                return [
                    {
                        'width': 0,
                        'height': '100vh',
                        'borderLeft': '1px solid #f0f0f0',
                        'padding': '0 10px',
                        'position': 'relative',
                        'background': '#f2f3f5',
                        'transition': 'width 0.15s ease'
                    },
                    'antd-arrow-left'
                ]
            }
            return [
                {
                    'width': '600px',
                    'height': '100vh',
                    'borderLeft': '1px solid #f0f0f0',
                    'padding': '0 20px',
                    'position': 'relative',
                    'background': '#f2f3f5',
                    'transition': 'width 0.4s ease'
                },
                'antd-arrow-right'
            ]
        }
        return window.dash_clientside.no_update;
    }
    ''',
    [Output('side-props', 'style'),
     Output('fold-side-props-icon', 'icon')],
    Input('fold-side-props', 'nClicks'),
    State('side-props', 'style')
)

if __name__ == '__main__':
    app.run(debug=True)
