from discord.ext.commands import Bot
from discord import Intents
import dotenv
import os


dotenv.load_dotenv()

TOKEN = os.getenv("CLIENT_TOKEN")

intents = Intents()
intents.messages = True
intents.dm_messages = True

bot = Bot(
    command_prefix=">",
    intents=intents
)

bot.load_extension("cogs.facts")
bot.run(TOKEN)