import json
import feffery_utils_components as fuc

# 国际化
from i18n import translator


class DeployConfig:
    """
    应用部署相关参数
    """

    # CDN模块名列表
    cdn_modules = [
        'DashRenderer',
        'dash_html_components',
        'dash_core_components',
        'feffery_antd_components',
        'feffery_utils_components',
        'feffery_markdown_components',
    ]


class AppConfig:
    """
    应用常规参数配置
    """

    # 应用默认标签页标题
    title = 'feffery-utils-components在线文档'

    # 应用logo地址
    logo_path = 'imgs/fuc-logo.svg'

    # 页首标题
    page_header_title = 'feffery-utils-components'

    # 当前组件版本
    library_version = fuc.__version__

    # 组件仓库地址
    library_repo = 'https://github.com/CNFeffery/feffery-utils-components'

    # 文档仓库地址
    doc_library_repo = 'https://github.com/CNFeffery/feffery-utils-docs'

    # 文档Gitee仓库地址
    doc_gitee_library_repo = 'https://gitee.com/cnfeffery/feffery-utils-docs'

    # 文档仓库分支名称
    doc_library_branch = 'main'

    # 当前应用是否为正式发布模式
    is_release = True

    # 文档贡献者信息
    doc_contributors = json.load(open('./public/contributors.json'))

    # 项目国际化指南地址
    i18n_guide_link = (
        'https://github.com/CNFeffery/feffery-utils-docs/issues/166'
    )

    @staticmethod
    def side_menu_items() -> list:
        # 侧边菜单栏数据结构
        return [
            {
                'component': 'ItemGroup',
                'props': {'key': '快速入门', 'title': translator.t('快速入门')},
                'children': [
                    {
                        'component': 'Item',
                        'props': {
                            'key': '/what-is-fuc',
                            'name': '/what-is-fuc',
                            'href': '/what-is-fuc',
                            'title': translator.t('fuc是什么'),
                        },
                    }
                ],
            },
            {'component': 'Divider', 'props': {'dashed': True}},
            {
                'component': 'ItemGroup',
                'props': {'key': '组件介绍', 'title': translator.t('组件介绍')},
                'children': [
                    {
                        'component': 'SubMenu',
                        'props': {'key': '通用', 'title': translator.t('通用')},
                        'children': [
                            {
                                'component': 'Item',
                                'props': {
                                    'key': '/FefferyBurger',
                                    'name': '/FefferyBurger',
                                    'title': translator.t(
                                        'FefferyBurger 动态菜单图标'
                                    ),
                                    'href': '/FefferyBurger',
                                },
                            },
                            {
                                'component': 'Item',
                                'props': {
                                    'key': '/FefferyDownload',
                                    'name': '/FefferyDownload',
                                    'title': translator.t(
                                        'FefferyDownload 文件下载'
                                    ),
                                    'href': '/FefferyDownload',
                                },
                            },
                            {
                                'component': 'Item',
                                'props': {
                                    'key': '/FefferyFancyButton',
                                    'name': '/FefferyFancyButton',
                                    'title': translator.t(
                                        'FefferyFancyButton 美观按钮'
                                    ),
                                    'href': '/FefferyFancyButton',
                                },
                            },
                        ],
                    },
                    {
                        'component': 'SubMenu',
                        'props': {
                            'key': '颜色选择',
                            'title': translator.t('颜色选择'),
                        },
                        'children': [
                            {
                                'component': 'Item',
                                'props': {
                                    'key': '/FefferyBlockColorPicker',
                                    'name': '/FefferyBlockColorPicker',
                                    'title': translator.t(
                                        'FefferyBlockColorPicker Block风格色彩选择器'
                                    ),
                                    'href': '/FefferyBlockColorPicker',
                                },
                            },
                            {
                                'component': 'Item',
                                'props': {
                                    'key': '/FefferyCircleColorPicker',
                                    'name': '/FefferyCircleColorPicker',
                                    'title': translator.t(
                                        'FefferyCircleColorPicker Circle风格色彩选择器'
                                    ),
                                    'href': '/FefferyCircleColorPicker',
                                },
                            },
                            {
                                'component': 'Item',
                                'props': {
                                    'key': '/FefferyEyeDropper',
                                    'name': '/FefferyEyeDropper',
                                    'title': translator.t(
                                        'FefferyEyeDropper 色彩拾取'
                                    ),
                                    'href': '/FefferyEyeDropper',
                                },
                            },
                            {
                                'component': 'Item',
                                'props': {
                                    'key': '/FefferyGithubColorPicker',
                                    'name': '/FefferyGithubColorPicker',
                                    'title': translator.t(
                                        'FefferyGithubColorPicker Github风格色彩选择器'
                                    ),
                                    'href': '/FefferyGithubColorPicker',
                                },
                            },
                            {
                                'component': 'Item',
                                'props': {
                                    'key': '/FefferyHexColorPicker',
                                    'name': '/FefferyHexColorPicker',
                                    'title': translator.t(
                                        'FefferyHexColorPicker 16进制色彩选择器'
                                    ),
                                    'href': '/FefferyHexColorPicker',
                                },
                            },
                            {
                                'component': 'Item',
                                'props': {
                                    'key': '/FefferyRgbColorPicker',
                                    'name': '/FefferyRgbColorPicker',
                                    'title': translator.t(
                                        'FefferyRgbColorPicker rgb色彩选择器'
                                    ),
                                    'href': '/FefferyRgbColorPicker',
                                },
                            },
                            {
                                'component': 'Item',
                                'props': {
                                    'key': '/FefferyTwitterColorPicker',
                                    'name': '/FefferyTwitterColorPicker',
                                    'title': translator.t(
                                        'FefferyTwitterColorPicker Twitter风格色彩选择器'
                                    ),
                                    'href': '/FefferyTwitterColorPicker',
                                },
                            },
                            {
                                'component': 'Item',
                                'props': {
                                    'key': '/FefferyWheelColorPicker',
                                    'name': '/FefferyWheelColorPicker',
                                    'title': translator.t(
                                        'FefferyWheelColorPicker Wheel风格色彩选择器'
                                    ),
                                    'href': '/FefferyWheelColorPicker',
                                },
                            },
                        ],
                    },
                    {
                        'component': 'SubMenu',
                        'props': {
                            'key': '动效',
                            'title': translator.t('动效'),
                        },
                        'children': [
                            {
                                'component': 'Item',
                                'props': {
                                    'key': '/FefferyAutoAnimate',
                                    'name': '/FefferyAutoAnimate',
                                    'title': translator.t(
                                        'FefferyAutoAnimate 自动动画'
                                    ),
                                    'href': '/FefferyAutoAnimate',
                                },
                            },
                            {
                                'component': 'Item',
                                'props': {
                                    'key': '/FefferyMotion',
                                    'name': '/FefferyMotion',
                                    'title': translator.t(
                                        'FefferyMotion 动画编排'
                                    ),
                                    'href': '/FefferyMotion',
                                },
                            },
                            {
                                'component': 'Item',
                                'props': {
                                    'key': '/FefferyBirdsBackground',
                                    'name': '/FefferyBirdsBackground',
                                    'title': translator.t(
                                        'FefferyBirdsBackground 3D-Birds背景'
                                    ),
                                    'href': '/FefferyBirdsBackground',
                                },
                            },
                            {
                                'component': 'Item',
                                'props': {
                                    'key': '/FefferyCellsBackground',
                                    'name': '/FefferyCellsBackground',
                                    'title': translator.t(
                                        'FefferyCellsBackground 3D-Cells背景'
                                    ),
                                    'href': '/FefferyCellsBackground',
                                },
                            },
                            {
                                'component': 'Item',
                                'props': {
                                    'key': '/FefferyCloudsBackground',
                                    'name': '/FefferyCloudsBackground',
                                    'title': translator.t(
                                        'FefferyCloudsBackground 3D-Clouds背景'
                                    ),
                                    'href': '/FefferyCloudsBackground',
                                },
                            },
                            {
                                'component': 'Item',
                                'props': {
                                    'key': '/FefferyCloudsTwoBackground',
                                    'name': '/FefferyCloudsTwoBackground',
                                    'title': translator.t(
                                        'FefferyCloudsTwoBackground 3D-CloudsTwo背景'
                                    ),
                                    'href': '/FefferyCloudsTwoBackground',
                                },
                            },
                            {
                                'component': 'Item',
                                'props': {
                                    'key': '/FefferyFogBackground',
                                    'name': '/FefferyFogBackground',
                                    'title': translator.t(
                                        'FefferyFogBackground 3D-Fog背景'
                                    ),
                                    'href': '/FefferyFogBackground',
                                },
                            },
                            {
                                'component': 'Item',
                                'props': {
                                    'key': '/FefferyGlobeBackground',
                                    'name': '/FefferyGlobeBackground',
                                    'title': translator.t(
                                        'FefferyGlobeBackground 3D-Globe背景'
                                    ),
                                    'href': '/FefferyGlobeBackground',
                                },
                            },
                            {
                                'component': 'Item',
                                'props': {
                                    'key': '/FefferyHaloBackground',
                                    'name': '/FefferyHaloBackground',
                                    'title': translator.t(
                                        'FefferyHaloBackground 3D-Halo背景'
                                    ),
                                    'href': '/FefferyHaloBackground',
                                },
                            },
                            {
                                'component': 'Item',
                                'props': {
                                    'key': '/FefferyNetBackground',
                                    'name': '/FefferyNetBackground',
                                    'title': translator.t(
                                        'FefferyNetBackground 3D-Net背景'
                                    ),
                                    'href': '/FefferyNetBackground',
                                },
                            },
                            {
                                'component': 'Item',
                                'props': {
                                    'key': '/FefferyRingsBackground',
                                    'name': '/FefferyRingsBackground',
                                    'title': translator.t(
                                        'FefferyRingsBackground 3D-Rings背景'
                                    ),
                                    'href': '/FefferyRingsBackground',
                                },
                            },
                            {
                                'component': 'Item',
                                'props': {
                                    'key': '/FefferyTopologyBackground',
                                    'name': '/FefferyTopologyBackground',
                                    'title': translator.t(
                                        'FefferyTopologyBackground 3D-Topology背景'
                                    ),
                                    'href': '/FefferyTopologyBackground',
                                },
                            },
                            {
                                'component': 'Item',
                                'props': {
                                    'key': '/FefferyTrunkBackground',
                                    'name': '/FefferyTrunkBackground',
                                    'title': translator.t(
                                        'FefferyTrunkBackground 3D-Trunk背景'
                                    ),
                                    'href': '/FefferyTrunkBackground',
                                },
                            },
                            {
                                'component': 'Item',
                                'props': {
                                    'key': '/FefferyWavesBackground',
                                    'name': '/FefferyWavesBackground',
                                    'title': translator.t(
                                        'FefferyWavesBackground 3D-Waves背景'
                                    ),
                                    'href': '/FefferyWavesBackground',
                                },
                            },
                            {
                                'component': 'Item',
                                'props': {
                                    'key': '/FefferyTiltHover',
                                    'name': '/FefferyTiltHover',
                                    'title': translator.t(
                                        'FefferyTiltHover 倾斜悬浮'
                                    ),
                                    'href': '/FefferyTiltHover',
                                },
                            },
                        ],
                    },
                    {
                        'component': 'SubMenu',
                        'props': {
                            'key': '加载动画',
                            'title': translator.t('加载动画'),
                        },
                        'children': [
                            {
                                'component': 'Item',
                                'props': {
                                    'key': '/FefferyExtraSpinner',
                                    'name': '/FefferyExtraSpinner',
                                    'title': translator.t(
                                        'FefferyExtraSpinner 额外加载动画'
                                    ),
                                    'href': '/FefferyExtraSpinner',
                                },
                            },
                            {
                                'component': 'Item',
                                'props': {
                                    'key': '/FefferyTopProgress',
                                    'name': '/FefferyTopProgress',
                                    'title': translator.t(
                                        'FefferyTopProgress 顶端加载进度条'
                                    ),
                                    'href': '/FefferyTopProgress',
                                },
                            },
                        ],
                    },
                    {
                        'component': 'SubMenu',
                        'props': {
                            'key': '容器',
                            'title': translator.t('容器'),
                        },
                        'children': [
                            {
                                'component': 'Item',
                                'props': {
                                    'key': '/FefferyDiv',
                                    'name': '/FefferyDiv',
                                    'title': translator.t(
                                        'FefferyDiv 进阶div容器'
                                    ),
                                    'href': '/FefferyDiv',
                                },
                            },
                            {
                                'component': 'Item',
                                'props': {
                                    'key': '/FefferyFixed',
                                    'name': '/FefferyFixed',
                                    'title': translator.t(
                                        'FefferyFixed 固定布局'
                                    ),
                                    'href': '/FefferyFixed',
                                },
                            },
                            {
                                'component': 'Item',
                                'props': {
                                    'key': '/FefferyHighlightWords',
                                    'name': '/FefferyHighlightWords',
                                    'title': translator.t(
                                        'FefferyHighlightWords 关键词高亮'
                                    ),
                                    'href': '/FefferyHighlightWords',
                                },
                            },
                            {
                                'component': 'Item',
                                'props': {
                                    'key': '/FefferyPortal',
                                    'name': '/FefferyPortal',
                                    'title': translator.t(
                                        'FefferyPortal 传送门'
                                    ),
                                    'href': '/FefferyPortal',
                                },
                            },
                            {
                                'component': 'Item',
                                'props': {
                                    'key': '/FefferyScrollbars',
                                    'name': '/FefferyScrollbars',
                                    'title': translator.t(
                                        'FefferyScrollbars 滚动条容器'
                                    ),
                                    'href': '/FefferyScrollbars',
                                },
                            },
                            {
                                'component': 'Item',
                                'props': {
                                    'key': '/FefferyShadowDom',
                                    'name': '/FefferyShadowDom',
                                    'title': translator.t(
                                        'FefferyShadowDom Shadow DOM'
                                    ),
                                    'href': '/FefferyShadowDom',
                                },
                            },
                            {
                                'component': 'Item',
                                'props': {
                                    'key': '/FefferySticky',
                                    'name': '/FefferySticky',
                                    'title': translator.t(
                                        'FefferySticky 粘性布局'
                                    ),
                                    'href': '/FefferySticky',
                                },
                            },
                        ],
                    },
                    {
                        'component': 'SubMenu',
                        'props': {
                            'key': '拖拽交互',
                            'title': translator.t('拖拽交互'),
                        },
                        'children': [
                            {
                                'component': 'Item',
                                'props': {
                                    'key': '/FefferyDraggable',
                                    'name': '/FefferyDraggable',
                                    'title': translator.t(
                                        'FefferyDraggable 可拖拽'
                                    ),
                                    'href': '/FefferyDraggable',
                                },
                            },
                            {
                                'component': 'Item',
                                'props': {
                                    'key': '/FefferyGrid',
                                    'name': '/FefferyGrid',
                                    'title': translator.t(
                                        'FefferyGrid 可拖拽网格'
                                    ),
                                    'href': '/FefferyGrid',
                                },
                            },
                            {
                                'component': 'Item',
                                'props': {
                                    'key': '/FefferyGridItem',
                                    'name': '/FefferyGridItem',
                                    'title': translator.t(
                                        'FefferyGridItem 可拖拽网格项'
                                    ),
                                    'href': '/FefferyGridItem',
                                },
                            },
                            {
                                'component': 'Item',
                                'props': {
                                    'key': '/FefferyRND',
                                    'name': '/FefferyRND',
                                    'title': translator.t(
                                        'FefferyRND 尺寸可调可拖拽'
                                    ),
                                    'href': '/FefferyRND',
                                },
                            },
                            {
                                'component': 'Item',
                                'props': {
                                    'key': '/FefferySortable',
                                    'name': '/FefferySortable',
                                    'title': translator.t(
                                        'FefferySortable 排序列表'
                                    ),
                                    'href': '/FefferySortable',
                                },
                            },
                        ],
                    },
                    {
                        'component': 'SubMenu',
                        'props': {
                            'key': '播放器',
                            'title': translator.t('播放器'),
                        },
                        'children': [
                            {
                                'component': 'Item',
                                'props': {
                                    'key': '/FefferyAPlayer',
                                    'name': '/FefferyAPlayer',
                                    'title': translator.t(
                                        'FefferyAPlayer 音频播放'
                                    ),
                                    'href': '/FefferyAPlayer',
                                },
                            },
                            {
                                'component': 'Item',
                                'props': {
                                    'key': '/FefferyDPlayer',
                                    'name': '/FefferyDPlayer',
                                    'title': translator.t(
                                        'FefferyDPlayer 视频播放'
                                    ),
                                    'href': '/FefferyDPlayer',
                                },
                            },
                            {
                                'component': 'Item',
                                'props': {
                                    'key': '/FefferyMusicPlayer',
                                    'name': '/FefferyMusicPlayer',
                                    'title': translator.t(
                                        'FefferyMusicPlayer 音乐播放'
                                    ),
                                    'href': '/FefferyMusicPlayer',
                                },
                            },
                        ],
                    },
                    {
                        'component': 'SubMenu',
                        'props': {
                            'key': '编辑器',
                            'title': translator.t('编辑器'),
                        },
                        'children': [
                            {
                                'component': 'Item',
                                'props': {
                                    'key': '/FefferyMarkdownEditor',
                                    'name': '/FefferyMarkdownEditor',
                                    'title': translator.t(
                                        'FefferyMarkdownEditor markdown编辑器'
                                    ),
                                    'href': '/FefferyMarkdownEditor',
                                },
                            },
                            {
                                'component': 'Item',
                                'props': {
                                    'key': '/FefferyRichTextEditor',
                                    'name': '/FefferyRichTextEditor',
                                    'title': translator.t(
                                        'FefferyRichTextEditor 富文本编辑器'
                                    ),
                                    'href': '/FefferyRichTextEditor',
                                },
                            },
                            {
                                'component': 'Item',
                                'props': {
                                    'key': '/FefferyVditor',
                                    'name': '/FefferyVditor',
                                    'title': translator.t(
                                        'FefferyVditor 类Typora的markdown编辑器'
                                    ),
                                    'href': '/FefferyVditor',
                                },
                            },
                        ],
                    },
                    {
                        'component': 'SubMenu',
                        'props': {
                            'key': '图片',
                            'title': translator.t('图片'),
                        },
                        'children': [
                            {
                                'component': 'Item',
                                'props': {
                                    'key': '/FefferyAnimatedImage',
                                    'name': '/FefferyAnimatedImage',
                                    'title': translator.t(
                                        'FefferyAnimatedImage 动图'
                                    ),
                                    'href': '/FefferyAnimatedImage',
                                },
                            },
                            {
                                'component': 'Item',
                                'props': {
                                    'key': '/FefferyDom2Image',
                                    'name': '/FefferyDom2Image',
                                    'title': translator.t(
                                        'FefferyDom2Image 元素转图片'
                                    ),
                                    'href': '/FefferyDom2Image',
                                },
                            },
                            {
                                'component': 'Item',
                                'props': {
                                    'key': '/FefferyImageCropper',
                                    'name': '/FefferyImageCropper',
                                    'title': translator.t(
                                        'FefferyImageCropper 图片裁剪'
                                    ),
                                    'href': '/FefferyImageCropper',
                                },
                            },
                            {
                                'component': 'Item',
                                'props': {
                                    'key': '/FefferyImageGallery',
                                    'name': '/FefferyImageGallery',
                                    'title': translator.t(
                                        'FefferyImageGallery 相册'
                                    ),
                                    'href': '/FefferyImageGallery',
                                },
                            },
                            {
                                'component': 'Item',
                                'props': {
                                    'key': '/FefferyPhotoSphereViewer',
                                    'name': '/FefferyPhotoSphereViewer',
                                    'title': translator.t(
                                        'FefferyPhotoSphereViewer 全景图片查看器'
                                    ),
                                    'href': '/FefferyPhotoSphereViewer',
                                },
                            },
                        ],
                    },
                    {
                        'component': 'SubMenu',
                        'props': {
                            'key': '数据录入',
                            'title': translator.t('数据录入'),
                        },
                        'children': [
                            {
                                'component': 'Item',
                                'props': {
                                    'key': '/FefferyEmojiPicker',
                                    'name': '/FefferyEmojiPicker',
                                    'title': translator.t(
                                        'FefferyEmojiPicker emoji选择器'
                                    ),
                                    'href': '/FefferyEmojiPicker',
                                },
                            },
                            {
                                'component': 'Item',
                                'props': {
                                    'key': '/FefferyImagePaste',
                                    'name': '/FefferyImagePaste',
                                    'title': translator.t(
                                        'FefferyImagePaste 粘贴板图片获取'
                                    ),
                                    'href': '/FefferyImagePaste',
                                },
                            },
                        ],
                    },
                    {
                        'component': 'SubMenu',
                        'props': {
                            'key': '事件监听',
                            'title': translator.t('事件监听'),
                        },
                        'children': [
                            {
                                'component': 'Item',
                                'props': {
                                    'key': '/FefferyDeviceDetect',
                                    'name': '/FefferyDeviceDetect',
                                    'title': translator.t(
                                        'FefferyDeviceDetect 设备信息检测'
                                    ),
                                    'href': '/FefferyDeviceDetect',
                                },
                            },
                            {
                                'component': 'Item',
                                'props': {
                                    'key': '/FefferyDocumentVisibility',
                                    'name': '/FefferyDocumentVisibility',
                                    'title': translator.t(
                                        'FefferyDocumentVisibility 页面可见性检查'
                                    ),
                                    'href': '/FefferyDocumentVisibility',
                                },
                            },
                            {
                                'component': 'Item',
                                'props': {
                                    'key': '/FefferyEventListener',
                                    'name': '/FefferyEventListener',
                                    'title': translator.t(
                                        'FefferyEventListener 通用事件监听'
                                    ),
                                    'href': '/FefferyEventListener',
                                },
                            },
                            {
                                'component': 'Item',
                                'props': {
                                    'key': '/FefferyGeolocation',
                                    'name': '/FefferyGeolocation',
                                    'title': translator.t(
                                        'FefferyGeolocation 地理位置监听'
                                    ),
                                    'href': '/FefferyGeolocation',
                                },
                            },
                            {
                                'component': 'Item',
                                'props': {
                                    'key': '/FefferyIdle',
                                    'name': '/FefferyIdle',
                                    'title': translator.t(
                                        'FefferyIdle 闲置状态监听'
                                    ),
                                    'href': '/FefferyIdle',
                                },
                            },
                            {
                                'component': 'Item',
                                'props': {
                                    'key': '/FefferyInViewport',
                                    'name': '/FefferyInViewport',
                                    'title': translator.t(
                                        'FefferyInViewport 元素可见性检查'
                                    ),
                                    'href': '/FefferyInViewport',
                                },
                            },
                            {
                                'component': 'Item',
                                'props': {
                                    'key': '/FefferyKeyPress',
                                    'name': '/FefferyKeyPress',
                                    'title': translator.t(
                                        'FefferyKeyPress 按键事件监听'
                                    ),
                                    'href': '/FefferyKeyPress',
                                },
                            },
                            {
                                'component': 'Item',
                                'props': {
                                    'key': '/FefferyListenDrag',
                                    'name': '/FefferyListenDrag',
                                    'title': translator.t(
                                        'FefferyListenDrag 拖拽事件监听'
                                    ),
                                    'href': '/FefferyListenDrag',
                                },
                            },
                            {
                                'component': 'Item',
                                'props': {
                                    'key': '/FefferyListenDrop',
                                    'name': '/FefferyListenDrop',
                                    'title': translator.t(
                                        'FefferyListenDrop 放置事件监听'
                                    ),
                                    'href': '/FefferyListenDrop',
                                },
                            },
                            {
                                'component': 'Item',
                                'props': {
                                    'key': '/FefferyListenElementSize',
                                    'name': '/FefferyListenElementSize',
                                    'title': translator.t(
                                        'FefferyListenElementSize 元素尺寸监听'
                                    ),
                                    'href': '/FefferyListenElementSize',
                                },
                            },
                            {
                                'component': 'Item',
                                'props': {
                                    'key': '/FefferyListenHover',
                                    'name': '/FefferyListenHover',
                                    'title': translator.t(
                                        'FefferyListenHover 鼠标悬停监听'
                                    ),
                                    'href': '/FefferyListenHover',
                                },
                            },
                            {
                                'component': 'Item',
                                'props': {
                                    'key': '/FefferyListenPaste',
                                    'name': '/FefferyListenPaste',
                                    'title': translator.t(
                                        'FefferyListenPaste 全局粘贴监听'
                                    ),
                                    'href': '/FefferyListenPaste',
                                },
                            },
                            {
                                'component': 'Item',
                                'props': {
                                    'key': '/FefferyListenScroll',
                                    'name': '/FefferyListenScroll',
                                    'title': translator.t(
                                        'FefferyListenScroll 滚动条监听'
                                    ),
                                    'href': '/FefferyListenScroll',
                                },
                            },
                            {
                                'component': 'Item',
                                'props': {
                                    'key': '/FefferyListenUnload',
                                    'name': '/FefferyListenUnload',
                                    'title': translator.t(
                                        'FefferyListenUnload 页面关闭监听'
                                    ),
                                    'href': '/FefferyListenUnload',
                                },
                            },
                            {
                                'component': 'Item',
                                'props': {
                                    'key': '/FefferyLocation',
                                    'name': '/FefferyLocation',
                                    'title': translator.t(
                                        'FefferyLocation 地址监听'
                                    ),
                                    'href': '/FefferyLocation',
                                },
                            },
                            {
                                'component': 'Item',
                                'props': {
                                    'key': '/FefferyLongPress',
                                    'name': '/FefferyLongPress',
                                    'title': translator.t(
                                        'FefferyLongPress 长按事件监听'
                                    ),
                                    'href': '/FefferyLongPress',
                                },
                            },
                            {
                                'component': 'Item',
                                'props': {
                                    'key': '/FefferyMediaQuery',
                                    'name': '/FefferyMediaQuery',
                                    'title': translator.t(
                                        'FefferyMediaQuery 媒体查询监听'
                                    ),
                                    'href': '/FefferyMediaQuery',
                                },
                            },
                            {
                                'component': 'Item',
                                'props': {
                                    'key': '/FefferyMousePosition',
                                    'name': '/FefferyMousePosition',
                                    'title': translator.t(
                                        'FefferyMousePosition 鼠标位置监听'
                                    ),
                                    'href': '/FefferyMousePosition',
                                },
                            },
                            {
                                'component': 'Item',
                                'props': {
                                    'key': '/FefferyNetwork',
                                    'name': '/FefferyNetwork',
                                    'title': translator.t(
                                        'FefferyNetwork 网络状态信息监听'
                                    ),
                                    'href': '/FefferyNetwork',
                                },
                            },
                            {
                                'component': 'Item',
                                'props': {
                                    'key': '/FefferyPageLeave',
                                    'name': '/FefferyPageLeave',
                                    'title': translator.t(
                                        'FefferyPageLeave 鼠标离开页面监听'
                                    ),
                                    'href': '/FefferyPageLeave',
                                },
                            },
                            {
                                'component': 'Item',
                                'props': {
                                    'key': '/FefferyResponsive',
                                    'name': '/FefferyResponsive',
                                    'title': translator.t(
                                        'FefferyResponsive 页面响应式监听'
                                    ),
                                    'href': '/FefferyResponsive',
                                },
                            },
                            {
                                'component': 'Item',
                                'props': {
                                    'key': '/FefferyTextSelection',
                                    'name': '/FefferyTextSelection',
                                    'title': translator.t(
                                        'FefferyTextSelection 文字选中监听'
                                    ),
                                    'href': '/FefferyTextSelection',
                                },
                            },
                            {
                                'component': 'Item',
                                'props': {
                                    'key': '/FefferyWindowSize',
                                    'name': '/FefferyWindowSize',
                                    'title': translator.t(
                                        'FefferyWindowSize 浏览器窗口尺寸监听'
                                    ),
                                    'href': '/FefferyWindowSize',
                                },
                            },
                        ],
                    },
                    {
                        'component': 'SubMenu',
                        'props': {
                            'key': '静态资源控制',
                            'title': translator.t('静态资源控制'),
                        },
                        'children': [
                            {
                                'component': 'Item',
                                'props': {
                                    'key': '/FefferyExternalCss',
                                    'name': '/FefferyExternalCss',
                                    'title': translator.t(
                                        'FefferyExternalCss 外部css资源动态注入'
                                    ),
                                    'href': '/FefferyExternalCss',
                                },
                            },
                            {
                                'component': 'Item',
                                'props': {
                                    'key': '/FefferyExternalJs',
                                    'name': '/FefferyExternalJs',
                                    'title': translator.t(
                                        'FefferyExternalJs 外部js资源动态注入'
                                    ),
                                    'href': '/FefferyExternalJs',
                                },
                            },
                        ],
                    },
                    {
                        'component': 'SubMenu',
                        'props': {
                            'key': '页面控制',
                            'title': translator.t('页面控制'),
                        },
                        'children': [
                            {
                                'component': 'Item',
                                'props': {
                                    'key': '/FefferyFullscreen',
                                    'name': '/FefferyFullscreen',
                                    'title': translator.t(
                                        'FefferyFullscreen 全屏化'
                                    ),
                                    'href': '/FefferyFullscreen',
                                },
                            },
                        ],
                    },
                    {
                        'component': 'SubMenu',
                        'props': {
                            'key': '样式控制',
                            'title': translator.t('样式控制'),
                        },
                        'children': [],
                    },
                    {
                        'component': 'SubMenu',
                        'props': {
                            'key': '通信',
                            'title': translator.t('通信'),
                        },
                        'children': [],
                    },
                    {
                        'component': 'SubMenu',
                        'props': {
                            'key': '文件预览',
                            'title': translator.t('文件预览'),
                        },
                        'children': [],
                    },
                    {
                        'component': 'SubMenu',
                        'props': {
                            'key': '尺寸调整',
                            'title': translator.t('尺寸调整'),
                        },
                        'children': [],
                    },
                    {
                        'component': 'SubMenu',
                        'props': {
                            'key': '安全',
                            'title': translator.t('安全'),
                        },
                        'children': [],
                    },
                    {
                        'component': 'SubMenu',
                        'props': {
                            'key': '性能优化',
                            'title': translator.t('性能优化'),
                        },
                        'children': [],
                    },
                    {
                        'component': 'SubMenu',
                        'props': {
                            'key': '数据展示',
                            'title': translator.t('数据展示'),
                        },
                        'children': [],
                    },
                    {
                        'component': 'SubMenu',
                        'props': {
                            'key': '数据展示',
                            'title': translator.t('数据展示'),
                        },
                        'children': [],
                    },
                    {
                        'component': 'SubMenu',
                        'props': {
                            'key': '反馈',
                            'title': translator.t('反馈'),
                        },
                        'children': [],
                    },
                    {
                        'component': 'SubMenu',
                        'props': {
                            'key': '存储',
                            'title': translator.t('存储'),
                        },
                        'children': [],
                    },
                    {
                        'component': 'SubMenu',
                        'props': {
                            'key': '验证码',
                            'title': translator.t('验证码'),
                        },
                        'children': [],
                    },
                    {
                        'component': 'SubMenu',
                        'props': {
                            'key': '其他',
                            'title': translator.t('其他'),
                        },
                        'children': [],
                    },
                ],
            },
            # {
            #     'component': 'ItemGroup',
            #     'props': {'key': '更新日志', 'title': translator.t('更新日志')},
            #     'children': [
            #         {
            #             'component': 'SubMenu',
            #             'props': {
            #                 'key': '0.2.x版本',
            #                 'title': '0.2.x',
            #             },
            #             'children': [
            #                 {
            #                     'component': 'Item',
            #                     'props': {
            #                         'key': '/changelog-' + version,
            #                         'name': '/changelog-' + version,
            #                         'title': version,
            #                         'href': '/changelog-' + version,
            #                     },
            #                 }
            #                 for version in []
            #             ],
            #         }
            #     ],
            # },
        ]

    # 侧边菜单栏key值 -> 展开项节点key值数组
    side_menu_expand_keys = {
        '/FefferyBurger': ['通用'],
        '/FefferyDownload': ['通用'],
        '/FefferyFancyButton': ['通用'],
        '/FefferyBlockColorPicker': ['颜色选择'],
        '/FefferyCircleColorPicker': ['颜色选择'],
        '/FefferyEyeDropper': ['颜色选择'],
        '/FefferyGithubColorPicker': ['颜色选择'],
        '/FefferyHexColorPicker': ['颜色选择'],
        '/FefferyRgbColorPicker': ['颜色选择'],
        '/FefferyTwitterColorPicker': ['颜色选择'],
        '/FefferyWheelColorPicker': ['颜色选择'],
        '/FefferyAutoAnimate': ['动效'],
        '/FefferyMotion': ['动效'],
        '/FefferyBirdsBackground': ['动效'],
        '/FefferyCellsBackground': ['动效'],
        '/FefferyCloudsBackground': ['动效'],
        '/FefferyCloudsTwoBackground': ['动效'],
        '/FefferyFogBackground': ['动效'],
        '/FefferyGlobeBackground': ['动效'],
        '/FefferyHaloBackground': ['动效'],
        '/FefferyNetBackground': ['动效'],
        '/FefferyRingsBackground': ['动效'],
        '/FefferyTopologyBackground': ['动效'],
        '/FefferyTrunkBackground': ['动效'],
        '/FefferyWavesBackground': ['动效'],
        '/FefferyTiltHover': ['动效'],
        '/FefferyExtraSpinner': ['加载动画'],
        '/FefferyTopProgress': ['加载动画'],
        '/FefferyDiv': ['容器'],
        '/FefferyFixed': ['容器'],
        '/FefferyHighlightWords': ['容器'],
        '/FefferyPortal': ['容器'],
        '/FefferyScrollbars': ['容器'],
        '/FefferyShadowDom': ['容器'],
        '/FefferySticky': ['容器'],
        '/FefferyDraggable': ['拖拽交互'],
        '/FefferyGrid': ['拖拽交互'],
        '/FefferyGridItem': ['拖拽交互'],
        '/FefferyRND': ['拖拽交互'],
        '/FefferySortable': ['拖拽交互'],
        '/FefferyAPlayer': ['播放器'],
        '/FefferyDPlayer': ['播放器'],
        '/FefferyMusicPlayer': ['播放器'],
        '/FefferyMarkdownEditor': ['编辑器'],
        '/FefferyRichTextEditor': ['编辑器'],
        '/FefferyVditor': ['编辑器'],
        '/FefferyAnimatedImage': ['图片'],
        '/FefferyDom2Image': ['图片'],
        '/FefferyImageCropper': ['图片'],
        '/FefferyImageGallery': ['图片'],
        '/FefferyPhotoSphereViewer': ['图片'],
        '/FefferyEmojiPicker': ['数据录入'],
        '/FefferyImagePaste': ['数据录入'],
        '/FefferyDeviceDetect': ['事件监听'],
        '/FefferyDocumentVisibility': ['事件监听'],
        '/FefferyEventListener': ['事件监听'],
        '/FefferyGeolocation': ['事件监听'],
        '/FefferyIdle': ['事件监听'],
        '/FefferyInViewport': ['事件监听'],
        '/FefferyKeyPress': ['事件监听'],
        '/FefferyListenDrag': ['事件监听'],
        '/FefferyListenDrop': ['事件监听'],
        '/FefferyListenElementSize': ['事件监听'],
        '/FefferyListenHover': ['事件监听'],
        '/FefferyListenPaste': ['事件监听'],
        '/FefferyListenScroll': ['事件监听'],
        '/FefferyListenUnload': ['事件监听'],
        '/FefferyLocation': ['事件监听'],
        '/FefferyLongPress': ['事件监听'],
        '/FefferyMediaQuery': ['事件监听'],
        '/FefferyMousePosition': ['事件监听'],
        '/FefferyNetwork': ['事件监听'],
        '/FefferyPageLeave': ['事件监听'],
        '/FefferyResponsive': ['事件监听'],
        '/FefferyTextSelection': ['事件监听'],
        '/FefferyWindowSize': ['事件监听'],
        '/FefferyExternalCss': ['静态资源控制'],
        '/FefferyExternalJs': ['静态资源控制'],
        '/FefferyFullscreen': ['页面控制'],
    }
