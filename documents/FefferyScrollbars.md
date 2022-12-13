**id：** *string*型

　　用于设置*当前组件的唯一id信息*

**style：** *dict*型

　　用于设置*当前组件的css样式*

**className：** *string*型

　　用于设置*当前组件的css类名*

**children：** *组件型*

　　用于传入*嵌套的子元素*

**autoHide：** *bool*型，默认为`True`

　　设置*是否当容器内timeout时长内无鼠标操作后自动隐藏滚动条*

**forceVisible：** *bool*或*string*型，默认为`False`

　　用于设置*是否强制展示滚动条*，也可以设置为`'x'`或`'y'`指定要显示滚动条的方向

**timeout：** *int*型，默认为`1000`

　　用于设置*滚动条无操作自动隐藏的等待时长*

**scrollbarMinSize：** *int*型，默认为`25`

　　用于设置*滚动条最小像素长度*

**scrollbarMaxSize：** *int*型

　　用于设置*滚动条最大像素长度*，默认无限制

　　