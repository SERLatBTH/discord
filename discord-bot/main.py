import os
import time
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
def load_discord_token():
    try:
        return os.environ["DISCORD_TOKEN"]
    except KeyError:
        raise NameError("DISCORD_TOKEN env does not exist. Unable to proceed.")

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True

# Define the command prefix
bot = commands.Bot(command_prefix='$', intents=intents)
tree = bot.tree

@bot.event
async def on_ready():
    print(f'Bot is ready. Logged in as {bot.user}')
    await tree.sync()

@tree.command(name='test', description='Test command')
async def test(interaction: discord.Integration):
    await interaction.response.send_message('Test command works!')

if __name__ == '__main__':
    token = load_discord_token()
    bot.run(token)
    print('Bot exited on ' + time.strftime('%Y-%m-%d %H:%M:%S'))