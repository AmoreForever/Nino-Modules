#▄▀█ █▀▄▀█ █▀█ █▀█ █▀▀
#█▀█ █░▀░█ █▄█ █▀▄ ██▄
#          
#             © Copyright 2022
#
#          https://t.me/the_farkhodov 
#
# 🔒 Licensed under the GNU GPLv3
# 🌐 https://www.gnu.org/licenses/agpl-3.0.html
# meta developer: @the_farkhodov


from .. import loader, utils
from asyncio import sleep
from telethon.tl.types import Message
import random

class HighpingMod(loader.Module):
	strings = {
	"name": "Inlinehighping", 
	"res": "Response time",
	"upd": "Uptime:",
	}
	strings_ru = {
	"res": "Скорость отклика",
	"upd": "Прошло с проследней перезагрузки:",
	}
	"""High Ping"""
	async def hpingcmd(self, message:Message):
		"""Fake Inline ping!"""
		res = self.strings("res")
		upd = self.strings("upd")
		ran1 = random.randint(1, 45000)
		ran2 = random.randint(10, 999)
		ran3 = random.randint(0, 23)
		ran4 = random.randint(10, 60)
		ran5 = random.randint(10, 60)
		await self.animate(
		message,
		[f"<code>🐻 Nofin...</code>"] + [f"▫️ <b>{res}</b>: <code>{ran1}.{ran2}</code> <b>ms</b>\n▫️ <b>{upd} {ran3}:{ran4}:{ran5}</b>"],
		interval=0.3,
		inline=True,
	)
	