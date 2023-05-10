**id：** *string*型

　　用于设置*当前组件的唯一id信息*

**cookieKey：** *string*型，必填

　　用于*设置要绑定的cookie键名*

**defaultValue：** *string*型

　　当`cookieKey`对应的cookie在浏览器中无有效值时，用于*对当前cookie进行初始化赋值*

**value：** *string*型

　　用于*对当前cookie进行值更新*，也可以在当前组件初始化时，同步当前cookie在浏览器中的有效值

**expires：** *int*型

　　用于*设置当前cookie的有效时长*，单位：秒，默认有效时长为当前标签页会话期间

**pathname：** *string*型，默认为`'/'`

　　用于*设置当前cookie值可用的路径*

**secure：** *bool*型，默认为`False`

　　用于*设置当前cookie是否仅允许通过https安全传输*