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
                'key': '/',
                'title': '通用组件'
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
