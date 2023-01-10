**id：** *string*型

　　用于设置*当前组件的唯一id信息*

**deviceInfo：** *dict*型

　　用于*监听当前设备的一系列参数信息*，携带的键值对属性有：

- **isMobile：** *bool*型，*检测是否为手机、平板等移动设备*
- **isAndroid：** *bool*型，*检测是否为安卓系统*
- **isIOS：** *bool*型，*检测是否为ios系统*
- **isChrome：** *bool*型，*检测是否为Chrome浏览器*
- **isFirefox：** *bool*型，*检测是否为Firefox浏览器*
- **isSafari：** *bool*型，*检测是否为Safari浏览器*
- **isIE：** *bool*型，*检测是否为IE浏览器*
- **isEdge：** *bool*型，*检测是否为Edge浏览器*
- **osVersion：** *string*型，*检测系统版本*
- **osName：** *string*型，*检测系统名称*
- **browserVersion：** *string*型，*检测浏览器缩略版本*
- **fullBrowserVersion：** *string*型，*检测完整的浏览器版本*
- **browserName：** *string*型，*检测浏览器名称*
- **ua：** *string*型，*检测User-Agent信息*
- **deviceType：** *string*型，*检测设备类型*