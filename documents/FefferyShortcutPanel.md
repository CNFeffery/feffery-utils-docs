**id：** *string*型

　　用于设置*当前组件的唯一id信息*

**locale：** *string*型，默认为`'zh'`

　　用于*设置辅助文案的默认语言*，可选的有`'zh'`、`'en'`

**data：** `list[dict]`型，必填

　　用于*定义当前面板所包含的快捷指令菜单元素*，每个*dict*型元素代表一条指令菜单项，其可用的键值对参数有：

- **id：** *string*型，必填，用于*为当前指令菜单项设置唯一id*
- **title：** *string*型，必填，用于*设置当前指令菜单项的显示标题内容*
- **hotkey：** *string*型，用于*设置当前指令菜单项的触发快捷键方式*，如`cmd+k,ctrl+k`
- **handler：** *string*型，用于*为当前菜单项设置触发时要执行的javascript回调函数字符串*
- **parent：** *string*型，用于*为当前指令菜单项设置所属的上一层级指令菜单项id信息*
- **keywords：** *string*型，用于*为当前指令菜单项设置搜索时使用的关联关键词*
- **children：** `list[string]`型，用于*为当前指令菜单项设置下一层级子项id信息数组*
- **section：** *string*型，用于*为当前指令菜单项设置分组标签*

**triggeredHotkey：** *dict*型

　　用于*监听指令菜单项选中事件*，具有键值对属性：

- **id：** *string*型，用于*记录当前被触发的指令菜单项id信息*
- **timestamp：** *int*型，用于*记录触发时的时间戳信息*

**placeholder：** *string*型

　　用于*设置搜索输入框的提示文案*，`locale='zh'`时默认为`'输入指令或进行搜索...'`，`locale='en'`时默认为`'Type a command or search...'`

**openHotkey：** *string*型，默认为`'cmd+k,ctrl+k'`

　　用于*设置触发指令面板显示的快捷键*

**theme：** *string*型，默认为`'light'`

　　用于*为指令面板设置主题风格*，可选的有`'light'`、`'dark'`

**open：** *bool*型，默认为`False`

　　用于*手动控制指令面板显示*，每次更新为`True`触发面板显示后都会自动重置为`False`

**close：** *bool*型，默认为`False`

　　用于*手动控制指令面板关闭*，每次更新为`True`触发面板关闭后都会自动重置为`False`

**panelStyles：** *dict*型

　　用于*快捷配置指令面板相关全局作用样式*，可用的键值对参数有：

- **width：** *string*型，默认为`'640px'`，用于*设置面板宽度*
- **overflowBackground：** *string*型，默认为`'rgba(255, 255, 255, 0.5)'`，用于*设置面板选项滚动区域背景色*
- **textColor：** *string*型，默认为`'rgb(60, 65, 73)'`，用于*设置面板字体颜色*
- **fontSize：** *string*型，默认为`'16px'`，用于*设置面板字体尺寸*
- **top：** *string*型，默认为`'20%'`，用于*设置面板到页面顶端的距离*
- **accentColor：** *string*型，默认为`'rgb(110, 94, 210)'`，用于*设置面板的主色*
- **secondaryBackgroundColor：** *string*型，默认为`'rgb(239, 241, 244)'`，用于*设置面板的次要背景色*
- **secondaryTextColor：** *string*型，默认为`'rgb(107, 111, 118)'`，用于*设置面板次要文字颜色*
- **selectedBackground：** *string*型，默认为`'rgb(248, 249, 251)'`，用于*设置面板已选中项背景色*
- **actionsHeight：** *string*型，默认为`'300px'`，用于*设置面板高度*
- **groupTextColor：** *string*型，默认为`'rgb(144, 149, 157)'`，用于*设置面板选项分组标签文字颜色*
- **zIndex：** *int*型，默认为`1`，用于*设置面板的z-index属性*

**searchValue：** *string*型

　　用于*监听当前输入框内的文字内容*