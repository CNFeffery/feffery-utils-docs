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
                    'component': 'Item',
                    'props': {
                        'key': '/FefferyCaptcha',
                        'href': '/FefferyCaptcha',
                        'title': 'FefferyCaptcha 验证码'
                    }
                },
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
                        'key': '/FefferyExecuteJs',
                        'href': '/FefferyExecuteJs',
                        'title': 'FefferyExecuteJs js执行'
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
                        'key': '/FefferyStyle',
                        'href': '/FefferyStyle',
                        'title': 'FefferyStyle 动态样式'
                    }
                },
                {
                    'component': 'Item',
                    'props': {
                        'key': '/FefferyTopProgress',
                        'href': '/FefferyTopProgress',
                        'title': 'FefferyTopProgress 顶部加载进度条'
                    }
                }
            ]
        }
    ]
