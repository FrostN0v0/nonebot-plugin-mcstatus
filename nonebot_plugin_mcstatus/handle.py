from typing import List, cast

from mcstatus import JavaServer,MinecraftServer,BedrockServer

from nonebot.adapters.onebot.v11 import Message,MessageSegment,GroupMessageEvent
from src.plugins.nonebot_plugin_mcstatus.data import Data, Server
from src.plugins.nonebot_plugin_mcstatus.parser import Namespace

from pathlib import Path
from selenium import webdriver
import os
import time
from PIL import Image,ImageFont,ImageDraw
import base64

class Handle:
    @classmethod
    async def check(cls, args: Namespace) -> str:
        try:
            ping = await MinecraftServer.lookup(args.address).async_ping()
            status = True
        except:
            ping = None
            status = False
        chromedriver = "C:\Program Files\Google\Chrome\Application\chromedriver"
        os.environ["webdriver.chrome.driver"] = chromedriver
        driver = webdriver.Chrome(chromedriver)
        driver.get(f"https://adorable0v0.top/mcs/?host={args.address}")
        driver.set_window_size(960, 1080)
        driver.find_element_by_xpath("/html/body/div").screenshot("C:/sk/data/mc/img/server.png")
        driver.quit()
        im = Image.open("C:/sk/data/mc/img/server.png")
        try:
            server = JavaServer.lookup(args.address)
        except:
            server = BedrockServer.lookup(args.address)
        Nstatus = server.status()
        # 获取并处理服务器图标，缓存到本地发送
        a = Nstatus.favicon
        b = a.split(',')[1]
        img_data = base64.b64decode(b)
        with open('C:/sk/data/mc/img/icon.png', 'wb+') as f:
            f.write(img_data)
        im2 = Image.open("C:/sk/data/mc/img/icon.png")
        im2 = im2.resize((128,128))
        im.paste(im2, (25, 25))
        dw = ImageDraw.Draw(im)
        ft = ImageFont.truetype(font='C:/sk/resources/font/yzz.ttc', size=20)
        oping_data = Nstatus.latency.real
        ping_data = round(oping_data,1)
        dw.text(xy=(560, 105), text=f'{ping_data}MS', fill=(0, 255, 127), font=ft)
        im.save('C:/sk/data/mc/img/result.png')
        server_icon = Path('C:/sk/data/mc/img/result.png')
        return (MessageSegment.image(server_icon))

    @classmethod
    async def add(cls, args: Namespace) -> str:
        try:
            await MinecraftServer.lookup(args.address).async_ping()
            status = True
        except:
            status = False

        Data().add_server(
            Server(name=args.name, address=args.address, status=status),
            args.user_id,
            args.group_id,
        )

        return "添加服务器成功！"

    @classmethod
    async def remove(cls, args: Namespace) -> str:
        Data().remove_server(args.name, args.user_id, args.group_id)

        return "移除服务器成功！"

    @classmethod
    async def list(cls, args: Namespace) -> str:
        server_list = Data().get_server_list(args.user_id, args.group_id)

        if server_list:
            return "本群关注服务器列表如下：\n" + "\n".join(
                f"[{'o' if server.status else 'x'}] {server.name} ({server.address})"
                for server in cast(List[Server], server_list)
            )
        else:
            return "本群关注服务器列表为空！"
    @classmethod
    async def p(cls, args: Namespace) -> str:
        try:
            server_list = Data().get_server_list(args.user_id, args.group_id)
            if args.name in (
                server.name
                for server in server_list
                            ):
                for server in server_list:
                    if args.name == server.name:
                        address = server.address
                        chromedriver = "C:\Program Files\Google\Chrome\Application\chromedriver"
                        os.environ["webdriver.chrome.driver"] = chromedriver
                        driver = webdriver.Chrome(chromedriver)
                        driver.get(f"https://adorable0v0.top/mcs/?host={address}")
                        driver.set_window_size(960, 1080)
                        driver.find_element_by_xpath("/html/body/div").screenshot("C:/sk/data/mc/img/server.png")
                        driver.quit()
                        im = Image.open("C:/sk/data/mc/img/server.png")
                        try:
                            server = JavaServer.lookup(address)
                        except:
                            server = BedrockServer.lookup(address)
                        Nstatus = server.status()
                        # 获取并处理服务器图标，缓存到本地发送
                        a = Nstatus.favicon
                        b = a.split(',')[1]
                        img_data = base64.b64decode(b)
                        with open('C:/sk/data/mc/img/icon.png', 'wb+') as f:
                            f.write(img_data)
                        im2 = Image.open("C:/sk/data/mc/img/icon.png")
                        im2 = im2.resize((128, 128))
                        im.paste(im2, (25, 25))
                        dw = ImageDraw.Draw(im)
                        ft = ImageFont.truetype(font='C:/sk/resources/font/yzz.ttc', size=20)
                        oping_data = Nstatus.latency.real
                        ping_data = round(oping_data, 1)
                        dw.text(xy=(560, 105), text=f'{ping_data}MS', fill=(0, 255, 127), font=ft)
                        im.save('C:/sk/data/mc/img/result.png')
                        server_icon = Path('C:/sk/data/mc/img/result.png')
                        return (MessageSegment.image(server_icon))
            else:
                return "没有找到对应该名称的已记录服务器"
        except Exception as err:
            print(err)
