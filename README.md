### 本仓库Fork自[Nonebot Plugin MCStatus](https://github.com/nonepkg/nonebot-plugin-mcstatus)

基于 [nonebot2](https://github.com/nonebot/nonebot2) 和 [go-cqhttp](https://github.com/Mrs4s/go-cqhttp) 的 Minecraft 服务器状态查询插件

修改了消息反馈形式，查询到的状态将以图片返回
能够返回玩家列表、在线人数、MOTD信息、服务器图标以及Ping值
部分信息返回需要在服务端server.properties文件中开启服务器query功能
- `enable-query=true` 开启query功能
- `query.port=25565` query端口（默认即可无需调整）

### 安装

#### 克隆此仓库至Nonebot生成的`plugins`文件夹中

`git clone https://github.com/FrostN0v0/nonebot_plugin_mcstatus.git`

### 使用

**使用前请先确保命令前缀为空，否则请在以下命令前加上命令前缀 (默认为 `/` )。**

- `mc list` 查看当前会话（群/私聊）的关注服务器列表
- `mc add server address` 添加服务器到当前会话（群/私聊）的关注服务器列表
- `mc remove server` 从当前会话（群/私聊）的关注服务器列表移除服务器
- `mc check address` 查看指定地址的服务器状态（一次性）
- `mc ping <name>` 检查对应服务器的状态

