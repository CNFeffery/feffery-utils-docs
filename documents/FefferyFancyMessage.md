**id：** *string*型

　　用于设置*当前组件的唯一id信息*

**style：** *dict*型

　　用于设置*当前组件的css样式*

**className：** *string*型

　　用于设置*当前组件的css类名*

**children：** *组件型*

　　用于传入*嵌套的子元素*

**visible：** *bool*型，默认为`True`

　　用于设置*是否显示当前消息弹窗*

**position：** *string*型，默认为`'top-center'`

　　用于设置*当前消息提示弹窗的方位*，可选的有`'top-left'`、`'top-center'`、`'top-right'`、`'bottom-left'`、`'bottom-center'`、`'bottom-right'`

**reverseOrder：** *bool*型，默认为`True`

　　用于设置*较新的消息提示弹窗是否从底部进行追加*

**containerClassName：** *string*型

　　用于设置*消息提示容器的css类*

**containerStyle：** *dict*型

　　用于设置*消息提示容器的css样式*

**gutter：** *int*型，默认为`8`

　　用于设置*相邻消息提示容器之间的像素间距*

**type：** *string*型，默认为`'blank'`

　　用于设置*消息提示的类型*，可选的有`'blank'`、`'success'`、`'error'`

**duration：** *int*型，默认为`4000`

　　用于设置*每条消息提示的停留持续时长*，单位：毫秒

**icon：** *组件型*

　　用于*自定义作为图标的元素内容*