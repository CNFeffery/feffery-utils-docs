**id：** *string*型

　　用于设置*当前组件的唯一id信息*

**style：** *dict*型

　　用于设置*当前组件的css样式*

**className：** *string*型

　　用于设置*当前组件的css类名*

**children：** *组件型*

　　用于传入*嵌套的子元素*

**nClicks：** *int*型，默认为`0`

　　用于*监听当前按钮被点击的次数*

**debounceWait：** *int*型，默认为`0`

　　用于*设置针对nClicks更新的防抖等待时长*，单位：毫秒，从而避免用户快速连击按钮导致的回调频繁触发

**type：** *string*型，默认为`'primary'`

　　用于*设置按钮的样式类型*，可选的有`'primary'`、`'secondary'`、`'danger'`

**disabled：** *bool*型，默认为`False`

　　用于*设置是否禁用按钮*

**href：** *string*型

　　当*需要按钮充当链接跳转功能时*，用于设置链接地址

**target：** *string*型，默认为`'_blank'`

　　用于*设置按钮的链接跳转行为*

**before：** *组件型*

　　用于*为按钮设置前缀内嵌元素*

**after：** *组件型*

　　用于*为按钮设置后缀内嵌元素*

**ripple：** *bool*型，默认为`False`

　　用于*设置是否开启点击涟漪效果*