**id：** *string*型

　　用于设置*当前组件的唯一id信息*

**socketUrl：** *string*型

　　用于设置*要建立连接的WebSocket服务url*

**reconnectLimit：** *int*型，默认为`3`

　　用于设置*连接重试次数*

**reconnectInterval：** *int*型，默认为`3000`

　　用于设置*相邻重连尝试的等待时间间隔*，单位：毫秒

**operation：** *string*型

　　用于设置*即将要执行的行为*，可选的有`'connect'`（重新连接）、`'disconnect'`（断开连接）、`'send'`（发送信息），每次更新`operation`参数执行完操作后，`operation`都会自动重置为`None`

**message：** *string*型

　　当通过`operation`参数发送信息时，用于设置*要发送的信息内容*

**latestMessage：** *string*型

　　用于监听*最近一次从服务器发送来的信息*

**state：** *string*型

　　用于监听*当前连接的状态*，有`'connecting'`（建立连接中）、`'open'`（保持连接）、`'closing'`（断开连接中）、`'closed'`（已断开连接）