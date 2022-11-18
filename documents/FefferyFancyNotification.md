**id：** *string*型

　　用于设置*当前组件的唯一id信息*

**style：** *dict*型

　　用于设置*当前组件的css样式*

**className：** *string*型

　　用于设置*当前组件的css类名*

**children：** *组件型*

　　用于传入*嵌套的子元素*

**type：** *string*型

　　用于设置*通知框的类型*，可选的有`'info'`、`'success'`、`'warning'`、`'error'`

**visible：** *bool*型，默认为`True`

　　用于设置*是否显示当前通知框*

**position：** *string*型，默认为`'top-right'`

　　用于设置*当前通知框的方位*，可选的有`'top-left'`、`'top-center'`、`'top-right'`、`'bottom-left'`、`'bottom-center'`、`'bottom-right'`

**autoClose：** *bool*或*int*型，默认为`5000`

　　用于设置*通知框的自动关闭行为*，`False`表示不会自动关闭，传入*int*型则用于定义从通知框显现，到自动关闭的延时，单位：毫秒

**closable：** *bool*型，默认为`True`

　　用于设置*通知框是否可手动关闭*

**hideProgressBar：** *bool*型，默认为`False`

　　用于设置*是否为通知框渲染关闭倒计时进度条*

**pauseOnHover：** *bool*型，默认为`True`

　　用于设置*当鼠标悬停于通知框之上时，是否暂停自动关闭倒计时*

**closeOnClick：** *bool*型，默认为`True`

　　用于设置*是否允许通知框在被点击后自动关闭*

**newestOnTop：** *bool*型，默认为`False`

　　用于设置*较新的通知框是否从更顶端的位置弹出*

**toastClassName：** *string*型

　　用于设置*通知框的css类*

**bodyClassName：** *string*型

　　用于设置*通知框内容区的css类*

**progressClassName：** *string*型

　　用于设置*通知框进度条的css类*

**progressStyle：** *dict*型

　　用于设置*通知框进度条的css样式*

**draggable：** *bool*型，默认为`True`

　　用于设置*当前通知框是否可拖拽*

**draggablePercent：** *int*型，默认为`80`

　　用于设置*通知框被拖拽位移宽度百分比阈值*，如果超出这个阈值，则被拖拽的通知框会被手动关闭

**containerId：** *string*型

　　当通知框需要在局部容器内弹出时，用于设置*此局部容器的id*

**limit：** *int*型

　　用于设置*同时允许出现的通知框数量上限*

**theme：** *string*型，默认为`'light'`

　　用于设置*通知框风格主题*，可选的有`'light'`、`'dark'`、`'colored'`