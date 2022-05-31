from typing import cast

import nonebot
from mcstatus import MinecraftServer
from nonebot import get_bots
from nonebot.adapters.onebot.v11 import (
    Bot,
    GroupMessageEvent,
    MessageEvent,
    PrivateMessageEvent,
)
from nonebot.params import ShellCommandArgs
from nonebot.plugin import on_shell_command, require

from src.plugins.nonebot_plugin_mcstatus.data import Data, ServerList
from src.plugins.nonebot_plugin_mcstatus.handle import Handle
from src.plugins.nonebot_plugin_mcstatus.parser import ArgNamespace, mc_parser

scheduler = require("nonebot_plugin_apscheduler").scheduler

# 注册 shell_like 事件响应器
mc = on_shell_command("mc", parser=mc_parser, priority=5)

@mc.handle()
async def _(bot: Bot, event: MessageEvent, args: ArgNamespace = ShellCommandArgs()):
    args.user_id = event.user_id if isinstance(event, PrivateMessageEvent) else None
    args.group_id = event.group_id if isinstance(event, GroupMessageEvent) else None
    args.is_admin = (
        event.sender.role in ["admin", "owner"]
        if isinstance(event, GroupMessageEvent)
        else False
    )
    if hasattr(args, "handle"):
        result = await getattr(Handle, args.handle)(args)
        if result:
            await bot.send(event, result)
