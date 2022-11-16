**id：** *string*型

　　用于设置*当前组件的唯一id信息*

**style：** *dict*型

　　用于设置*当前组件的css样式*

**className：** *string*型

　　用于设置*当前组件的css类名*

**children：** *组件型*

　　用于传入*嵌套的子元素*

**appendChild：** *组件型*

　　用于*快捷向已有children数组末尾追加子元素*，每次成功追加后`appendChild`会自动重置为`None`

**insertChild：** *dict型*

　　用于*快捷在已有children数组中指定位置插入新元素*，必要的键值对参数有：

- **index：** *int*型，用于*设置新元素的插入位序*
- **element：** *组件型*，用于*设置要插入的新元素*

**replaceChild：** *dict*型

　　用于*快捷替换已有children数组中的指定位置元素*，必要的键值对参数有：

- **index：** *int*型，用于*设置待替换元素在children数组中的位序*
- **element：** *组件型*，用于*设置要替换的新元素*

**deleteChildIndex：** *int*型

　　用于*快捷删除已有children数组中的指定位置元素*

**_width：** *int*型

　　用于*监听当前容器的像素宽度*

**_height：** *int*型

　　用于*监听当前容器的像素高度*

**debounceWait：** *int*型，默认为`150`

　　用于设置*容器宽度、高度监听的防抖延时*，单位：毫秒

**mouseEnterCount：** *int*型

　　用于*监听当前容器的鼠标移入事件发生次数*

**mouseLeaveCount：** *int*型

　　用于*监听当前容器的鼠标移出事件发生次数*

**nClicks：** *int*型

　　用于*监听当前容器的点击事件次数*

**nDoubleClicks：** *int*型

　　用于*监听当前容器的双击事件次数*

**enableListenContextMenu：** *bool*型，默认为`False`

　　用于设置*是否开启右键事件监听*，开启后会强制关闭当前容器内的默认右键菜单弹出

**contextMenuEvent：** *dict*型

　　当`enableListenContextMenu=True`时，用于*监听右键事件相关参数*

**isHovering：** *bool*型

　　用于*监听当前元素是否处于鼠标悬停状态*

**enableClickAway：** *bool*型，默认为`False`

　　用于设置*是否开启容器外点击事件监听*，当页面中开启此功能的`FefferyDiv`元素较多时会带来性能问题，请谨慎使用

**clickAwayCount：** *int*型

　　当`enableClickAway=True`时，用于*监听容器外点击事件次数*

**shadow：** *string*型，默认为`'no-shadow'`

　　用于*快捷为当前容器添加阴影效果*，可选的有`'no-shadow'`（无阴影）、`'hover-shadow'`（悬停时显示阴影）、`'always-shadow'`（持久阴影）