**id：** *string*型

　　用于设置*当前组件的唯一id信息*

**pasteText：** *string*型

　　用于*监听最近一次有效粘贴事件对应的文本内容*

**pasteCount：** *int*型，默认为`0`

　　用于*监听有效粘贴事件累计发生次数*

**enableListenPaste：** *bool*型，默认为`False`

　　用于*强制设置是否启用全局文本粘贴事件监听*

**targetContainerId：** *string*型

　　用于*设置粘贴事件发生的目标容器id*，当`enableListenPaste=False`且此参数有效设置时，只有用户鼠标移入目标容器内进行粘贴时才会监听粘贴事件