class Config:
    # 顶端进度条需要纳入的监听目标
    include_props = [
        'docs-content.children'
    ]

    # 定义侧边菜单树状结构数据
    menuItems = [
        {
            'component': 'ItemGroup',
            'props': {
                'key': '/',
                'title': '快速入门'
            },
            'children': [
                {
                    'component': 'Item',
                    'props': {
                        'key': '/what-is-fmc',
                        'href': '/what-is-fmc',
                        'title': 'fuc是什么？'
                    }
                }
            ]
        },
        {
            'component': 'ItemGroup',
            'props': {
                'key': '全部组件',
                'title': '全部组件'
            },
            'children': [
                {
                    'component': 'SubMenu',
                    'props': {
                        'key': '色彩选择类组件',
                        'title': '色彩选择类组件'
                    },
                    'children': [
                        {
                            'component': 'ItemGroup',
                            'props': {
                                'key': 'Block风格色彩选择器',
                                'title': 'Block风格色彩选择器'
                            },
                            'children': [
                                {
                                    'component': 'Item',
                                    'props': {
                                        'key': '/FefferyBlockColorPicker',
                                        'title': 'FefferyBlockColorPicker',
                                        'href': '/FefferyBlockColorPicker'
                                    }
                                }
                            ]
                        },
                        {
                            'component': 'ItemGroup',
                            'props': {
                                'key': 'Circle风格色彩选择器',
                                'title': 'Circle风格色彩选择器'
                            },
                            'children': [
                                {
                                    'component': 'Item',
                                    'props': {
                                        'key': '/FefferyCircleColorPicker',
                                        'title': 'FefferyCircleColorPicker',
                                        'href': '/FefferyCircleColorPicker'
                                    }
                                }
                            ]
                        },
                        {
                            'component': 'ItemGroup',
                            'props': {
                                'key': '色彩拾取组件',
                                'title': '色彩拾取组件'
                            },
                            'children': [
                                {
                                    'component': 'Item',
                                    'props': {
                                        'key': '/FefferyEyeDropper',
                                        'title': 'FefferyEyeDropper',
                                        'href': '/FefferyEyeDropper'
                                    }
                                }
                            ]
                        },
                        {
                            'component': 'ItemGroup',
                            'props': {
                                'key': 'Github风格色彩选择器',
                                'title': 'Github风格色彩选择器'
                            },
                            'children': [
                                {
                                    'component': 'Item',
                                    'props': {
                                        'key': '/FefferyGithubColorPicker',
                                        'title': 'FefferyGithubColorPicker',
                                        'href': '/FefferyGithubColorPicker'
                                    }
                                }
                            ]
                        },
                        {
                            'component': 'ItemGroup',
                            'props': {
                                'key': '16进制色彩选择器',
                                'title': '16进制色彩选择器'
                            },
                            'children': [
                                {
                                    'component': 'Item',
                                    'props': {
                                        'key': '/FefferyHexColorPicker',
                                        'title': 'FefferyHexColorPicker',
                                        'href': '/FefferyHexColorPicker'
                                    }
                                }
                            ]
                        },
                        {
                            'component': 'ItemGroup',
                            'props': {
                                'key': 'Rgb色彩选择器',
                                'title': 'Rgb色彩选择器'
                            },
                            'children': [
                                {
                                    'component': 'Item',
                                    'props': {
                                        'key': '/FefferyRgbColorPicker',
                                        'title': 'FefferyRgbColorPicker',
                                        'href': '/FefferyRgbColorPicker'
                                    }
                                }
                            ]
                        },
                        {
                            'component': 'ItemGroup',
                            'props': {
                                'key': 'Twitter风格色彩选择器',
                                'title': 'Twitter风格色彩选择器'
                            },
                            'children': [
                                {
                                    'component': 'Item',
                                    'props': {
                                        'key': '/FefferyTwitterColorPicker',
                                        'title': 'FefferyTwitterColorPicker',
                                        'href': '/FefferyTwitterColorPicker'
                                    }
                                }
                            ]
                        },
                        {
                            'component': 'ItemGroup',
                            'props': {
                                'key': 'Wheel风格色彩选择器',
                                'title': 'Wheel风格色彩选择器'
                            },
                            'children': [
                                {
                                    'component': 'Item',
                                    'props': {
                                        'key': '/FefferyWheelColorPicker',
                                        'title': 'FefferyWheelColorPicker',
                                        'href': '/FefferyWheelColorPicker'
                                    }
                                }
                            ]
                        }
                    ]
                },
                {
                    'component': 'SubMenu',
                    'props': {
                        'key': '监听类组件',
                        'title': '监听类组件'
                    },
                    'children': [
                        {
                            'component': 'ItemGroup',
                            'props': {
                                'key': '设备信息检测',
                                'title': '设备信息检测'
                            },
                            'children': [
                                {
                                    'component': 'Item',
                                    'props': {
                                        'key': '/FefferyDeviceDetect',
                                        'title': 'FefferyDeviceDetect',
                                        'href': '/FefferyDeviceDetect'
                                    }
                                }
                            ]
                        },
                        {
                            'component': 'ItemGroup',
                            'props': {
                                'key': '页面可见性监听',
                                'title': '页面可见性监听'
                            },
                            'children': [
                                {
                                    'component': 'Item',
                                    'props': {
                                        'key': '/FefferyDocumentVisibility',
                                        'title': 'FefferyDocumentVisibility',
                                        'href': '/FefferyDocumentVisibility'
                                    }
                                }
                            ]
                        },
                        {
                            'component': 'ItemGroup',
                            'props': {
                                'key': '地理位置监听',
                                'title': '地理位置监听'
                            },
                            'children': [
                                {
                                    'component': 'Item',
                                    'props': {
                                        'key': '/FefferyGeolocation',
                                        'title': 'FefferyGeolocation',
                                        'href': '/FefferyGeolocation'
                                    }
                                }
                            ]
                        },
                        {
                            'component': 'ItemGroup',
                            'props': {
                                'key': '闲置状态监听',
                                'title': '闲置状态监听'
                            },
                            'children': [
                                {
                                    'component': 'Item',
                                    'props': {
                                        'key': '/FefferyIdle',
                                        'title': 'FefferyIdle',
                                        'href': '/FefferyIdle'
                                    }
                                }
                            ]
                        },
                        {
                            'component': 'ItemGroup',
                            'props': {
                                'key': '元素可见性监听',
                                'title': '元素可见性监听'
                            },
                            'children': [
                                {
                                    'component': 'Item',
                                    'props': {
                                        'key': '/FefferyInViewport',
                                        'title': 'FefferyInViewport',
                                        'href': '/FefferyInViewport'
                                    }
                                }
                            ]
                        },
                        {
                            'component': 'ItemGroup',
                            'props': {
                                'key': '页面响应式监听',
                                'title': '页面响应式监听'
                            },
                            'children': [
                                {
                                    'component': 'Item',
                                    'props': {
                                        'key': '/FefferyResponsive',
                                        'title': 'FefferyResponsive',
                                        'href': '/FefferyResponsive'
                                    }
                                }
                            ]
                        },
                        {
                            'component': 'ItemGroup',
                            'props': {
                                'key': '浏览器窗口尺寸监听',
                                'title': '浏览器窗口尺寸监听'
                            },
                            'children': [
                                {
                                    'component': 'Item',
                                    'props': {
                                        'key': '/FefferyWindowSize',
                                        'title': 'FefferyWindowSize',
                                        'href': '/FefferyWindowSize'
                                    }
                                }
                            ]
                        }
                    ]
                },
                {
                    'component': 'SubMenu',
                    'props': {
                        'key': '拖拽类组件',
                        'title': '拖拽类组件'
                    },
                    'children': [
                        {
                            'component': 'ItemGroup',
                            'props': {
                                'key': '可拖拽网格',
                                'title': '可拖拽网格'
                            },
                            'children': [
                                {
                                    'component': 'Item',
                                    'props': {
                                        'key': '/FefferyGrid',
                                        'title': 'FefferyGrid 可拖拽网格',
                                        'href': '/FefferyGrid'
                                    }
                                },
                                {
                                    'component': 'Item',
                                    'props': {
                                        'key': '/FefferyGridItem',
                                        'title': 'FefferyGridItem 可拖拽网格项',
                                        'href': '/FefferyGridItem'
                                    }
                                }
                            ]
                        }
                    ]
                },
                {
                    'component': 'Item',
                    'props': {
                        'key': '/FefferyCaptcha',
                        'href': '/FefferyCaptcha',
                        'title': 'FefferyCaptcha 验证码'
                    }
                },
                {
                    'component': 'Item',
                    'props': {
                        'key': '/FefferyCountDown',
                        'href': '/FefferyCountDown',
                        'title': 'FefferyCountDown 倒计时'
                    }
                },
                {
                    'component': 'Item',
                    'props': {
                        'key': '/FefferyCssVar',
                        'href': '/FefferyCssVar',
                        'title': 'FefferyCssVar css变量更新'
                    }
                },
                {
                    'component': 'Item',
                    'props': {
                        'key': '/FefferyDiv',
                        'href': '/FefferyDiv',
                        'title': 'FefferyDiv 进阶div容器'
                    }
                },
                {
                    'component': 'Item',
                    'props': {
                        'key': '/FefferyExecuteJs',
                        'href': '/FefferyExecuteJs',
                        'title': 'FefferyExecuteJs js执行'
                    }
                },
                {
                    'component': 'Item',
                    'props': {
                        'key': '/FefferyExternalCss',
                        'href': '/FefferyExternalCss',
                        'title': 'FefferyExternalCss 外部css资源注入'
                    }
                },
                {
                    'component': 'Item',
                    'props': {
                        'key': '/FefferyExternalJs',
                        'href': '/FefferyExternalJs',
                        'title': 'FefferyExternalJs 外部js资源注入'
                    }
                },
                {
                    'component': 'Item',
                    'props': {
                        'key': '/FefferyExtraSpinner',
                        'href': '/FefferyExtraSpinner',
                        'title': 'FefferyExtraSpinner 额外加载动画'
                    }
                },
                {
                    'component': 'Item',
                    'props': {
                        'key': '/FefferyFancyButton',
                        'href': '/FefferyFancyButton',
                        'title': 'FefferyFancyButton 美观按钮'
                    }
                },
                {
                    'component': 'Item',
                    'props': {
                        'key': '/FefferyFancyMessage',
                        'href': '/FefferyFancyMessage',
                        'title': 'FefferyFancyMessage 美观消息提示'
                    }
                },
                {
                    'component': 'Item',
                    'props': {
                        'key': '/FefferyFancyNotification',
                        'href': '/FefferyFancyNotification',
                        'title': 'FefferyFancyNotification 美观通知'
                    }
                },
                {
                    'component': 'Item',
                    'props': {
                        'key': '/FefferyFullscreen',
                        'href': '/FefferyFullscreen',
                        'title': 'FefferyFullscreen 全屏化'
                    }
                },
                {
                    'component': 'Item',
                    'props': {
                        'key': '/FefferyGuide',
                        'href': '/FefferyGuide',
                        'title': 'FefferyGuide 功能引导'
                    }
                },
                {
                    'component': 'Item',
                    'props': {
                        'key': '/FefferyHighlightWords',
                        'href': '/FefferyHighlightWords',
                        'title': 'FefferyHighlightWords 关键词高亮'
                    }
                },
                {
                    'component': 'Item',
                    'props': {
                        'key': '/FefferyImagePaste',
                        'href': '/FefferyImagePaste',
                        'title': 'FefferyImagePaste 图片粘贴捕获'
                    }
                },
                {
                    'component': 'Item',
                    'props': {
                        'key': '/FefferyJsonViewer',
                        'href': '/FefferyJsonViewer',
                        'title': 'FefferyJsonViewer json数据展示'
                    }
                },
                {
                    'component': 'Item',
                    'props': {
                        'key': '/FefferyLazyLoad',
                        'href': '/FefferyLazyLoad',
                        'title': 'FefferyLazyLoad 懒加载容器'
                    }
                },
                # {
                #     'component': 'Item',
                #     'props': {
                #         'key': '/FefferyLazyLoadImage',
                #         'href': '/FefferyLazyLoadImage',
                #         'title': 'FefferyLazyLoadImage 图片懒加载'
                #     }
                # },
                {
                    'component': 'Item',
                    'props': {
                        'key': '/FefferyQRCode',
                        'href': '/FefferyQRCode',
                        'title': 'FefferyQRCode 二维码生成'
                    }
                },
                {
                    'component': 'Item',
                    'props': {
                        'key': '/FefferyRawHTML',
                        'href': '/FefferyRawHTML',
                        'title': 'FefferyRawHTML html源码渲染'
                    }
                },
                {
                    'component': 'Item',
                    'props': {
                        'key': '/FefferyReload',
                        'href': '/FefferyReload',
                        'title': 'FefferyReload 页面重载'
                    }
                },
                {
                    'component': 'Item',
                    'props': {
                        'key': '/FefferyScroll',
                        'href': '/FefferyScroll',
                        'title': 'FefferyScroll 滚动动作'
                    }
                },
                {
                    'component': 'Item',
                    'props': {
                        'key': '/FefferyScrollbars',
                        'href': '/FefferyScrollbars',
                        'title': 'FefferyScrollbars 滚动条容器'
                    }
                },
                {
                    'component': 'Item',
                    'props': {
                        'key': '/FefferySessionStorage',
                        'href': '/FefferySessionStorage',
                        'title': 'FefferySessionStorage 状态同步'
                    }
                },
                {
                    'component': 'Item',
                    'props': {
                        'key': '/FefferySetTitle',
                        'href': '/FefferySetTitle',
                        'title': 'FefferySetTitle 页面title更新'
                    }
                },
                {
                    'component': 'Item',
                    'props': {
                        'key': '/FefferyShadowDom',
                        'href': '/FefferyShadowDom',
                        'title': 'FefferyShadowDom 样式隔离'
                    }
                },
                {
                    'component': 'Item',
                    'props': {
                        'key': '/FefferyShortcutPanel',
                        'href': '/FefferyShortcutPanel',
                        'title': 'FefferyShortcutPanel 快捷方式面板'
                    }
                },
                # {
                #     'component': 'Item',
                #     'props': {
                #         'key': '/FefferySticky',
                #         'href': '/FefferySticky',
                #         'title': 'FefferySticky 进阶粘性布局'
                #     }
                # },
                {
                    'component': 'Item',
                    'props': {
                        'key': '/FefferyStyle',
                        'href': '/FefferyStyle',
                        'title': 'FefferyStyle 动态样式'
                    }
                },
                # {
                #     'component': 'Item',
                #     'props': {
                #         'key': '/FefferySyntaxHighlighter',
                #         'href': '/FefferySyntaxHighlighter',
                #         'title': 'FefferySyntaxHighlighter 代码语法高亮'
                #     }
                # },
                {
                    'component': 'Item',
                    'props': {
                        'key': '/FefferyTimeout',
                        'href': '/FefferyTimeout',
                        'title': 'FefferyTimeout 定时执行'
                    }
                },
                {
                    'component': 'Item',
                    'props': {
                        'key': '/FefferyTopProgress',
                        'href': '/FefferyTopProgress',
                        'title': 'FefferyTopProgress 顶部加载进度条'
                    }
                },
                {
                    'component': 'Item',
                    'props': {
                        'key': '/FefferyVirtualList',
                        'href': '/FefferyVirtualList',
                        'title': 'FefferyVirtualList 虚拟滚动列表'
                    }
                },
                {
                    'component': 'Item',
                    'props': {
                        'key': '/FefferyWebSocket',
                        'href': '/FefferyWebSocket',
                        'title': 'FefferyWebSocket WebSocket通信'
                    }
                },
            ]
        }
    ]
