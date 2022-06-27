
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from .. import loader, utils

def register(cb):
	cb(InstaMod())
chat = 101159919
class InstaMod(loader.Module):
	"""InstaSave"""

	strings = {"name": "InstaSaveMod"}

	def __init__(self):
		self.name = self.strings['name']
		self._me = None
		self._ratelimit = []

	async def client_ready(self, client, db):
		self._db = db
		self.client = client
		self.me = await client.get_me()

	async def instcmd(self, message):
		""".inst {link}"""

		args = utils.get_args_raw(message)
		async with message.client.conversation(chat) as conv:
			await utils.answer(message, 'Скачиваю...')
			response = conv.wait_event(events.NewMessage(incoming=True, from_users=chat, chats=chat))
			bot_send_link = await message.client.send_message(chat, args)
			response = await response
			await response.download_media("hui.mp4")
			await message.client.send_file(message.to_id, "hui.mp4")
			await response.delete()
			await bot_send_link.delete()
			await message.delete()
			os.remove("hui.mp4")