import os
import time
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

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
    bot.run(TOKEN)
    print('Bot exited on ' + time.strftime('%Y-%m-%d %H:%M:%S'))